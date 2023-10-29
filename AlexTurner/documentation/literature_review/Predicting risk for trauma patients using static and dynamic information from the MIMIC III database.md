---
tags:
  - 📬
publish: "true"
aliases:
  - Predicting risk for trauma patients using static and dynamic information from the MIMIC III database
  - tsiklidisPredictingRiskTrauma2022
url: https://dx.plos.org/10.1371/journal.pone.0262523
DOI: 10.1371/journal.pone.0262523
citekey: tsiklidisPredictingRiskTrauma2022
keywords: [survival, MIMIC-III, ✅, trauma]
authors: "[Evan J. Tsiklidis, Talid Sinno, Scott L. Diamond]"
type: paper
status: 🟥
created: 
updated:
year: 2022
---



> [!meta]+ Metadata
> zotero_link:: [Tsiklidis et al. - 2022 - Predicting risk for trauma patients using static a.pdf](zotero://select/library/items/NPT56A45)
> abstract:: {(abstract)}


The MIMIC-III database was filtered toextract 5,400 trauma patient records (526 non-survivors)each ofwhich contained 5static variables (age, gender, etc.) and 28 dynamic variables (e.g., vital signs and metabolic panel). Training data was also extracted from the dynamic variables using a3-hour moving time window whereby each window was treated as aunique patient-time fragment. We extracted the mean, standard deviation, and skew from each ofthese 3-hour fragments and included them as inputs for training. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=4YDH8USS)

Since modern intensive care units (ICU) monitor patients continuously, the data-rich environment can be used to predict mortality, time-dependent risk, and provide opportunities for data science and machine learning [2,3]. Due to the high patient-to-patient variability, adata-driven approach isareasonable way of predicting patient outcomes as patient-scale mechanistic models developed from first principles are highly challenging and likely injury-specific [4–6]. 
	<mark class="hltr-gray" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=YE2UZR8Q)

exclusion criterion consistent with the work of Alistair et al., where patients were excluded ifthey were neonatal or pediatric patients (age < 16), presented in the ICU for less than 4hours, 
	<mark class="hltr-red" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=8VKKDDXZ)

![[tsiklidisPredictingRiskTrauma2022-3-x164-y401.png]]

![[tsiklidisPredictingRiskTrauma2022-3-x191-y79.png]]

The rate of missingness for dynamic variables prior to imputation isshown in Table 2. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=PA9M56ED)

![[tsiklidisPredictingRiskTrauma2022-4-x187-y510.png]]

![[tsiklidisPredictingRiskTrauma2022-4-x191-y70.png]]

```dataview
TABLE created, updated as modified, tags, type, related
FROM ""
WHERE contains(related, "tsiklidisPredictingRiskTrauma2022")
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