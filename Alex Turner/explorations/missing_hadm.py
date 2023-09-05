# filter missing data
missing_hadm_df = df_labevents[df_labevents['HADM_ID'].isnull()]

# join tables for existing HADM_IDs
joined_df = pd.merge(df_labevents[df_labevents['HADM_ID'].notnull()], df_admission, on=['SUBJECT_ID', 'HADM_ID'], how='left')

# find rows with missing HADM_ID
def find_hadm_id(row):
    possible_admissions = df_admission[df_admission['SUBJECT_ID'] == row['SUBJECT_ID']]
    for _, admission_row in possible_admissions.iterrows():
        if admission_row['ADMITTIME'] <= row['CHARTTIME'] <= admission_row['DISCHTIME']:
            return admission_row['HADM_ID']
    return None

missing_hadm_df['HADM_ID'] = missing_hadm_df.apply(find_hadm_id, axis=1)

# combine the dataframes
final_df = pd.concat([joined_df, missing_hadm_df], ignore_index=True)

print(final_df)