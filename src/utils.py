from pathlib import Path
import pandas as pd

def get_project_root() -> Path:
    return Path(__file__).absolute().parent.parent

def save_csv(df, filename):
    filepath = Path(filename)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath, index=False)
    
        
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
    
    # define bin labels
    age_bin_labels = ['0', '1-17', '18-35', '36-50', '51-70', '71+']
    
    # create age bins
    df['AGE_cat'] = pd.cut(df['AGE'], bins=age_bin_edges, labels=age_bin_labels, right=False)
    
    return df

def get_sepsis_codes(df_desc_icd):
    """
    Get ICD-9 codes relating to sepsis
    
    Parameters:
    
    Returns:
    
    """
    
    icd_sepsis = df_desc_icd[df_desc_icd.apply(lambda x:'sepsis' in x['SHORT_TITLE'].lower(),axis=1)]['ICD9_CODE'].values
    
    return icd_sepsis

def get_sepsis_admissions(icd_sepsis, df):
    """

    Args:
        icd_sepsis (list): List of ICD-9 codes relating to sepsis.
        df (DataFrame): DataFrame containing column ICD9_CODE.
    
    Returns:
        df_sepsis_admissions (DataFrame): DataFrame containing sepsis admissions.
    """

    df_sepsis_admissions = df[df.apply(lambda x:x['ICD9_CODE'] in icd_sepsis, axis=1)]
    
    return df_sepsis_admissions
    