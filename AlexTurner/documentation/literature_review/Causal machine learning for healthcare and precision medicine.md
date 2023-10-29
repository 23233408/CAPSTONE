---
tags:
  - 📬
publish: "true"
aliases:
  - Causal machine learning for healthcare and precision medicine
  - sanchezCausalMachineLearning2022
url: https://royalsocietypublishing.org/doi/10.1098/rsos.220638
DOI: 10.1098/rsos.220638
citekey: sanchezCausalMachineLearning2022
keywords: [find, re-read, causal, causality]
authors: "[Pedro Sanchez, Jeremy P. Voisey, Tian Xia, Hannah I. Watson, Alison Q. O’Neil, Sotirios A. Tsaftaris]"
type: paper
status: 🟥
created: 
updated:
year: 2022
---



> [!meta]+ Metadata
> zotero_link:: [Sanchez et al_2022_Causal machine learning for healthcare and precision medicine.pdf](zotero://select/library/items/H65LGJ4H)
> abstract:: {(abstract)}


causality: if A is a cause and B is an effect, then B relies on A for its value. As causal relations are directional, the reverse is not true; A does not rely on B for its value. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=URDKIZKP)

Even though data from EHRs, for example, are usually observational, they have already been successfully leveraged in several ML applications [17], such as modelling disease progression [18], predicting disease deterioration [19] and discovering risk factors [20], as well as for predicting treatment responses [21]. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 6](zotero://open-pdf/library/items/?page=6&annotation=NB7ZYKDK)

the best treatment for an individual—the main goal of precision medicine [26]—can only be identified with a model that is capable of causal reasoning 
	<mark class="hltr-yellow" >Highlight</mark> [Page 6](zotero://open-pdf/library/items/?page=6&annotation=QZX3YRRG)

![[sanchezCausalMachineLearning2022-9-x131-y588.png]]

Figure 3. We illustrate the difference between individualized and average treatment effect (ITE versus ATE). ‘Feature’ represents patient characteristics, which would be multi-dimensional in reality. ‘Outcome’ is some measure of response to the treatment, where a more positive value is preferable. The ITE for each patient is the difference between actual and the counterfactual outcome. We show an example counterfactual to highlight that ITE for some patients might differ from the average (ATE). By employing causal inference methods to estimate individualized treatment effects, we can understand which patients benefit from certain medication and which patients do not, thus enabling us to make personalized treatment recommendations. Note that the patient data points are evenly distributed along the feature axis, which would indicate that this data comes from an RCT (due to lack of bias). The estimation of treatment affect using observational data is subject to confounding as patient characteristics affect both the selection of treatment and outcome. Causal inference methods need to mitigate this. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 9](zotero://open-pdf/library/items/?page=9&annotation=7W6RUWID)

Managing diseases such as AD can be challenging due to the heterogeneity of symptoms and their trajectory over time across the population. A pathology might evolve differently for patients with different covariates. For treatment decisions in a longitudinal setting, CI methods need to model patient history and treatment timing [65]. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 10](zotero://open-pdf/library/items/?page=10&annotation=FJI8PVCG)

```dataview
TABLE created, updated as modified, tags, type, related
FROM ""
WHERE contains(related, "sanchezCausalMachineLearning2022")
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