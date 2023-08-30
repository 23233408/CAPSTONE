import os
import pandas as pd
from datetime import datetime

output_dir = '/home/labadmin/work/data-science-capstone-project/data/labevents_transform_sepsis_parquet'
file_name = 'labevents_transform_sepsis'
print(str(datetime.now()) + ' Start')

# List all Parquet files in the output folder
parquet_files = [f'{output_dir}/{file}' for file in os.listdir(output_dir) if file.endswith('.parquet')]

# Read all Parquet files into a list of DataFrames
dfs = [pd.read_parquet(file) for file in parquet_files]

# Concatenate the list of DataFrames into a single DataFrame
df = pd.concat(dfs, ignore_index=True)
print(len(df))
print(str(datetime.now()) + ' End')
print(df)
