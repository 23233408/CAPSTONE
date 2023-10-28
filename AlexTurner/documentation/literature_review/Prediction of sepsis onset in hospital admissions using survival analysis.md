---
tags:
  - 📬
publish: "true"
aliases:
  - Prediction of sepsis onset in hospital admissions using survival analysis
  - deshonPredictionSepsisOnset2022
url: https://link.springer.com/10.1007/s10877-022-00804-6
DOI: 10.1007/s10877-022-00804-6
citekey: deshonPredictionSepsisOnset2022
keywords: [✅, SIRS, LSTM, MIMC03, survival analysis, DeepSurv, regularized Cox]
authors: "[Brandon DeShon, Benjamin Dummitt, Joshua Allen, Byron Yount]"
type: paper
status: 🟥
created: 
updated:
year: 2022
---



> [!meta]+ Metadata
> zotero_link:: [DeShon et al. - 2022 - Prediction of sepsis onset in hospital admissions .pdf](zotero://select/library/items/QNZUSDBJ)
> abstract:: {(abstract)}




* MIMIC-III dataset
* Survival analysis

Sepsis represents a significant burden to healthcare in terms of both patient outcomes and financial costs as it accounts for more than 50% of hospital deaths [1] and the average cost to the payor organizations, per sepsisrelated hospitalization is $18,023 when present on admission and $51,022 when it develops in the hospital [2]." Gray
	<mark class="hltr-gray" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=2T45I7DB)

The distinction between sepsis that is present upon admission vs. onset that occurs during a hospital stay is an important one. Hospital length of stay, ICU length of stay, mortality, payor costs, and readmission rate are all significantly worse for patients with sepsis that develops subsequent to hospital admission [2–4]." Yellow
	<mark class="hltr-yellow" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=APS2SYG8)

Low prevalence of positive cases is not a concern as the assumptions for Cox proportional hazards are met under the conditions of the study design [23]. The DeepSurv model is also expected to be resilient to case imbalance as it incorporates the Cox model’s log-risk as it’s activation function [18]." Yellow
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=FZZTJ28R)

Benefits of Cox proportional hazards

We used both ‘last observation carried forward’ (LOCF) and median imputation to account for missing values." Yellow
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=V3AUA3P8)

We additionally implemented a deep learning-based survival methodology for comparison with regularized or nonregularized Cox models. The deep learning survival model (DeepSurv) is a feed forward neural network that has the activation function estimating the log-risk function of a Cox model and the objective function set to the average negative log partial likelihood [18]." Yellow
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=WT3L69ZD)

supplementary material available at https://doi.org/10.1007/s10877-022-00804-6." Yellow
	<mark class="hltr-yellow" >Highlight</mark> [Page 8](zotero://open-pdf/library/items/?page=8&annotation=JQ7SNGHS)

```dataview
TABLE created, updated as modified, tags, type, related
FROM ""
WHERE contains(related, "deshonPredictionSepsisOnset2022")
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