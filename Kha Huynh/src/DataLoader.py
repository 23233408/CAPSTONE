import pandas as pd
import numpy as np, warnings
from pathlib import Path
import os
from importlib import reload

import utils as utils
reload(utils)

import engineer_features as ef
reload(ef)

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
      df_labevents = pd.read_csv(self.ROOT_DIR / 'data/LABEVENTS.csv')
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
    df_microbiologyevents['AB_ITEMID'] = pd.to_numeric(df_microbiologyevents['AB_ITEMID'], errors='coerce').fillna(pd.NA).astype('Int64')
    # df_microbiologyevents['AB_ITEMID'] = df_microbiologyevents.AB_ITEMID.astype(int)
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
    df_labevents = df_labevents.merge(df_demographic[['SUBJECT_ID', 'HADM_ID', 'ADMITTIME', 'DISCHTIME', 'DEATHTIME']], on=['SUBJECT_ID', 'HADM_ID'])
    df_labevents.sort_values(['SUBJECT_ID', 'HADM_ID', 'CHARTTIME'], inplace=True)
    new_admittime = df_labevents.drop_duplicates(['SUBJECT_ID', 'HADM_ID'])
    new_admittime['NEW_ADMITTIME'] = np.where(new_admittime.CHARTTIME < new_admittime.ADMITTIME, new_admittime.CHARTTIME, new_admittime.ADMITTIME)
    # new_admittime = df_labevents.groupby(['SUBJECT_ID', 'HADM_ID']).apply(lambda x: self.__get_admittime(x)).reset_index(name='NEW_ADMITTIME')
    df_labevents = df_labevents.merge(new_admittime[['SUBJECT_ID', 'HADM_ID', 'NEW_ADMITTIME']], on=['SUBJECT_ID', 'HADM_ID'])

    df_labevents['TIME'] = np.ceil((df_labevents.CHARTTIME - df_labevents.NEW_ADMITTIME).dt.total_seconds() / 3600)
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
    # load features from file and get top n features
    potential_cases = df_labevents[df_labevents.ITEMID.isin(feature_list)].merge(df_demographic[['SUBJECT_ID', 'HADM_ID', 'AGE', 'GENDER', 'IS_SEPSIS']], on=['SUBJECT_ID', 'HADM_ID'])

    # get only the data at first n hours
    potential_cases = potential_cases[(potential_cases.TIME <= hours)]
    potential_cases = potential_cases.merge(df_desc_labitems[['ITEMID', 'LABEL', 'FLUID']], on=['ITEMID'])

    # One-hot encoding GENDER
    potential_cases['GENDER_NUM'] = potential_cases['GENDER'].replace({'M': 0, 'F': 1})
    potential_cases.drop(columns=["GENDER"], inplace=True)

    return potential_cases

  def create_train_data(self, df_labevents, df_demographic, df_desc_labitems, hours, feature_no = -1, output_filename=''):
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
    # read the features list in the potential csv file and get top n features
    potential_events = pd.read_csv(self.ROOT_DIR / 'data/potential_events.csv')
    potential_events.sort_values(['abnormal_count'], ascending=False, inplace=True)
    if feature_no == -1:
      # get all features
      feature_list = potential_events['ITEMID']
    else:
      feature_list = potential_events.iloc[:feature_no]['ITEMID']
    
    # get the df_labevents filtered by hours and features
    a = self.__create_labevents_processed(df_labevents, df_demographic, df_desc_labitems, feature_list, hours)
    a.sort_values(['SUBJECT_ID', 'HADM_ID', 'ITEMID', 'CHARTTIME'], ascending = False, inplace=True)
    # get unique rows by SUBJECT_ID, HADM_ID, ITEMID
    df_final = a.drop_duplicates(subset=['SUBJECT_ID', 'HADM_ID', 'ITEMID'], ignore_index=True)[['SUBJECT_ID', 'HADM_ID', 'AGE', 'GENDER_NUM', 'IS_SEPSIS', 'ITEMID']]

    # drop all rows having null in VALUENUM and keep only the firt duplicate rows
    a = a.dropna(subset=['VALUENUM'], axis=0)
    a = a.drop_duplicates(['SUBJECT_ID', 'HADM_ID', 'ITEMID'])
    # merge the result back to the unique rows by SUBJECT_ID, HADM_ID, ITEMID and unpivot the table
    df_final = df_final.merge(a[['SUBJECT_ID', 'HADM_ID', 'ITEMID', 'VALUENUM']], on=['SUBJECT_ID', 'HADM_ID', 'ITEMID'], how='left')
    # df_final.fillna(-999, inplace=True)
    df_final = df_final.pivot_table(values='VALUENUM', index=['SUBJECT_ID', 'HADM_ID', 'AGE', 'GENDER_NUM', 'IS_SEPSIS'], columns='ITEMID', aggfunc='first')
    # rename the features column names
    df_final.columns = ["ITEMID_" + str(i) for i in df_final.columns]
    df_final = df_final.reset_index()

    # fill all null VALUENUM by -999 and save to csv file
    df_final = df_final.fillna(-999)

    # # compute SOFA score
    # df_final['SOFA'] = ef.get_sofa_score(df=df_final)

    try:
      utils.save_csv(df_final, output_filename)
    except:
      utils.save_csv(df_final, self.ROOT_DIR / f'data/Model input data/t{hours}.csv')

    # return df_final

  def create_train_data_sequence_t(self, df_labevents, df_demographic, df_desc_labitems, hours, feature_no = -1, output_filename=''):
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
    # read the features list in the potential csv file and get top n features
    potential_events = pd.read_csv(self.ROOT_DIR / 'data/potential_events.csv')
    potential_events.sort_values(['abnormal_count'], ascending=False, inplace=True)
    if feature_no == -1:
      # get all features
      feature_list = potential_events['ITEMID']
    else:
      feature_list = potential_events.iloc[:feature_no]['ITEMID']
    
    # get the df_labevents filtered by hours and features
    a = self.__create_labevents_processed(df_labevents, df_demographic, df_desc_labitems, feature_list, hours)
    a.sort_values(['SUBJECT_ID', 'HADM_ID', 'ITEMID', 'CHARTTIME'], inplace=True)

    # split dataframe to 3 dfs, admissions with 4, <4, >4 rows
    temp = a.groupby(['SUBJECT_ID', 'HADM_ID', 'ITEMID'])['CHARTTIME'].count().reset_index(name='count')
    temp.count = temp['count'].astype(int)
    row4_df = a.merge(temp[temp.count == hours][['SUBJECT_ID', 'HADM_ID', 'ITEMID']], on=['SUBJECT_ID', 'HADM_ID', 'ITEMID'])
    rowG4_df = a.merge(temp[temp.count > hours][['SUBJECT_ID', 'HADM_ID', 'ITEMID']], on=['SUBJECT_ID', 'HADM_ID', 'ITEMID'])
    rowL4_df = a.merge(temp[temp.count < hours][['SUBJECT_ID', 'HADM_ID', 'ITEMID']], on=['SUBJECT_ID', 'HADM_ID', 'ITEMID'])

    # for admission >4 rows, only get 4 latest rows by CHARTTIME
    rowG4_df = rowG4_df.groupby(['SUBJECT_ID', 'HADM_ID', 'ITEMID']).tail(hours)

    # for admission <4 rows, duplicate the first row and replace the value by mean in that admission/ITEMID
    rowL4_mean = rowL4_df.groupby(['SUBJECT_ID', 'HADM_ID', 'ITEMID'])['VALUENUM'].mean().reset_index(name='avg')
    rowL4_mean.avg = rowL4_mean.avg.astype(float)
    rowL4_mean = pd.DataFrame(np.repeat(rowL4_mean.values, hours-1, axis=0), columns=rowL4_mean.columns)
    
    first_row_df = rowL4_df.drop_duplicates(['SUBJECT_ID', 'HADM_ID', 'ITEMID'])
    replicate_first_row = pd.DataFrame(np.repeat(first_row_df.values, hours-1, axis=0), columns=first_row_df.columns)
    replicate_first_row.VALUENUM = rowL4_mean.avg

    rowL4_df = pd.concat([rowL4_df, replicate_first_row], ignore_index=True)
    rowL4_df.sort_values(['SUBJECT_ID', 'HADM_ID', 'ITEMID', 'CHARTTIME'], inplace=True)
    rowL4_df = rowL4_df.groupby(['SUBJECT_ID', 'HADM_ID', 'ITEMID']).tail(hours)

    # union 3 dfs
    df_final = pd.concat([row4_df, rowG4_df], ignore_index=True)
    df_final = pd.concat([df_final, rowL4_df], ignore_index=True)
    df_final.VALUENUM.fillna(-999, inplace=True)
    df_final['level'] = df_final.groupby(['SUBJECT_ID', 'HADM_ID', 'ITEMID']).cumcount()

    result = df_final.pivot_table(values='VALUENUM', index=['SUBJECT_ID', 'HADM_ID', 'AGE', 'GENDER_NUM', 'IS_SEPSIS', 'level'], columns='ITEMID', aggfunc='first')
    result.columns = ["ITEMID_" + str(i) for i in result.columns]
    result = result.reset_index()
    result = result.fillna(-999)
    result.drop(['level'], axis=1, inplace=True)
    try:
      utils.save_csv(result, output_filename)
    except:
      utils.save_csv(result, self.ROOT_DIR / f'data/Model input data/t{hours}_sequence.csv')

    return result
  
  def create_train_data_sequence(self, df_labevents, df_demographic, df_desc_labitems, hours, feature_no = -1, output_filename=''):
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
    # read the features list in the potential csv file and get top n features
    potential_events = pd.read_csv(self.ROOT_DIR / 'data/potential_events.csv')
    potential_events.sort_values(['abnormal_count'], ascending=False, inplace=True)
    if feature_no == -1:
      # get all features
      feature_list = potential_events['ITEMID']
    else:
      feature_list = potential_events.iloc[:feature_no]['ITEMID']
    
    # get the df_labevents filtered by hours and features
    a = self.__create_labevents_processed(df_labevents, df_demographic, df_desc_labitems, feature_list, hours)
    a.sort_values(['SUBJECT_ID', 'HADM_ID', 'ITEMID', 'CHARTTIME'], inplace=True)

    row_mean = a.groupby(['SUBJECT_ID', 'HADM_ID', 'ITEMID'])['VALUENUM'].mean().reset_index(name='avg')
    row_mean.avg = row_mean.avg.astype(float)
    
    df_final = a.merge(row_mean, on=['SUBJECT_ID', 'HADM_ID', 'ITEMID'])
    df_final.VALUENUM = np.where(df_final.VALUENUM.isnull(),df_final.avg, df_final.VALUENUM)
    
    df_final['level'] = df_final.groupby(['SUBJECT_ID', 'HADM_ID', 'ITEMID']).cumcount()
    df_final.VALUENUM.fillna(-999, inplace=True)

    result = df_final.pivot_table(values='VALUENUM', index=['SUBJECT_ID', 'HADM_ID', 'AGE', 'GENDER_NUM', 'IS_SEPSIS', 'level'], columns='ITEMID', aggfunc='first')
    result.columns = ["ITEMID_" + str(i) for i in result.columns]
    result = result.reset_index()
    result = result.fillna(-999)
    result.drop(['level'], axis=1, inplace=True)

    try:
      utils.save_csv(result, output_filename)
    except:
      utils.save_csv(result, self.ROOT_DIR / f'data/Model input data/t{hours}_sequence.csv')

    return result
  
  def create_train_data_sequence_new(self, df_labevents, df_demographic, df_desc_labitems, hours, feature_no = -1, output_filename=''):
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
    # # read the features list in the potential csv file and get top n features
    # potential_events = pd.read_csv(self.ROOT_DIR / 'data/potential_events.csv')
    # potential_events.sort_values(['abnormal_count'], ascending=False, inplace=True)
    # if feature_no == -1:
    #   # get all features
    #   feature_list = potential_events['ITEMID']
    # else:
    #   feature_list = potential_events.iloc[:feature_no]['ITEMID']
    
    # read the features list in the potential csv file and get top n features
    feature_list = self.__read_features(self.ROOT_DIR / 'data/potential_events.csv', feature_no)
    
    # get the df_labevents filtered by hours and features
    a = self.__create_labevents_processed(df_labevents, df_demographic, df_desc_labitems, feature_list, hours)
    a.sort_values(['SUBJECT_ID', 'HADM_ID', 'ITEMID', 'CHARTTIME'], inplace=True)
    
    a['VALUENUM'].replace(np.nan, -999, inplace=True)
    result = a.pivot_table(values='VALUENUM', index=['SUBJECT_ID', 'HADM_ID', 'AGE', 'GENDER_NUM', 'IS_SEPSIS', 'CHARTTIME'], columns='ITEMID', aggfunc='first')
    result.columns = ["ITEMID_" + str(i) for i in result.columns]
    result = result.reset_index()
    # result.replace(-999, np.nan, inplace=True)

    # item_cols = result.columns[result.columns.str.startswith('ITEMID_')]
    # mean_by_item = result.groupby(['SUBJECT_ID', 'HADM_ID'])[item_cols].mean().reset_index()
    # result = result.merge(mean_by_item, on=['SUBJECT_ID', 'HADM_ID'])

    # new_col = {f'{x}_x':x for x in item_cols}
    # remove_col = [f'{x}_y' for x in item_cols]
    # for itemx, itemy in zip(new_col, remove_col):
    #   result[itemx] = np.where(result[itemx].isna(), result[itemy], result[itemx])

    # result = result.rename(columns=new_col)
    # result.drop(remove_col, axis=1, inplace=True)
    # compute SOFA score
    result['SOFA'] = ef.get_sofa_score(df=result)

    try:
      utils.save_csv(result, output_filename)
    except:
      utils.save_csv(result, self.ROOT_DIR / f'data/Model input data/t{hours}_sequence.csv')

    return result

  def __read_features(self, feature_filename, feature_no=-1):
    """
    Read features from file and get top n features.

    Parameters:
    - feature_filename: the feature file path
    - feature_no: the top n features to select

    Returns:
    - The numpy array of features
    """
    try:
      potential_events = pd.read_csv(feature_filename)
      if feature_no == -1:
        # get all features
        feature_list = potential_events['ITEMID']
      else:
        feature_list = potential_events.iloc[:feature_no]['ITEMID']
      # Parameters for computing SOFA score:
      #     Platelet_count [51265]
      #     Bilirubin_total [50885]
      #     Creatinine [50912]
      SOFA_features = np.array([51265, 50885, 50912])
      result = np.concatenate((feature_list, np.setdiff1d(SOFA_features, feature_list)))
    except Exception as e:
      raise
    return result

  def create_train_data_sequence_padded(self, df_labevents, df_demographic, df_desc_labitems, hours, feature_no = -1, output_filename=''):
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
    # # read the features list in the potential csv file and get top n features
    # potential_events = pd.read_csv(self.ROOT_DIR / 'data/potential_events.csv')
    # potential_events.sort_values(['abnormal_count'], ascending=False, inplace=True)
    # if feature_no == -1:
    #   # get all features
    #   feature_list = potential_events['ITEMID']
    # else:
    #   feature_list = potential_events.iloc[:feature_no]['ITEMID']
    
    # read the features list in the potential csv file and get top n features
    feature_list = self.__read_features(self.ROOT_DIR / 'data/potential_events.csv', feature_no)

    # get the df_labevents filtered by hours and features
    a = self.__create_labevents_processed(df_labevents, df_demographic, df_desc_labitems, feature_list, hours)
    a.sort_values(['SUBJECT_ID', 'HADM_ID', 'ITEMID', 'CHARTTIME'], inplace=True)

    df_final = a
    df_final.VALUENUM.fillna(-999, inplace=True)
    result = df_final.pivot_table(values='VALUENUM', index=['SUBJECT_ID', 'HADM_ID', 'AGE', 'GENDER_NUM', 'IS_SEPSIS', 'CHARTTIME'], columns='ITEMID', aggfunc='first')
    result.columns = ["ITEMID_" + str(i) for i in result.columns]
    result = result.reset_index()
    result.replace(-999, np.nan, inplace=True)
    
    max_rows = result.groupby(['HADM_ID']).size().max()
    row_max_df = result[result.groupby(['SUBJECT_ID', 'HADM_ID']).transform('size') == max_rows]
    row_less_df = result[~result.HADM_ID.isin(row_max_df.HADM_ID)]

    first_row_df = row_less_df.drop_duplicates(['SUBJECT_ID', 'HADM_ID'])[['HADM_ID','IS_SEPSIS','SUBJECT_ID', 'AGE', 'GENDER_NUM']]
    replicate_first_row = pd.DataFrame(np.repeat(first_row_df.values, max_rows-1, axis=0), columns=first_row_df.columns)
    # Find columns with the prefix "ITEM_"
    item_cols = list(set(row_less_df.columns)-set(['HADM_ID','IS_SEPSIS','SUBJECT_ID', 'AGE', 'GENDER_NUM']))
    for col in item_cols:
      replicate_first_row[col] = np.nan

    row_less_df = pd.concat([replicate_first_row, row_less_df])
    # row_less_df.sort_values(['SUBJECT_ID', 'HADM_ID', 'CHARTTIME'], inplace=True)
    row_less_df = row_less_df.groupby(['SUBJECT_ID', 'HADM_ID']).tail(max_rows)
    
    result = pd.concat([row_max_df, row_less_df], ignore_index=True)
    try:
      utils.save_csv(result, output_filename)
    except:
      utils.save_csv(result, self.ROOT_DIR / f'data/Model input data/t{hours}_sequence.csv')

    return result
  
  def extract_train_data_by_features(self, df_labevents, df_demographic, df_desc_labitems, hours, feature_filename='', feature_no = -1, output_filename=''):
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
    # read the features list in the potential csv file and get top n features
    feature_list = self.__read_features(feature_filename, feature_no)

    # get the df_labevents filtered by hours and features
    a = self.__create_labevents_processed(df_labevents, df_demographic, df_desc_labitems, feature_list, hours)
    a.sort_values(['SUBJECT_ID', 'HADM_ID', 'ITEMID', 'CHARTTIME'], ascending = False, inplace=True)
    # get unique rows by SUBJECT_ID, HADM_ID, ITEMID
    df_final = a.drop_duplicates(subset=['SUBJECT_ID', 'HADM_ID', 'ITEMID'], ignore_index=True)[['SUBJECT_ID', 'HADM_ID', 'AGE', 'GENDER_NUM', 'IS_SEPSIS', 'ITEMID']]

    # drop all rows having null in VALUENUM and keep only the firt duplicate rows
    a = a.dropna(subset=['VALUENUM'], axis=0)
    a = a.drop_duplicates(['SUBJECT_ID', 'HADM_ID', 'ITEMID'])
    # merge the result back to the unique rows by SUBJECT_ID, HADM_ID, ITEMID and unpivot the table
    df_final = df_final.merge(a[['SUBJECT_ID', 'HADM_ID', 'ITEMID', 'VALUENUM']], on=['SUBJECT_ID', 'HADM_ID', 'ITEMID'], how='left')
    df_final = df_final.pivot_table(values='VALUENUM', index=['SUBJECT_ID', 'HADM_ID', 'AGE', 'GENDER_NUM', 'IS_SEPSIS'], columns='ITEMID', aggfunc='first')
    # rename the features column names
    df_final.columns = ["ITEMID_" + str(i) for i in df_final.columns]
    df_final = df_final.reset_index()

    # fill all null VALUENUM by -999 and save to csv file
    df_final = df_final.fillna(-999)

    # compute SOFA score
    df_final['SOFA'] = ef.get_sofa_score(df=df_final)

    try:
      utils.save_csv(df_final, output_filename)
    except:
      utils.save_csv(df_final, self.ROOT_DIR / f'data/Model input data/t{hours}.csv')

    return df_final
  
  def convert_itemid_to_title(self, itemid_array, df_desc_labitems):
    """
    Convert ITEMID_xxxx to itemid's Label.

    Parameters:
    - itemid_array: the array of ITEMIDs to convert
    - df_desc_labitems: the labitems description dataframe

    Returns:
    - A dictionary of {ITEMID_xxxx: LABEL}
    """
    plot_feats = {x: f'{df_desc_labitems[df_desc_labitems.ITEMID == int(x[7:])].LABEL.values[0]} ({x[7:]})' for x in itemid_array}
    return plot_feats