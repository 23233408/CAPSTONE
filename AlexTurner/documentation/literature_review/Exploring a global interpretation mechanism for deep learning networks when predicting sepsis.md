---
tags:
  - 📬
publish: "true"
aliases:
  - Exploring a global interpretation mechanism for deep learning networks when predicting sepsis
  - stricklerExploringGlobalInterpretation2023
url: https://www.nature.com/articles/s41598-023-30091-3
DOI: 10.1038/s41598-023-30091-3
citekey: stricklerExploringGlobalInterpretation2023
keywords: [interpretability, ✅, deep learning, sepsis, LSTM, blackbox, keytext]
authors: "[Ethan A. T. Strickler, Joshua Thomas, Johnson P. Thomas, Bruce Benjamin, Rittika Shamsuddin]"
type: paper
status: 🟥
created: 
updated:
year: 2023
---



> [!meta]+ Metadata
> zotero_link:: [Strickler et al. - 2023 - Exploring a global interpretation mechanism for de.pdf](zotero://select/library/items/SU7NVC69)
> abstract:: {(abstract)}


we identified 17 features that the LSTM used for sepsis classification, 11 of which overlaps with the top 20 features from the Random Forest model, 10 with academic features and 5 with clinical features. Clinical opinion suggests, 3 LSTM features have strong correlation with some clinical features that were not identified by the mechanism. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=YNFL3PWP)

age, chloride ion concentration, pH and oxygen saturation should be investigated further for connection with developing sepsis. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=HUP3TLJ8)

![[stricklerExploringGlobalInterpretation2023-2-x107-y79.png]]

However, the accuracy-interpretability trade-off6,7 in ML is still an open research challenge, where model complexity is directly proportional to higher accuracy, but inversely proportional with human-interpretability. Examples of these can also be seen in sepsis detection8–27. As a result, even though ML has greatly advanced healthcare data analysis28–35, computational healthcare studies (including sepsis detection8–11,30,36) often choose statistics, intrinsically interpretable ML models and/or feature selection methods for analysis, instead of stateof-the-art ML models with higher accuracy. Moreover, there is no guarantee that local explanation provided (via post-hoc analysis using LIME37/SHAP38,39) for one instance in the dataset will be the same for a different instance in the same dataset, even if they share the class membership. As such, features obtained from local explanations will not be a good representation of the additional relevant features needed for timely sepsis detection. Thus, global interpreter for state-of-art-model is essential because it can aid the task of identifying relevant sepsis factors. Moreover, a global interpreter allows black-box models to retain their high accuracy, while becoming more transparent to human beings. Various works have addressed the challenge of creating global interpreters, and some notable examples include40, 
	<mark class="hltr-gray" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=S2CYTFPB)

dditionally, for human interpretability, it is important to provide explanations of decisions in easy terms that understandable by the general population; yet, some methods such as covariance matrices2,27 require a certain expertise for interpretation. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=ISF5IWTY)

This is further complicated by the fact that literature studies5,20,21,26,27,30,44–48, and our own experiments show that it is difficult to obtain high and balanced specificity and sensitivity for ML models on sepsis detection, especially when using the publicly available, physiological dataset5 on sepsis; as such, a large body of work on sepsis16,44–48, uses text data and Electronic Health Records (EHR). 
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=WXJHHAGS)

vital signs (heart rate, blood pressure, etc.), laboratory values (pH, platelet count, hemoglobin, etc.), and demographics (age, gender, etc.). 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=FTDTQWNQ)

-	*Features*

![[stricklerExploringGlobalInterpretation2023-5-x143-y484.png]]

![[stricklerExploringGlobalInterpretation2023-10-x36-y475.png]]

```dataview
TABLE created, updated as modified, tags, type, related
FROM ""
WHERE contains(related, "stricklerExploringGlobalInterpretation2023")
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