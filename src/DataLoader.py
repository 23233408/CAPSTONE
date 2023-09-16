import pandas as pd
import numpy as np, warnings
from pathlib import Path
import os
from importlib import reload

import src.utils as utils
reload(utils)

class DataLoader:

  ROOT_DIR = Path('../..')
  
  def __init__(self, ROOT_DIR):
      self.ROOT_DIR = ROOT_DIR

  # def set_root_dir(root_dir):
  #   global ROOT_DIR
  #   ROOT_DIR = root_dir

  def load_descriptions(self):
    """
    Load the description tables of D_ICD_DIAGNOSES icd, D_LABITEMS, D_ITEMS

    Parameters: N/A

    Returns:
    - df_desc_icd: the D_ICD_DIAGNOSES dataframe
    - df_desc_labitems: the D_LABITEMS dataframe
    - df_desc_items: the D_ITEMS dataframe
    """
    # load description tables
    df_desc_icd = pd.read_csv(self.ROOT_DIR / 'data/D_ICD_DIAGNOSES.csv')
    df_desc_labitems = pd.read_csv(self.ROOT_DIR / 'data/D_LABITEMS.csv')
    df_desc_items = pd.read_csv(self.ROOT_DIR / 'data/D_ITEMS.csv')
    return df_desc_icd, df_desc_labitems, df_desc_items

  def load_patients(self):
    """
    Load the PATIENTS table

    Parameters: N/A

    Returns:
    - df_patients: the PATIENTS dataframe
    """
    # load transaction dataset
    df_patients = pd.read_csv(self.ROOT_DIR / 'data/PATIENTS.csv')
    # patients: DOB to date format, we not care about the birth time
    df_patients['DOB'] = pd.to_datetime(df_patients['DOB'], format='%Y-%m-%d %H:%M:%S')
    return df_patients

  def load_admissions(self):
    """
    Load the ADMISSIONS table

    Parameters: N/A

    Returns:
    - df_admissions: the ADMISSIONS dataframe
    """
    df_admissions = pd.read_csv(self.ROOT_DIR / 'data/ADMISSIONS.csv')
    # admissions: ADMITTIME, DISCHTIME, EDREGTIME, EDOUTTIME
    df_admissions['ADMITTIME'] = pd.to_datetime(df_admissions['ADMITTIME'], format='%Y-%m-%d %H:%M:%S')
    df_admissions['DISCHTIME'] = pd.to_datetime(df_admissions['DISCHTIME'], format='%Y-%m-%d %H:%M:%S')
    df_admissions['EDREGTIME'] = pd.to_datetime(df_admissions['EDREGTIME'], format='%Y-%m-%d %H:%M:%S')
    df_admissions['EDOUTTIME'] = pd.to_datetime(df_admissions['EDOUTTIME'], format='%Y-%m-%d %H:%M:%S')
    return df_admissions

  def load_diagnoses_icd(self, df_desc_icd):
    """
    Load the DIAGNOSES_ICD table. A columns IS_SEPSIS is added to identify which icd9 code is sepsis

    Parameters:
    - df_desc_icd: the ICD9 code description dataframe

    Returns:
    - df_diagnoses_icd: the DIAGNOSES_ICD dataframe
    """
    df_diagnoses_icd = pd.read_csv(self.ROOT_DIR / 'data/DIAGNOSES_ICD.csv')# retrieve all sepsis icd code
    sepsis_icd =  df_desc_icd[df_desc_icd.apply(lambda x:'sepsis' in x['SHORT_TITLE'].lower(),axis=1)]['ICD9_CODE'].values
    # add new binary classifier target variable
    # df_diagnoses_icd['IS_SEPSIS'] = df_diagnoses_icd.apply(lambda x: 1 if x['ICD9_CODE'] in sepsis_icd else 0, axis=1)
    df_diagnoses_icd['IS_SEPSIS'] = np.where(df_diagnoses_icd.ICD9_CODE.isin(sepsis_icd), 1, 0)
    return df_diagnoses_icd

  def load_labevents(self, df_demographic):
    """
    Load the LABEVENTS table. The null HADM_ID is cleaned up and a csv file is created as a cleaned labevents

    Parameters:
    - df_demographic: the demographic dataframe

    Returns:
    - df_labevents: the LABEVENTS dataframe
    """
    try:
      df_labevents = pd.read_csv(self.ROOT_DIR / 'data/labevents_cleaned.csv')
    except:
      df_labevents = pd.read_csv(self.ROOT_DIR / 'data/labevents.csv')
      # convert column type: CHARTTIME
      df_labevents = self.__labevents_cleanup_hadm_id(df_demographic, df_labevents)
      # utils.save_csv(df_labevents, self.ROOT_DIR / 'data/labevents_cleaned.csv')
    df_labevents['CHARTTIME'] = pd.to_datetime(df_labevents['CHARTTIME'], format='%Y-%m-%d %H:%M:%S')
    return df_labevents

  def load_microbiologyevents(self):
    """
    Load the MICROBIOLOGYEVENTS table.

    Parameters: N/A

    Returns:
    - df_microbiologyevents: the MICROBIOLOGYEVENTS dataframe
    """
    df_microbiologyevents = pd.read_csv(self.ROOT_DIR / 'data/MICROBIOLOGYEVENTS.csv')
    df_microbiologyevents['CHARTTIME'] = pd.to_datetime(df_microbiologyevents['CHARTTIME'], format='%Y-%m-%d %H:%M:%S')
    return df_microbiologyevents

  def load_demographic(self, df_diagnoses_icd):
    """
    Create the demographic table from patients and admissions tables. Added AGE, IS_SEPSIS columns

    Parameters:
    - df_diagnoses_icd: the diagnoses_icd dataframe

    Returns:
    - df_demographic: the demographic dataframe
    """
    df_admissions = self.load_admissions()
    df_patients = self.load_patients()
    # merge the patients and admission tables to a demographic dataframe
    df_demographic = pd.merge(df_admissions, df_patients[['SUBJECT_ID', 'GENDER', 'DOB', 'EXPIRE_FLAG']], on='SUBJECT_ID')

    # create an age column to each case
    df_demographic['AGE'] = (((df_demographic['ADMITTIME'].dt.date - df_demographic['DOB'].dt.date) // 365) / pd.Timedelta(days=1)).astype('int16')
    print(f"Removed {len(df_demographic[df_demographic.AGE<18])} admissions with AGE < 18")
    df_demographic = df_demographic[df_demographic.AGE >= 18]
    # add column IS_SEPSIS to demographic data indicating which case is diagnosed with sepsis
    diagnosed_sepsis = df_diagnoses_icd[df_diagnoses_icd.IS_SEPSIS==1].drop_duplicates(['SUBJECT_ID', 'HADM_ID'])
    df_demographic = df_demographic.merge(diagnosed_sepsis[['SUBJECT_ID', 'HADM_ID', 'IS_SEPSIS']], on=['SUBJECT_ID', 'HADM_ID'], how='left')
    df_demographic['IS_SEPSIS'].fillna(0, inplace=True)
    df_demographic['IS_SEPSIS'] = df_demographic.IS_SEPSIS.astype(int)

    return df_demographic
  
  def demographic_clean_AGE(self, df_demographic):
    """
    Cleanup AGE column in demographic table. Get all admissions having AGE > 100 and replace by the median age of all admissions. Add column AGE_cat

    Parameters:
    - df_demographic: the demographic dataframe

    Returns:
    - df_demographic: the cleaned demographic dataframe
    """
    median_age = int(df_demographic['AGE'].median())
    df_demographic.loc[df_demographic.AGE>100, 'AGE'] = median_age
    df_demographic = utils.categorise_age(df_demographic)
    return df_demographic


  def __labevents_cleanup_hadm_id(self, df_demographic, df_labevents):
    """
    Cleanup the NULL HADM_ID in the labevents dataset

    Parameters:
    - df_demographic: demographic dataframe
    - df_labevents: labevents dataframe
    
    Returns:
    - df_labevents: the cleaned df_labevents dataframe
    """
    # get all labevent records with HADM_ID null and merge with the demographic table to have the HADM_ID, ADMITTIME, DISCHTIME
    df_empty_hadm_labevents = df_labevents[df_labevents['HADM_ID'].isnull()]
    df_empty_hadm_labevents = df_empty_hadm_labevents.merge(df_demographic[['SUBJECT_ID', 'HADM_ID', 'ADMITTIME', 'DISCHTIME']], on='SUBJECT_ID')

    # only keep records that has ADMITTIME <= CHARTTIME <= DISCHTIME and remove other records
    index = df_empty_hadm_labevents[(df_empty_hadm_labevents['CHARTTIME'] >= df_empty_hadm_labevents['ADMITTIME']) & (df_empty_hadm_labevents['CHARTTIME'] <= df_empty_hadm_labevents['DISCHTIME'])].index
    df_empty_hadm_labevents = df_empty_hadm_labevents[df_empty_hadm_labevents.index.isin(index)]
    # set the HADM_ID of the labevents with HADM_ID of the demographic table
    df_empty_hadm_labevents.HADM_ID_x = df_empty_hadm_labevents.HADM_ID_y

    # Rename HADM_ID_x to HADM_ID and remove HADM_ID_y, ADMITTIME, DISCHTIME columns
    df_empty_hadm_labevents.rename(columns={'HADM_ID_x': 'HADM_ID'}, inplace=True)
    df_empty_hadm_labevents.drop(columns=['HADM_ID_y', 'ADMITTIME', 'DISCHTIME'], inplace=True)

    # concat the updated records with records that originally have HADM_ID
    df_not_empty_hadm = df_labevents[~df_labevents.HADM_ID.isnull()]
    combined_df_hasHADM = pd.concat([df_not_empty_hadm, df_empty_hadm_labevents], ignore_index=True)
    combined_df_hasHADM['HADM_ID'] = combined_df_hasHADM['HADM_ID'].astype(int)
    return combined_df_hasHADM

  def __get_admittime(self, x):
    """
    Compute the admittime of each labevents. Return the ADMITTIME or CHARTTIME whichever is min.

    Parameters:
    - x: the dataframe
    
    Returns:
    - new_admittime: the new admittime
    """
    x.sort_values(['CHARTTIME'], inplace=True)
    min_charttime = x.iloc[0]['CHARTTIME']
    new_admittime = x.iloc[0]['ADMITTIME']
    if min_charttime < new_admittime:
      new_admittime = min_charttime
    return new_admittime

  def labevents_compute_TIME(self, df_labevents, df_demographic):
    """
    Compute the TIME of each labevents by CHARTTIME - ADMITTIME.

    Parameters:
    - df_labevents: the labevents dataframe
    - df_demographic: the demographic dataframe
    
    Returns:
    - df_labevents: the df_labevents dataframe with TIME column
    """
    df_labevents = df_labevents.merge(df_demographic[['SUBJECT_ID', 'HADM_ID', 'ADMITTIME']], on=['SUBJECT_ID', 'HADM_ID'])
    new_admittime = df_labevents.groupby(['SUBJECT_ID', 'HADM_ID']).apply(lambda x: self.__get_admittime(x)).reset_index(name='NEW_ADMITTIME')
    df_labevents = df_labevents.merge(new_admittime, on=['SUBJECT_ID', 'HADM_ID'])

    df_labevents['TIME'] = np.ceil((df_labevents.CHARTTIME - df_labevents.ADMITTIME).dt.total_seconds() / 3600)
    return df_labevents

  def __create_labevents_processed(self, df_labevents, df_demographic, df_desc_labitems, feature_list, hours):
    """
    Get all labevents rows filtered by itemid, t=n. Replace GENDER by GENDER_NUM

    Parameters:
    - df_labevents: the labevents dataframe
    - df_demographic: the demographic dataframe
    - df_desc_labitems: the labitems description dataframe
    
    Returns:
    - potential_cases: the labevents filtered
    """
    # load features from file and get top 10 features
    potential_cases = df_labevents[df_labevents.ITEMID.isin(feature_list)].merge(df_demographic[['SUBJECT_ID', 'HADM_ID', 'AGE', 'GENDER', 'IS_SEPSIS']], on=['SUBJECT_ID', 'HADM_ID'])

    # get only the data at first n hours
    potential_cases = potential_cases[(potential_cases.TIME <= hours)]
    potential_cases = potential_cases.merge(df_desc_labitems[['ITEMID', 'LABEL', 'FLUID']], on=['ITEMID'])

    # One-hot encoding GENDER
    potential_cases['GENDER_NUM'] = potential_cases['GENDER'].replace({'M': 0, 'F': 1})
    potential_cases.drop(columns=["GENDER"], inplace=True)

    return potential_cases

  def create_train_data(self, df_labevents, df_demographic, df_desc_labitems, hours, feature_no = 20):
    """
    Get all labevents rows filtered by itemid, t=n. Replace GENDER by GENDER_NUM

    Parameters:
    - df_labevents: the labevents dataframe
    - df_demographic: the demographic dataframe
    - df_desc_labitems: the labitems description dataframe
    
    Returns:
    - potential_cases: the labevents filtered
    """
    potential_events = pd.read_csv(self.ROOT_DIR / 'data/potential_events.csv')
    feature_list = potential_events.iloc[:feature_no]['ITEMID']

    a = self.__create_labevents_processed(df_labevents, df_demographic, df_desc_labitems, feature_list, hours)
    a.sort_values(['SUBJECT_ID', 'HADM_ID', 'ITEMID', 'CHARTTIME'], ascending = False, inplace=True)

    df_final = a.drop_duplicates(subset=['SUBJECT_ID', 'HADM_ID', 'ITEMID'], ignore_index=True)[['SUBJECT_ID', 'HADM_ID', 'AGE', 'GENDER_NUM', 'IS_SEPSIS', 'ITEMID']]

    a = a.dropna(subset=['VALUENUM'], axis=0)
    a = a.drop_duplicates(['SUBJECT_ID', 'HADM_ID', 'ITEMID'])
    df_final = df_final.merge(a[['SUBJECT_ID', 'HADM_ID', 'ITEMID', 'VALUENUM']], on=['SUBJECT_ID', 'HADM_ID', 'ITEMID'], how='left')
    df_final = df_final.pivot_table(values='VALUENUM', index=['SUBJECT_ID', 'HADM_ID', 'AGE', 'GENDER_NUM', 'IS_SEPSIS'], columns='ITEMID', aggfunc='first').reset_index()

    df_final = df_final.fillna(-999)

    utils.save_csv(df_final, self.ROOT_DIR / f'data/output_csv/t{hours}.csv')