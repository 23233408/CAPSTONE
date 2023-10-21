import pandas as pd
import numpy as np, warnings
from pathlib import Path
import os

def save_csv(df, filename):
    filepath = Path(filename)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath, index=False)

# check the admission diagnoses to find whether it is diagnosed sepsis
def check_sepsis(subject_id, hadm_id, df_diagnoses_icd):
    admission_diagnoses = df_diagnoses_icd[(df_diagnoses_icd['SUBJECT_ID'] == subject_id) & (df_diagnoses_icd['HADM_ID'] == hadm_id)]
    is_sepsis = 1 if sum(admission_diagnoses['IS_SEPSIS']) > 0 else 0
    return is_sepsis

def create_labevent_columns(df, item_ids):
    columns = item_ids
    flag_columns = np.array([f"{item}_FLAG" for item in item_ids])
    columns= np.append(columns, flag_columns)
    df = pd.concat([df, pd.DataFrame(np.nan, columns=columns, index=df.index)], axis=1)
    return df

def categorise_age(df):
    """
    Categorise the 'AGE' column in the DataFrame into age bins.
    
    Parameters:
    - df: DataFrame containing the 'AGE' column
    
    Returns:
    - DataFrame with an additional 'AGE_cat' column containing the age categories
    """

    # define age bin edges
    age_bin_edges = [0, 1, 18, 36, 51, 71, 121]
    
    # define bin labels: neonatal, child, adult, middle-age, elderly, very old
    age_bin_labels = ['0', '1-17', '18-35', '36-50', '51-70', '71+']
    
    # create age bins
    df['AGE_cat'] = pd.cut(df['AGE'], bins=age_bin_edges, labels=age_bin_labels, right=False)
    df['AGE_NUM'] = pd.factorize(df['AGE_cat'], sort=True)[0]
    
    return df


