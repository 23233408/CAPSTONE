---
tags:
  - 📬
publish: "true"
aliases:
  - Learning representations for the early detection of sepsis with deep neural networks
  - kamLearningRepresentationsEarly2017
url: https://linkinghub.elsevier.com/retrieve/pii/S0010482517302743
DOI: 10.1016/j.compbiomed.2017.08.015
citekey: kamLearningRepresentationsEarly2017
keywords: [✅, deep learning, early detection, SIRS, LSTM, feature extraction, multivariate time-series, time-series]
authors: "[Hye Jin Kam, Ha Young Kim]"
type: paper
status: 🟥
created: 
updated:
year: 2017
---



> [!meta]+ Metadata
> zotero_link:: [Kam and Kim - 2017 - Learning representations for the early detection o.pdf](zotero://select/library/items/D4VZIEIF)
> abstract:: {(abstract)}


Although a new Sepsis-3 definition for the occurrence of sepsis was defined in 2016 [21], discussions on the effectiveness of the newly proposed definition are continuing. 
	<mark class="hltr-red" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=64BK8E9V)

In this study, as in the reference paper [17], the target detection time for a patient with sepsis was defined as the first hour in which two or more of the former conditions were satisfied with confirmed sepsis infection in the hospital with the ICD-9 code 995.9 for each hospitalization episode. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=4X85ELP6)

The time of “early” detection of the generation group was also set at the same time as the reference paper: 3 h prior to the target detection hour. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=G5YIFZRV)

We selected the following basic variables based on their versatility: (1) systolic blood pressure, (2) pulse pressure, (3) heart rate, (4) body temperature, (5) respiration rate, (6) white blood cell count, (7) pH, (8) blood oxygen saturation, and (9) age. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=XVH4ATMX)

-	*Features*

Representative value of basic variables summarized in 1 h intervals Because the measurement interval of each variable in the electronic medical record varies from 10 min to 24 h, the basic data of the patient was summarized by extracting the minimum (min), average (avg), and maximum (max) values per 1 h interval, which was the most common interval for each variable (see Table 2). If there was no measured value at the corresponding time, the nearest measured value was imputed in place of the missing value. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=M6TJ9VMN)

Reference features in the 5 h time window Reference features were extracted to reflect the change in datum value in a 5 h window, and this was performed with the subsequent steps by Calvert et al. [17]. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=6IPP6VVU)

![[kamLearningRepresentationsEarly2017-3-x23-y126.png]]

Our results also show improvements in the AUC and sensitivity, although not significant, compared with the DFN models, SepDFN100 and SepDFN109, using the 100 basic features and the human - extracted temporal 109 reference features, respectively. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 6](zotero://open-pdf/library/items/?page=6&annotation=H86Z2L4D)

As is already known from several reports [21], the SIRS is not a necessary and sufficient condition for the occurrence of sepsis. Therefore, the above - mentioned cases (1) and (2) may occur but, in order to predict sepsis early, case (2) should be included. However, in this paper, because the 5 h - SIRS conditions were defined as the condition of early detection, the target time cannot be determined in their absence and, therefore, case (2) inevitably has to be excluded. In future studies, it is necessary to study models with various criteria related to sepsis diagnosis, especially version 3. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 6](zotero://open-pdf/library/items/?page=6&annotation=IT946SQX)

-	*Limitations of data - group definition with SIRS*

Unlike studies that attempt to interpret the model itself, recent studies have attempted to explain the information that led to the decisions of DNN models [49,50] 
	<mark class="hltr-blue" >Highlight</mark> [Page 7](zotero://open-pdf/library/items/?page=7&annotation=WN5PBJU6)

```dataview
TABLE created, updated as modified, tags, type, related
FROM ""
WHERE contains(related, "kamLearningRepresentationsEarly2017")
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