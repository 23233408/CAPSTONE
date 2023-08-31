import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine


chunksize = 25000
output_dir = '/home/labadmin/work/data-science-capstone-project/data/labevents_transform_sepsis_parquet'
file_name = 'labevents_transform_sepsis'

# Define query to select data from table
sql_query = "select * from v_labevents_transform_sepsis_v2"

# Define PostgreSQL connection parameters
db_username = 'capstone'
db_password = 'capstone'
db_hostname = 'localhost'
db_port = '5432'
db_name = 'capstone_db'

# Connect to PostgreSQL database
db_uri = f'postgresql+psycopg2://{db_username}:{db_password}@{db_hostname}:{db_port}/{db_name}'
engine = create_engine(db_uri)
conn = engine.connect().execution_options(stream_results=True)

print(str(datetime.now()) + ' Start')

# Read the data using pandas
df = pd.read_sql_query(sql=sql_query, 
                       con=conn,
                       index_col='row_key',
                       chunksize=chunksize)
idx = 1
# Write each chunk to Parquet
for chunk in df:
  idx_num = '{:0>2}'.format(idx)
  print(str(datetime.now()) + ' index ' + idx_num)
  chunk.to_parquet(f'{output_dir}/{file_name}_{idx_num}.parquet', engine='fastparquet', compression='SNAPPY')
  idx = idx + 1
print(str(datetime.now()) + ' End')
