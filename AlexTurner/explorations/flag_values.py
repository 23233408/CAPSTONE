# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3307229/

# proportion of flag labels in lab events
df_labevents['FLAG'].value_counts() / df_labevents.shape[0]


# Abnormal flags are recorded when comparing lab values against threshold ranges. The threshold ranges are not static, may vary based on reagents, and unfortunately are not known to us at present.

# get mean value of delta events
df_labevents[df_labevents.apply(lambda x:'delta' in x['FLAG'],axis=1)]