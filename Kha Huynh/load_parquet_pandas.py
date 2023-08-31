import os
import pandas as pd
from datetime import datetime

output_dir = '/home/labadmin/work/data-science-capstone-project/data/labevents_transform_sepsis_parquet'
file_name = 'labevents_transform_sepsis'

# List all Parquet files in the output folder
parquet_files = sorted([f'{output_dir}/{file}' for file in os.listdir(output_dir) if file.endswith('.parquet')])

print(str(datetime.now()) + ' Start')

# Read all Parquet files and concatenate the list of DataFrames into a single DataFrame
df = None
for file in parquet_files:
  df_i = pd.read_parquet(file, 'fastparquet')
  print(str(datetime.now()) + ' ' + file)
  if df is None:
    df = df_i
  else:
    df = pd.concat([df, df_i], ignore_index = True)

print(str(datetime.now()) + ' End')

print(len(df))
