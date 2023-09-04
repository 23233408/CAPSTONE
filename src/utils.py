from pathlib import Path

def get_project_root() -> Path:
    return Path(__file__).absolute().parent.parent


#function to save df to csv file
def save_csv(df, filename):
    filepath = Path(filename)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath, index=False)