---
tags:
  - 📬
publish: "true"
aliases:
  - Superhuman performance on sepsis MIMIC-III data by distributional reinforcement learning
  - bockSuperhumanPerformanceSepsis2022
url: https://dx.plos.org/10.1371/journal.pone.0275358
DOI: 10.1371/journal.pone.0275358
citekey: bockSuperhumanPerformanceSepsis2022
keywords: [MIMIC-III, data availability]
authors: "[Markus Böck, Julien Malle, Daniel Pasterk, Hrvoje Kukina, Ramin Hasani, Clemens Heitzinger]"
type: paper
status: 🟥
created: 
updated:
year: 2022
---



> [!meta]+ Metadata
> zotero_link:: [Böck et al. - 2022 - Superhuman performance on sepsis MIMIC-III data by.pdf](zotero://select/library/items/3R9HDRE3)

# summary

Data pipeline using MIMIC-III

Uses KNN with a custom distance metric (to replace Euclidean distance) in order to impute missing data

references the data preprocessing techniques in [this study]( https://www.nature.com/articles/s41591-018-0213-5#Sec14) 

# notes

From a machine learning perspective, despite the availability of a significant amount of unstructured data [7, 8], advanced and novel preprocessing techniques are required to make sense of the data. Moreover, sepsis treatment consists of modeling irregularly-sampled time series with long-term dependencies [9] which adds to its complexity." Gray
	<mark class="hltr-gray" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=3VF3962L)

Biomarkers and physiomarkers suggested by recent works such as [16–18]" Blue
	<mark class="hltr-blue" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=PVERT8HA)

especially where more rapid action is required

An approach mixing SQL queries and Julia programming [23] was chosen to properly organize data. To mitigate the long time horizon concerning other methods [19], we modified the time discretization from four-hour steps to one-hour steps to better model the biological processes under test. This, however, makes the missing-value imputation step more challenging. We address this by a novel method for matrix completion detailed in the following subsection" Yellow
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=2XCKRN34)

2.2 Missing-value imputation The dataset contains substantial amount of missing values which has to be taken care of. In the particular case of sepsis, we require some variables to be known to be able to apply the Sepsis-3 criteria [21] to decide whether apatient suffers from sepsis or not." Yellow
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=SFP877L2)

![[bockSuperhumanPerformanceSepsis2022-3-x63-y470.png]]

All features contain missing-values. Because of this, aclassical k-nearest-neighbors (kNN) model for imputation isnot directly applicable since itrequires acommon ground between observations to compute pairwise distances (and gather nearest neighbors)." Green
	<mark class="hltr-green" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=8V2KGQWZ)

![[bockSuperhumanPerformanceSepsis2022-4-x54-y246.png]]

To overcome this problem, we introduce the following distance metric that isable to handle missing values and will replace the euclidean distance in the kNN computations. The distance isdefined as:" Green
	<mark class="hltr-green" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=34Q8HWV5)

2.3 State representation Itishard to find an approximation of the formations contained in the continuous raw data into atabular form, specially due to high dimensionality. In this regard, the following problems arises: •The amount of data islimited. Therefore, the train-test split of data faces atrade off, for avoiding overfitting. Hence, careful considerations has to be taken into account for efficient sampling. •Edge cases and outliers in the data should not be ignored as they are special disease patterns." Gray
	<mark class="hltr-gray" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=MXXFVTE4)

16. Alqahtani MF, Marsillio LE, Rozenfeld RA. Areview ofbiomarke rsand physiomarkers inpediatric sepsis. Clinical Pediatric EmergencyMedicine. 2014; 15:177–184. https://doi.org/10.1016/j.cpem.2014.04. 008 17. Mohammed A, Van Wyk F,Chinthala LK, Khojandi A, Davis RL, CoopersmithCM, etal. TemporalDifferential ExpressionofPhysiomar kers Predicts Sepsis inCritically IllAdults. SHOCK. 2021; 56:58–64. https://doi.org/10.1097/SHK.0000000000001670 PMID: 32991797 18. Zimmet AM, Sullivan BA, Moorman JR, Lake DE, Ratcliffe SJ. Trajectories ofthe heart rate characteristics index, aphysiom arker ofsepsis inpremature infants, predict Neonatal ICU mortality. JRSM cardiovascular disease. 2020; 9.https:// doi.org/10.1177/2048004020945142 PMID: 33240492" Blue
	<mark class="hltr-blue" >Highlight</mark> [Page 17](zotero://open-pdf/library/items/?page=17&annotation=GH84TP9P)

Recent literature biomarkers

```dataview
TABLE created, updated as modified, tags, type, related
FROM ""
WHERE contains(related, "bockSuperhumanPerformanceSepsis2022")
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