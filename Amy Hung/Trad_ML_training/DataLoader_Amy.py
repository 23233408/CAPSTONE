"""
Below extract are functions I contributed during the project 
(for complete DataLoader, please refer to the "DataLoader.py" in src directory)
"""

import pandas as pd
import numpy as np, warnings
from pathlib import Path
import os
from importlib import reload

import src.utils as utils
reload(utils)

import src.engineer_features as ef
reload(ef)

class DataLoader:

  ROOT_DIR = Path('../..')
  
  def __init__(self, ROOT_DIR):
      self.ROOT_DIR = ROOT_DIR

  def extract_full_data_by_features(self, df_labevents, df_demographic, df_desc_labitems, hours, feature_filename='', feature_no = -1, output_filename=''):
      """
      Create the train data file.

      Parameters:
      - df_labevents: the labevents dataframe
      - df_demographic: the demographic dataframe
      - df_desc_labitems: the labitems description dataframe
      - hours: first n hours to extract
      - feature_no: the number of features to extract. Default =-1 to get all features in potential_events file
      - output_filename: the output filename. Default is stored in 'data/Model input data/t<hours>.csv
    
      Returns:
      - The result dataframe is saved as csv file in data/Model input data/ folder.
      """
      
      df_final = self.extract_train_data_by_features(df_labevents, df_demographic, df_desc_labitems, hours, feature_filename, feature_no, output_filename)

      # Obtain the new admittime from lab_events
      df_new_admittime = df_labevents[['SUBJECT_ID', 'HADM_ID', 'NEW_ADMITTIME']].drop_duplicates(subset=['SUBJECT_ID', 'HADM_ID'])

      # Create dataframe with Demographic data with all unique combinations of ['SUBJECT_ID', 'HADM_ID']
      all_hadm_data = df_demographic[['SUBJECT_ID', 'HADM_ID', 'AGE', 'GENDER', 'ADMITTIME', 'DISCHTIME', 'IS_SEPSIS']].drop_duplicates(subset=['SUBJECT_ID', 'HADM_ID'])
      all_hadm_data['GENDER_NUM'] = all_hadm_data['GENDER'].replace({'M': 0, 'F': 1})
      all_hadm_data.drop(columns=["GENDER"], inplace=True)
      
      # Add 'NEW_ADMITTIME' to all_hadm_data
      all_hadm_data = pd.merge(all_hadm_data, df_new_admittime, on=['SUBJECT_ID', 'HADM_ID'], how='left')

      # If there is any NaN in NEW_ADMITTIME, fill it with ADMITTIME
      all_hadm_data['NEW_ADMITTIME'].fillna(all_hadm_data['ADMITTIME'], inplace=True)

      # Compute the hospitalised duration for every admission
      all_hadm_data['HOSPITALISED_DURATION'] = ((all_hadm_data['DISCHTIME'] - all_hadm_data['NEW_ADMITTIME']).dt.total_seconds() / 3600 + 0.5).round().astype(int)
     
      # Filter rows with hospitalised duration > hours
      all_hadm_data = all_hadm_data[all_hadm_data['HOSPITALISED_DURATION'] >= hours]

      # Drop all the irrelevant columns
      all_hadm_data = all_hadm_data.drop(['ADMITTIME', 'DISCHTIME', 'NEW_ADMITTIME', 'HOSPITALISED_DURATION'], axis=1)

      # Drop the demographic columns from df_full
      df_final = df_final.drop(['AGE', 'GENDER_NUM', 'IS_SEPSIS'], axis=1)

      # Merge this with df_final
      df_full = pd.merge(all_hadm_data, df_final, on=['SUBJECT_ID', 'HADM_ID'], how='left')

      # fill all null VALUENUM by -999 and save to csv file
      df_full = df_full.fillna(-999)

      # compute SOFA score
      df_full['SOFA'] = ef.get_sofa_score(df=df_full)

      try:
        utils.save_csv(df_final, output_filename)
      except:
        utils.save_csv(df_full, self.ROOT_DIR / f'data/full_data/t{hours}.csv')

      return df_full