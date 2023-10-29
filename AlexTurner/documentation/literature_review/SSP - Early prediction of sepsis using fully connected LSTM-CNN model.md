---
tags:
  - 📬
publish: "true"
aliases:
  - SSP: Early prediction of sepsis using fully connected LSTM-CNN model
  - rafieiSSPEarlyPrediction2021
url: https://linkinghub.elsevier.com/retrieve/pii/S0010482520304418
DOI: 10.1016/j.compbiomed.2020.104110
citekey: rafieiSSPEarlyPrediction2021
keywords: [✅]
authors: "[Alireza Rafiei, Alireza Rezaee, Farshid Hajati, Soheila Gheisari, Mojtaba Golzan]"
type: paper
status: 🟥
created: 
updated:
year: 2021
---



> [!meta]+ Metadata
> zotero_link:: [Rafiei et al. - 2021 - SSP Early prediction of sepsis using fully connec.pdf](zotero://select/library/items/PAVYY5CT)
> abstract:: {(abstract)}


Smart Sepsis Predictor (SSP) 
	<mark class="hltr-orange" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=BJPK58EG)

SSP is a deep neural network architecture that encompasses long short-term memory (LSTM), convolutional, and fully connected layers 
	<mark class="hltr-orange" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=FUUR94QR)

Using ICU data, sepsis onset can be predicted up to 12 h in advance. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=LFFLZPK7)

Various disease scoring systems and diagnostic criteria are used in hospitals to identify patients with sepsis [17,18]. Systemic Inflammatory Response Syndrome (SIRS) is one of the first sepsis diagnostic criteria [19,20]. The Third International Consensus Definitions for Sepsis (Sepsis-3) is a redefinition of sepsis that has been recently introduced [4]. This definition emphasizes the priority of the non-homeostatic host response to infection, the possible lethality that is hugely over a straightforward infection, and the need for instant recognition. The Sequential Organ Failure Assessment (SOFA) scoring system is used to track a person’s status during the ICU to determine the gamut of a person’s organ function or failure rate in Sepsis-3 guidelines. This predominant score is based on six different ratings: the mean arterial pressure, serum glucose, bilirubin, PaO2/FiO2 ratio, platelets, and creatinine. In the SOFAscoring system, an acute change higher than two or more points in the total SOFA score can indicate organ failure consequent to the infection. A higher SOFA score is correlated with an increase in the probability of mortality [21]. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=3SPD8GMP)

The overall structure of the SSP is shown in Fig. 1. SSP takes three types of input data (vital signs, laboratory tests, and demographics) in two modes: Mode 1 and Mode 2. In Mode 1, it uses vital signs and de mographics. In Mode 2, it also takes laboratorytests. The first step of SSP is an inclusion block, through which unfavorable records are filtered. Following this, a deep network block containing Long Short-Term Memory (LSTM), convolutional, and fully connected layers is used to estimate the probability of sepsis onset. By applying a pre-set reference threshold, the model can assess whether the patient is suspected of sepsis or not. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=RWRRXSAQ)

![[rafieiSSPEarlyPrediction2021-3-x72-y42.png]]

![[media/zotero/rafieiSSPEarlyPrediction2021/rafieiSSPEarlyPrediction2021-4-x38-y631.png]]

![[rafieiSSPEarlyPrediction2021-5-x70-y81.png]]

Smart Sepsis Predictor (SSP) 
	<mark class="hltr-orange" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=highlight-p1x380y464)

SSP is a deep neural network architecture that encompasses long short-term memory (LSTM), convolutional, and fully connected layers 
	<mark class="hltr-orange" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=highlight-p1x202y445)

```dataview
TABLE created, updated as modified, tags, type, related
FROM ""
WHERE contains(related, "rafieiSSPEarlyPrediction2021")
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