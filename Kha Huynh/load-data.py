# importing packages
import json
import pandas as pd
import numpy as np
import psycopg2
import psycopg2.extras
from datetime import datetime


file_name = '/home/labadmin/work/data-science-capstone-project/data/LABEVENTS.csv'
# file_name = '/home/labadmin/work/data-science-capstone-project/data/LABEVENTS-1000.csv'
chunksize = 50000
table_name = 'labevents_transform_v3'

def execute_values(conn, df):
  global max_id, inserted_count
  # SQL query to execute
  query = "INSERT INTO "+table_name+"(row_key,subject_id,hadm_id,charttime,item_values) VALUES (%s,%s,%s,%s,%s) ON CONFLICT (row_key) DO UPDATE SET item_values = "+table_name+".item_values || %s::jsonb"

  # creating a cursor object
  cursor = conn.cursor()
  try:
    for index, row in df.iterrows():
      row_list = [row['ROW_KEY'],row['SUBJECT_ID'],row['HADM_ID'],row['CHARTTIME'],row['ITEM_VAUES'],row['ITEM_VAUES']]
      cursor.execute(query, row_list)
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print("Error: %s" % error)
    conn.rollback()
    cursor.close()
    return 0

  cursor.close()
  
def build_key(subject_id, hadm_id, charttime):
  key = str(subject_id) + '_' + ('n' if hadm_id is None else str(hadm_id)) + '_' + charttime.strftime('%Y%m%d%H%M%S')
  return key

conn = psycopg2.connect(
  database="capstone_db", user='capstone', password='capstone', host='127.0.0.1', port='5432'
)
psycopg2.extensions.register_adapter(dict, psycopg2.extras.Json)

for chunk in pd.read_csv(file_name, chunksize=chunksize,
                         usecols = ['SUBJECT_ID','HADM_ID','ITEMID','CHARTTIME','VALUE','VALUENUM','VALUEUOM','FLAG']):
  df = pd.DataFrame(columns=['ROW_INDEX','ROW_KEY','SUBJECT_ID','HADM_ID','CHARTTIME','TMP_ITEMS'])
  df.set_index("ROW_INDEX", inplace = True)
  chunk = chunk.replace(np.nan, None)
  
  for index, row in chunk.iterrows():
    subject_id = int(row['SUBJECT_ID'])
    hadm_id = None if row['HADM_ID'] is None else int(row['HADM_ID'])
    charttime = pd.to_datetime(row['CHARTTIME'])
    row_key = build_key(subject_id, hadm_id, charttime)
    values = {}
    if row['VALUENUM'] is not None:
      valuenum_f = float(row['VALUENUM'])
      valuenum_i = int(row['VALUENUM'])
      values['valuenum'] = valuenum_i if valuenum_i == valuenum_f else valuenum_f
    if row['FLAG'] is not None:
      values['flag'] = row['FLAG']
    if row['VALUE'] is not None:
      values['value'] = row['VALUE']
    if row['VALUEUOM'] is not None:
      values['valueuom'] = row['VALUEUOM']
    item_values = {str(row['ITEMID']):values}
    if row_key in df.index:
      row_values = df.loc[row_key]
      row_values['TMP_ITEMS'].update(item_values)
    else:
      new_row_values = [row_key,subject_id,hadm_id,charttime,item_values]
      df.loc[row_key] = new_row_values

  df['ITEM_VAUES'] = df['TMP_ITEMS'].apply(json.dumps)
  execute_values(conn=conn, df=df)
  print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " processed "+str(chunk.index.stop)+"+ rows")
