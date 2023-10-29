---
tags:
  - 📬
publish: "true"
aliases:
  - An application based on bioinformatics and machine learning for risk prediction of sepsis at first clinical presentation using transcriptomic data
  - shiApplicationBasedBioinformatics2022
url: https://www.frontiersin.org/articles/10.3389/fgene.2022.979529/full
DOI: 10.3389/fgene.2022.979529
citekey: shiApplicationBasedBioinformatics2022
keywords: [explainable, ✅, SHAP]
authors: "[Songchang Shi, Xiaobin Pan, Lihui Zhang, Xincai Wang, Yingfeng Zhuang, Xingsheng Lin, Songjing Shi, Jianzhang Zheng, Wei Lin]"
type: paper
status: 🟥
created: 
updated:
year: 2022
---



> [!meta]+ Metadata
> zotero_link:: [Shi et al. - 2022 - An application based on bioinformatics and machine.pdf](zotero://select/library/items/KQCM9ATF)
> abstract:: {(abstract)}


We explored the significance of each gene in the model and the interaction between each gene through SHAP analysis. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=U2F7UCYR)

Based on the sepsis-3 criteria (Shankar-Hari et al., 2016), infection was not confirmed, but the individuals were considered to be at 
	<mark class="hltr-yellow" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=UX665XEQ)

risk for sepsis. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=NL67PY44)

The KNN algorithm (Bania and Halder, 2020) was used to fill in the missing data. 
	<mark class="hltr-blue" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=9QI7GVLK)

Features that do not follow a standard normal distribution may cause the estimators in machine learning to deliver faulty outcomes. In our study, we used the StandardScaler utility class from the preprocessing module to perform data standardization. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=VRB9ZBL9)

Explanations based on the Shapley value have a solid theoretical foundation; it is the only attribution method that satisfies the requirements of local accuracy, missingness, and consistency (Lundberg et al., 2020; Yang et al., 2022). 
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=FM5ZSF6C)

Making the global analysis consistent with the local explanation, SHAP has been used to perform interpretability analysis by different researchers in their respective fields (Lundberg and Lee, 2017; Lundberg et al., 2020). 
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=MWETWBRG)

In principle, it is important to use “explainable models”; however, the machine learning models currently in use are claimed to be explainable but are not explainable or quasiexplainable (Yang et al., 2022). These models can provide flawed explanations in some studies that can lead to flawed correlation conclusions (Haufe et al., 2014). 
	<mark class="hltr-yellow" >Highlight</mark> [Page 9](zotero://open-pdf/library/items/?page=9&annotation=SKQ6YBN2)

FIGURE 6 Feature Sorting: Distinguishing feature values. The vertical axis shows ranked features according to the sum of the SHAP values of all samples, and the horizontal axis indicates the SHAP value (the distribution of the influence of the features on the model output). Each point represents a sample, the sample size was stacked vertically, and the color represents the feature value (red and blue correspond to high and low values, respectively). Taking the first row as an example, we observed that high ATP6V1D (red) had a positive impact on prediction, and low ATP6V1D (blue) had a negative impact on prediction. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 9](zotero://open-pdf/library/items/?page=9&annotation=GSRQLVDD)

```dataview
TABLE created, updated as modified, tags, type, related
FROM ""
WHERE contains(related, "shiApplicationBasedBioinformatics2022")
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