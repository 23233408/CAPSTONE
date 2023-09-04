from pathlib import Path
import pandas as pd

def get_project_root() -> Path:
    return Path(__file__).absolute().parent.parent


#function to save df to csv file
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
    
    # define bin labels: neonatal, child, adult, middle-age, elderly, very old
    age_bin_labels = ['0', '1-17', '18-35', '36-50', '51-70', '71+']
    
    # create age bins
    df_demographic['AGE_cat'] = pd.cut(df_demographic['AGE'], bins=age_bin_edges, labels=age_bin_labels, right=False)
    
    return df