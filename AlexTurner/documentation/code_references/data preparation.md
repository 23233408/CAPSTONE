

https://github.com/point85AI/Policy-Iteration-AI-Clinician 
### Data preparation for prescriptions table (4/6)

- Filter conditions:
- unit: 'mg'
- antibiotics medicines: ('Vancomycin','Meropenem','Levofloxacin')
- Contruct a normalized dose column
- Convert data type to datetime and extract only year value

```python
presc['dose_val_rx'] = pd.to_numeric(presc['dose_val_rx'], errors = 'coerce')
presc = presc[presc['dose_unit_rx']=='mg']
presc = presc[presc['drug'].isin(['Vancomycin','Meropenem','Levofloxacin'])]

temp_df = pd.DataFrame()
for item in presc.drug.unique():
    temp = presc[presc['drug'].str.contains(item)]
    temp['norm_size'] = temp['dose_val_rx'] / temp['dose_val_rx'].max()
    temp_df = temp_df.append(temp)
presc = pd.merge(presc, temp_df, on=list(presc.columns))

presc['startdate'] = pd.to_datetime(presc['startdate'], errors = 'coerce')
presc.sort_values(by='startdate', inplace=True)
presc.set_index('startdate', inplace = True)
presc.head(1)
```