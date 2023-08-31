import os
import dask.dataframe as dd
from datetime import datetime

output_dir = '/home/labadmin/work/data-science-capstone-project/data/labevents_transform_parquet'
file_name = 'labevents_transform'

print(str(datetime.now()) + ' Start')

# Read all Parquet files and concatenate the list of DataFrames into a single DataFrame
ddf = dd.read_parquet(path=f'{output_dir}/*.parquet',
                      index='row_key',
                      engine='fastparquet')

print(str(datetime.now()) + ' ' + str(len(ddf)))
# print(ddf)

# Get OutOfMemory crash when converting to pandas
# df = ddf.compute()

print(str(datetime.now()) + ' End')
