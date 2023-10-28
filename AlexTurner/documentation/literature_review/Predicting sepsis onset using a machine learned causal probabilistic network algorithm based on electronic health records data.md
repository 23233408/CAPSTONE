---
tags:
  - 📬
publish: "true"
aliases:
  - Predicting sepsis onset using a machine learned causal probabilistic network algorithm based on electronic health records data
  - valikPredictingSepsisOnset2023
url: https://www.nature.com/articles/s41598-023-38858-4
DOI: 10.1038/s41598-023-38858-4
citekey: valikPredictingSepsisOnset2023
keywords: [✅, keytext, EHR]
authors: "[John Karlsson Valik, Logan Ward, Hideyuki Tanushi, Anders F. Johansson, Anna Färnert, Mads Lause Mogensen, Brian W. Pickering, Vitaly Herasevich, Hercules Dalianis, Aron Henriksson, Pontus Nauclér]"
type: paper
status: 🟥
created: 
updated:
year: 2023
---



> [!meta]+ Metadata
> zotero_link:: [Valik et al. - 2023 - Predicting sepsis onset using a machine learned ca.pdf](zotero://select/library/items/FTLKXHVY)
> abstract:: {(abstract)}


early warning scores to detect patient deterioration, such as National Early Warning Score (NEWS2), have a broader purpose and are not specifically developed for sepsis6. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=YNBQ7LFH)

Sepsis patients had a median baseline Sequential Organ Failure Assessment (SOFA) score of 0 (interquartile range [IQR]: 0–1), at sepsis onset had a median SOFA of 2 (IQR: 2–4) and had a median worst SOFA of 3 (IQR: 2–5). 
	<mark class="hltr-yellow" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=M2VPGS4W)

causal probabilistic network (CPN) 
	<mark class="hltr-yellow" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=EKCDWU4P)

A limitation of several previous studies of machine learning based sepsis prediction tools is the use of administrative data to classify sepsis cases19–21. In this study, we used an objective sepsis classification based on clinical data, which is more reliable, less prone to bias, and robust over time22,23. 
	<mark class="hltr-blue" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=823S2DAH)

We focused on patients in the emergency department or non-ICU wards. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=P5X469I5)

![[valikPredictingSepsisOnset2023-5-x136-y123.png]]

CPNs are interpretable models, which are inherently explainable33. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 6](zotero://open-pdf/library/items/?page=6&annotation=E6GKDM2D)

routine measurements of heart rate, mean arterial pressure, respiratory rate, peripheral oxygen saturation, oxygen delivery (liters/minute), mental status, c-reactive protein, white blood cell count, platelets, bilirubin, creatinine, urea, albumin, lactate, HCO3, pH, current department, and time since surgery 
	<mark class="hltr-yellow" >Highlight</mark> [Page 9](zotero://open-pdf/library/items/?page=9&annotation=BCPQVTR7)

Measurements were filled forward without backfilling missing measurements. Only the most recent measurement, along with the time since it was measured, was used at each screening. As an input for model training, a discretized time-to-sepsis label was used. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 9](zotero://open-pdf/library/items/?page=9&annotation=ZT4RMQG8)

```dataview
TABLE created, updated as modified, tags, type, related
FROM ""
WHERE contains(related, "valikPredictingSepsisOnset2023")
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