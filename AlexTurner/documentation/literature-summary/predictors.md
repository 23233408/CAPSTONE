
# bacteria / organisms

Staph aureus 
E coli 


## common symptoms
1. **Fever or Hypothermia**: Body temperature above 101ºF (38ºC) or below 96.8ºF (36ºC)
2. **Tachycardia**: Rapid heart rate (above 90 beats per minute)
3. **Tachypnea**: Rapid breathing rate (above 20 breaths per minute)
4. **Confusion or Altered Mental Status**: Disorientation, confusion, or reduced alertness
5. **Extreme Fatigue**: Feeling extremely tired or weak

### Gastrointestinal Symptoms:

1. **Nausea and Vomiting**: Feeling sick to the stomach or throwing up
2. **Diarrhea**: Loose or watery stools

### Skin Symptoms:

1. **Pale or Mottled Skin**: Skin may appear pale, discolored, or blotchy
2. **Cold Extremities**: Cold hands and feet despite fever

### Cardiovascular Symptoms:

1. **Low Blood Pressure**: Systolic blood pressure lower than 100 mm Hg
2. **Poor Peripheral Perfusion**: Reduced blood flow to extremities, leading to cold and pale limbs

### Respiratory Symptoms:

1. **Shortness of Breath**: Difficulty breathing or rapid, shallow breathing
2. **Hypoxia**: Low oxygen levels in the blood

### Other Symptoms:

1. **High Blood Sugar**: Blood sugar levels may be elevated, even in people without diabetes
2. **Oliguria or Anuria**: Reduced or absent urine output
3. **Multiple Organ Dysfunction**: Failure of one or more organ systems

### Sepsis Criteria: SIRSSIRS Criteria and qSOFAqSOFA Score

1. **SIRS Criteria**: Two or more of the following—fever or hypothermia, tachycardia, tachypnea, high or low white blood cell count
2. **qSOFA Score**: Altered mental status, systolic blood pressure ≤ 100 mm Hg, and respiratory rate ≥ 22/min




Biomarkers
### Inflammatory Markers:

1. **C-Reactive Protein (CRP)**: A non-specific marker of inflammation that increases rapidly in response to infection.
    
2. **Procalcitonin (PCT)**: More specific to bacterial infections and sepsis than CRP, it is used to guide antibiotic therapy.
    
3. **Interleukin-6 (IL-6)**: A cytokine that plays a role in inflammation and increases rapidly during sepsis.
### Coagulation Markers:

1. **D-dimer**: A fibrin degradation product, elevated levels suggest abnormal blood clotting.
    
2. **Thrombocytopenia**: Low platelet count can be an early sign of disseminated intravascular coagulation (DIC), a complication of sepsis.
    

### Organ Dysfunction Markers:

1. **Lactate**: Elevated levels indicate tissue hypoxia and are a marker of severity in sepsis.
    
2. **Creatinine**: Elevated levels can indicate kidney dysfunction.
    
3. **Alanine aminotransferase (ALT) and Aspartate aminotransferase (AST)**: Elevated levels can indicate liver dysfunction.
    

### Other Biomarkers:

1. **Soluble urokinase-type plasminogen activator receptor (suPAR)**: An emerging biomarker for assessing the severity and prognosis of sepsis.
    
2. **Endothelial Markers**: Such as soluble E-selectin, are under investigation for their potential role in diagnosing sepsis.
    
3. **Neutrophil Gelatinase-Associated Lipocalin (NGAL)**: Mainly used as a marker of kidney injury, but may also be elevated in sepsis.




## SOFA SCORE
1. **Respiration**: Measured using the PaO2/FiO2 ratio
2. **Coagulation**: Measured using the platelet count
3. **Liver**: Measured using the bilirubin level
4. **Cardiovascular**: Measured using the mean arterial pressure (MAP) or the use of vasopressors
5. **CNS (Central Nervous System)**: Measured using the Glasgow Coma Scale (GCS)
6. **Renal**: Measured using creatinine level or urine output

### 1. Respiration

- **PaO2/FiO2 Ratio**: Can be found in the laboratory measurements. PaO2 is the arterial oxygen tension, and FiO2 is the fraction of inspired oxygen.

### 2. Coagulation

- **Platelet Count**: Also available in the laboratory measurements.

### 3. Liver

- **Bilirubin Level**: Found in the laboratory measurements.

### 4. Cardiovascular

- **Mean Arterial Pressure (MAP)**: This could be calculated from the vital sign measurements (Systolic BP, Diastolic BP).
- **Use of Vasopressors**: This information can be found in the medication prescriptions or input events.

### 5. CNS

- **Glasgow Coma Scale (GCS)**: This is generally recorded in the chart events.

### 6. Renal

- **Creatinine Level**: Found in the laboratory measurements.
- **Urine Output**: This could be found in the output events.





1. `PaO2` and `FiO2` from `LABEVENTS` (to calculate PaO2/FiO2 ratio)
2. `Platelet Count` from `LABEVENTS`
3. `Bilirubin Level` from `LABEVENTS`
4. `Systolic BP` and `Diastolic BP` from `CHARTEVENTS` (to calculate MAP)
5. `Glasgow Coma Scale` from `CHARTEVENTS`
6. `Creatinine Level` from `LABEVENTS`
7. `Urine Output` from `OUTPUTEVENTS`
8. `Vasopressor` information from `INPUTEVENTS_MV` or `INPUTEVENTS_CV`




