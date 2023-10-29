---
tags:
  - 📬
publish: "true"
aliases:
  - Predicting 30-days mortality for MIMIC-III patients with sepsis-3: a machine learning approach using XGboost
  - houPredicting30daysMortality2020
url: https://translational-medicine.biomedcentral.com/articles/10.1186/s12967-020-02620-5
DOI: 10.1186/s12967-020-02620-5
citekey: houPredicting30daysMortality2020
keywords: []
authors: "[Nianzong Hou, Mingzhe Li, Lu He, Bing Xie, Lin Wang, Rumin Zhang, Yong Yu, Xiaodong Sun, Zhengsheng Pan, Kai Wang]"
type: paper
status: 🟥
created: 
updated:
year: 2020
---



> [!meta]+ Metadata
> zotero_link:: [Hou et al. - 2020 - Predicting 30-days mortality for MIMIC-III patient.pdf](zotero://select/library/items/LDDTZUJJ)
> abstract:: {(abstract)}


the early identification and diagnosis for sepsis are essential, which could provide meaningful information for clinicians to assess patients’ condition and improve survival outcomes through prompt and appropriate treatment. 
	<mark class="hltr-gray" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=EUVCN7J9)

Due to the complex of vague sepsis syndrome definitions, unknown sources of infection and higher mortality, it is necessary to establish a reliable and effective prognostic model for sepsis. With the help of these prognostic models, strong evidences for clinical decision-making and rational allocation of public health care resources can be provided. 
	<mark class="hltr-gray" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=ELIQNGZQ)

The database contains charted events such as demographics, vital signs, laboratory tests, fluid balance and vital status; documents International Classification of Diseases and Ninth Revision (ICD-9) codes; records hourly physiologic data from bedside monitors validated by ICU nurses; and stores written evaluations of radiologic films by specialists covering in the corresponding time period. 
	<mark class="hltr-orange" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=E263ASBF)

Adult patients who were diagnosed with sepsis-3 were included in our study. The inclusion criteria were: (I) patients who were older than 18 years old; (II) length of stay in the ICU was over 24  h to ensure sufficient data for analysis; (III) patients with the diagnosed of sepsis according to The Third International Consensus Definitions for Sepsis and Septic Shock (sepsis-3) [2]. 
	<mark class="hltr-red" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=HR5G72EJ)

As it is common with missing data in the MIMIC-III database, we also removed the variables with more than 20% observations missing to facilitate and ensure the accuracy of the review. 
	<mark class="hltr-orange" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=GWVPC3L9)

As it is common with missing data in the MIMIC-III database, we also removed the variables with more than 20% observations missing to facilitate and ensure the accuracy of the review. However, for those with less than 20% missing data or randomly missing data, we explored and visualized them with Templ’s method (R Package “VIM”) [14] and multiple imputation method (R Package “mice”) [15] for further analysis respectively. 
	<mark class="hltr-red" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=55PHHCMG)

Following demographic data were extracted: age, gender, ethnicity, weight, height and body mass index (BMI), length of stay in hospital, length of stay in the ICU, hospital expire flag (in-hospital death recorded in the hospital database) at the first ICU admission. Then, we collected vital signs of the patients from the first 24 h of ICU stay, including heart rate (HR), systolic blood pressure (SBP), diastolic blood pressure (DBP), mean arterial pressure (MAP), temperature (TEMP), respiratory rate (RR) and oxyhemoglobin saturation (SpO2). Afterwards, laboratory values, such as blood routine examination, liver and kidney function, blood glucose, and arterial blood gas 
	<mark class="hltr-green" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=ZZD8CYYD)

![[houPredicting30daysMortality2020-3-x49-y65.png]]

(ABG) were abstracted. Furthermore, advanced cardiac life support (mechanical ventilation, renal replacement therapy, etc.) and accompanied diseases (diabetes, malignant tumour, etc.) were accessed. Because of the high sampling frequency, we use the maximum, minimum and the mean value when incorporating the characteristics of vital signs and related laboratory indicators. 
	<mark class="hltr-green" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=CFUJ9QC8)

Additional file 1. Extracted raw data from the MIMIC-III. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 12](zotero://open-pdf/library/items/?page=12&annotation=UQEBJUAH)

Te database contains charted events such as demographics, vital signs, laboratory tests, fuid balance and vital status; documents International Classifcation of Diseases and Ninth Revision (ICD-9) codes; records hourly physiologic data from bedside monitors validated by ICU nurses; and stores written evaluations of radiologic flms by specialists covering in the corresponding time period. 
	<mark class="hltr-orange" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=highlight-p2x304y329)

As it is common with missing data in the MIMIC-III database, we also removed the variables with more than 20% observations missing to facilitate and ensure the accuracy of the review. 
	<mark class="hltr-orange" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=highlight-p3x56y605)

```dataview
TABLE created, updated as modified, tags, type, related
FROM ""
WHERE contains(related, "houPredicting30daysMortality2020")
```


# Notes

| Highlight colour | Meaning |
|-----|----|
|<mark class="hltr-red">red</mark> | Disagree with Author |
|<mark class="hltr-orange">orange</mark> | Important Point by Author |
|<mark class="hltr-yellow">yellow</mark> | Interesting Point |
|<mark class="hltr-green">green</mark> | Important to me |
|<mark class="hltr-blue">blue</mark> | Notes after Initial Iteration |
|<mark class="hltr-purple">purple</mark> | Literary Note to Lookup Later |