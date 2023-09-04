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
