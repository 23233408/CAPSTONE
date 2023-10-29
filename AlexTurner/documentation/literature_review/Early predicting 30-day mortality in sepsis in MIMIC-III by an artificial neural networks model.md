---
tags:
  - 📬
publish: "true"
aliases:
  - Early predicting 30-day mortality in sepsis in MIMIC-III by an artificial neural networks model
  - suEarlyPredicting30day2022
url: https://eurjmedres.biomedcentral.com/articles/10.1186/s40001-022-00925-3
DOI: 10.1186/s40001-022-00925-3
citekey: suEarlyPredicting30day2022
keywords: [MIMIC-III, neural networks, predicting mortality, ✅]
authors: "[Yingjie Su, Cuirong Guo, Shifang Zhou, Changluo Li, Ning Ding]"
type: paper
status: 🟥
created: 
updated:
year: 2022
---



> [!meta]+ Metadata
> zotero_link:: [Su et al. - 2022 - Early predicting 30-day mortality in sepsis in MIM.pdf](zotero://select/library/items/YCCG3ELE)
> abstract:: {(abstract)}




-	*datasetTable 1: general characteristics of sepsisfilters out patients with missing data, as well as those under 18


Good methodology. May be irrelevant, as it is working with patients who have already been diagnosed with sepsis.*

Methods Database and patients MIMIC-III database is a US-based critical care public database. Clinical and laboratory data associated with 53,423 age ≥ 16 patients from 2001 to 2012 and 7870 neonates from 2001 to 2008 admitted in ICU were documented [13]. The database mainly included charted events such as demographics, vital signs, laboratory tests, vital status, medications, image reports, and clinical outcomes. All patients with sepsis (ICD9 code: 99,591) in MIMICIII (version 1.4) were enrolled in this study. Exclusion criteria included as follows: patients with missing > 5% individual data and age less than 18. 
	<mark class="hltr-orange" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=J79PAEI3)

age at the time of hospital admission, gender, admission type, marital status, ethnicity, ICU department, comorbidities (renal disease, coronary artery disease (CAD), diabetes, and hypertension), sequential organ failure assessment (SOFA) score and acute physiology and chronic health evaluation (APACHEII) score. The length of stay (LOS) in ICU and in-hospital mortality were also collected. 
	<mark class="hltr-orange" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=YM4ZBBYD)

Clinical and laboratory variables which were recorded within 24  h after admission were also extracted including systolic blood pressure (SBP), diastolic blood pressure (DBP), heart rate (HR), respiratory rate (RR), white blood cells (WBC), neutrophils, lymphocytes, sodium, chloride, platelet (PLT), red cell volume distribution width (RDW), mean corpusular volume (MCV), hematocrit, glucose, prothrombin time (PT), partial thrombin time (PTT), albumin, alanine aminotransferase (ALT), aspartate aminotransferase (AST), total bilirubin, urea nitrogen, creatinine, lactate, total calcium, and anion gap. NLR is defined as the ratio of neutrophils to lymphocytes. Multiple multivariable imputations were utilized for addressing missing data to maximize statistical power and minimize bias. 
	<mark class="hltr-orange" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=KSLJUDN2)

![[suEarlyPredicting30day2022-3-x297-y140.png]]

The main structures of artificial neural networks were illuminated in Fig.  2. 11 variables including age, AST, MCV, ALT, urea nitrogen, PTT, PT, RDW, lactate, albumin and total bilirubin which showed significant differences between two groups were selected for the input layer. 
	<mark class="hltr-green" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=5XKJRRCA)

ANN model with an AUC of 0.811 was significantly superior to compared to LR, SOFA score and APACHEII score. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 6](zotero://open-pdf/library/items/?page=6&annotation=453S748G)

low serum albumin levels 
	<mark class="hltr-yellow" >Highlight</mark> [Page 7](zotero://open-pdf/library/items/?page=7&annotation=JCD2SK7U)

[24]. 
	<mark class="hltr-orange" >Highlight</mark> [Page 7](zotero://open-pdf/library/items/?page=7&annotation=XYPF5TCP)

higher RDW was independently associated with 28-day mortality 
	<mark class="hltr-yellow" >Highlight</mark> [Page 8](zotero://open-pdf/library/items/?page=8&annotation=WR547IXJ)

Some limitations should be stated in our study. First, the MIMIC-III public database included data before 2012, while the new definition of Sepsis-3.0 was published in 2016. 
	<mark class="hltr-blue" >Highlight</mark> [Page 9](zotero://open-pdf/library/items/?page=9&annotation=P4GMBUJX)

Differences in the definition of sepsis in different phrases should be considered when applying our ANN model. Second, due to a high percentage of missing values in MIMIC-III, not all the variables which may affect the clinical outcomes in sepsis were included and analyzed. Some variables including the percentage of patients that received antibiotics, and the timing of such were not analyzed, 
	<mark class="hltr-blue" >Highlight</mark> [Page 9](zotero://open-pdf/library/items/?page=9&annotation=RR4NP93Y)

Methods Database and patients MIMIC-III database is a US-based critical care public database. Clinical and laboratory data associated with 53,423 age ≥ 16 patients from 2001 to 2012 and 7870 neonates from 2001 to 2008 admitted in ICU were doc- ≥ neonates from 2001 to 2008 admitted in ICU were documented [13]. Te database mainly included charted events such as demographics, vital signs, laboratory tests, vital status, medications, image reports, and clinical outcomes. All patients with sepsis (ICD9 code: 99,591) in MIMICIII (version 1.4) were enrolled in this study. Exclusion criteria included as follows: patients with missing > 5% individual data and age less than 18. 
	<mark class="hltr-orange" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=highlight-p2x56y449)

age at the time of hospital admission, gender, admission type, marital status, ethnicity, ICU department, comorbidities (renal disease, coronary artery disease (CAD), diabetes, and hypertension), sequential organ failure assessment (SOFA) score and acute physiology and chronic health evaluation (APACHEII) score. Te length of stay (LOS) in ICU and in-hospital mortality were also collected. 
	<mark class="hltr-orange" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=highlight-p2x56y305)

Clinical and laboratory variables which were recorded within 24 h after admission were also extracted including systolic blood pressure (SBP), diastolic blood pressure (DBP), heart rate (HR), respiratory rate (RR), white blood cells (WBC), neutrophils, lymphocytes, sodium, chloride, platelet (PLT), red cell volume distribution width (RDW), mean corpusular volume (MCV), hematocrit, glucose, prothrombin time (PT), partial thrombin time (PTT), albumin, alanine aminotransferase (ALT), aspartate aminotransferase (AST), total bilirubin, urea nitrogen, creatinine, lactate, total calcium, and anion gap. NLR is defned as the ratio of neutrophils to lymphocytes. Multiple multivariable imputations were utilized for addressing missing data to maximize statistical power and minimize bias. 
	<mark class="hltr-orange" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=highlight-p2x56y137)

```dataview
TABLE created, updated as modified, tags, type, related
FROM ""
WHERE contains(related, "suEarlyPredicting30day2022")
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