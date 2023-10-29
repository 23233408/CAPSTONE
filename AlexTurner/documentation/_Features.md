## Feature engineering and included features of each study:

|Study|Number of initial features|Number of final features|Including features|
|---|---|---|---|
|[Delahanty et al. (2019)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8741489/#bib10)|217|13|Lactic acid (max), Shock index age (last), WBC count(max), Lactic acid(change), Neutrophils(max), Glucose(max), Blood urea nitrogen(max), Shock index age (first), Respiratory rate (max), Albumin (last), Systolic blood pressure (min), Serum creatinine (max), Temperature (max)|
|[Barton et al. (2019)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8741489/#bib2)|6|6|SpO2, heart rate, respiratory rate, temperature, systolic blood pressure, diastolic blood pressure|
|Taylro, 2015|566|20|Oxygen saturation, Respiratory rate, Blood pressure, BUN, Albumin, Intubation, Procedures (in ED), Need for vasopressors, Age, RN resp care, RDW, Potassium, AST, Heart rate, Acuity level(triage), ED impression (Dx), CO2 (Lab), ECG performed, Beta-blocker (Home Med), Cardiac dysrhythmia (PMHx)|
|[Kam and Kim (2017)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8741489/#bib19)|9|9|systolic pressure, pulse pressure, heart rate, body temperature, respiratory rate, WBC count, pH, blood oxygen saturation,age|
|[Mao et al. (2018)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8741489/#bib28)|6|6|systolic blood pressure, diastolic blood pressure, heart rate, respiratory rate, temperature, peripheral capillary oxygen saturation|
|[Taneja et al. (2017)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8741489/#bib42)|31|NR|TNF-α, IL-1β, GCSF, IL-6, PCT, sTREM1, IL18, MMP9, TNFR1, TNFR2, IP10, MCP1, IL-1ra, NA, CD64, WBC, Lactic Acid, Systolic Blood Pressure, Diastolic Blood Pressure, Pulse, Temperature, Respirations, PCO2, Age, Gender, Bilirubin, Glasgow Coma Scale, Creatinine, Platelet, SOFA score, qSOFA score|
|[Saqib et al. (2018)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8741489/#bib38)|47|34|White blood cell count, Heart rate, Diastolic blood pressure, Systolic blood pressure, Mean blood pressure, Weight, Anion gap, Bicarbonate, Oxygen saturation, Height, Temperature, pH|
|[Bloch et al. (2019)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8741489/#bib5)|20|4|the number of trend changes in respiratory rate and arterial pressure, the minimal change in respiratory rate, and the median change in heart rate|
|[Kwon and Baek (2020)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8741489/#bib23)|14|NR|Age, sex, diagnoses at the ED, systolic blood pressure, respiration rate, mental status, body temperature, heart rate, arterial partial pressure of carbon dioxide, white blood cell count, duration of hospitalization, ICU admission, mechanical ventilation, mortality.|
|[Nemati et al.(2018)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8741489/#bib34)|65|65|RRSTD, MAPSTD, HRV1, BPV1, HRV2, BPV2, MAP, HR, O2Sat, SBP, DBP, RESP, Temp, GCS, PaO2, FIO2, WBC, Hemoglobin, Hematocrit, Creatinine, Bilirubin and Bilirubin direct, Platelets, INR, PTT, AST, Alkaline Phosphatase, Lactate, Glucose, Potassium, Calcium, BUN, Phosphorus, Magnesium, Chloride, B-type BNP, Troponin, Fibrinogen, CRP, Sedimentation Rate, Ammonia, pH, pCO2, HCO3, Base Excess, SaO2, Care Unit (Surgical, Cardiac Care, or Neuro intensive care), Surgery in the past 12 h, Wound Class (clean, contaminated, dirty, or infected), Surgical Specialty (Cardiovascular, Neuro, Ortho-Spine, Oncology, Urology, etc.), Number of antibiotics in the past 12, 24, and 48 h, Age, CCI, Mechanical Ventilation, maximum change in SOFA score over the past 6 h.|
|[Hou et al. (2020)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8741489/#bib16)|22|11|urine output, lactate, Bun, sysbp, INR, age, cancer, SpO2, sodium, AG, creatinine|


## Table of Abbreviations:

| Term   | Definition                                            |
|--------|-------------------------------------------------------|
| WBC    | White Blood Cell Count                                |
| BUN    | Blood Urea Nitrogen                                   |
| RDW    | Red Blood Cell Distribution Width                     |
| AST    | Aspartate Transaminase                                |
| ED     | Emergency Department                                  |
| ECG    | Electrocardiogram                                     |
| SOFA   | Sequential Organ Failure Assessment                   |
| qSOFA  | Quick Sequential Organ Failure Assessment             |
| RRSTD  | Standard Deviation of Respiratory Rate Intervals      |
| MAPSTD | Standard Deviation of Mean Arterial Pressure          |
| HRV1   | Average Multiscale Entropy of Respiratory Rate        |
| BPV1   | Average Multiscale Entropy of Mean Arterial Pressure  |
| HRV2   | Average Multiscale Conditional Entropy of Respiratory Rate |
| MAP    | Mean Arterial Blood Pressure                          |
| HR     | Heart Rate                                            |
| O2Sat  | Oxygen Saturation                                     |
| SBP    | Systolic Blood Pressure                               |
| DBP    | Diastolic Blood Pressure                              |
| RESP   | Respiratory Rate                                      |
| Temp   | Temperature                                           |
| GCS    | Glasgow Coma Scale                                    |
| PaO2   | Partial Pressure of Arterial Oxygen                   |
| FIO2   | Fraction of Inspired O2                               |
| INR    | International Normalized Ratio                        |
| PTT    | Partial Prothrombin Time                              |
| BNP    | B-type Natriuretic Peptide                            |
| CCI    | Charleston Comorbidity Index                          |
| sysbp  | Systolic Blood Pressure                               |
| AG     | Anion Gap                                             |

