---
tags:
  - 📬
publish: "true"
aliases:
  - A Machine Learning Model for Accurate Prediction of Sepsis in ICU Patients
  - wangMachineLearningModel2021
url: https://www.frontiersin.org/articles/10.3389/fpubh.2021.754348/full
DOI: 10.3389/fpubh.2021.754348
citekey: wangMachineLearningModel2021
keywords: [✅, infection, sepsis, random forest]
authors: "[Dong Wang, Jinbo Li, Yali Sun, Xianfei Ding, Xiaojuan Zhang, Shaohua Liu, Bing Han, Haixu Wang, Xiaoguang Duan, Tongwen Sun]"
type: paper
status: 🟥
created: 
updated:
year: 2021
---



> [!meta]+ Metadata
> zotero_link:: [Wang et al. - 2021 - A Machine Learning Model for Accurate Prediction o.pdf](zotero://select/library/items/C25AJ4IV)
> abstract:: {(abstract)}




-	*Provides a clinical explanation of early identifiers*

a set of 55 features (variables) was calculated and passed to the random forest algorithm to predict the onset of sepsis 
	<mark class="hltr-yellow" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=GT8F4I9H)

To date, the diagnosis of sepsis has largely relied on determining the presence of infection and organ dysfunction (4). 
	<mark class="hltr-orange" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=LWRGCWCP)

The early detection and prediction of patients who may develop sepsis is essential to improve the adverse consequences of sepsis. 
	<mark class="hltr-gray" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=SZGXRZWV)

calcitonin, C-reactive protein, white blood cells, platelets, and lactic acid (6, 7). 
	<mark class="hltr-yellow" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=3HGHVLCU)

Since sepsis is a complex clinical syndrome, it contains a wide range of multifaceted clinical and biological features; therefore, a single clinical index may not be a good reflection of the disease state 
	<mark class="hltr-gray" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=RLJG5TY8)

Bloch et al. constructed a sepsis prediction model based on the four vital signs of mean arterial pressure, heart rate, respiratory rate, and body temperature (10). 
	<mark class="hltr-blue" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=FRXTULLM)

The use of machine learning models can improve patient safety, improve the quality of care, and reduce medical costs (20). 
	<mark class="hltr-gray" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=5ER4HKK2)

necessary to identify high-risk patients and may enhance the understanding and facilitate clinical management of sepsis 
	<mark class="hltr-gray" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=JBAJZPLH)

used the random forest algorithm to predict the risk of sepsis in ICU patients by analyzing laboratory/clinic data as follows: (i) lipids, (ii) liver function, (iii) hemagglutination, (iv) blood cells, (v) renal function, and (vi) electrolyte. The essential idea of the random forest algorithm is to build multiple decision trees to reduce the correlation between trees using bootstrap aggregating or bagging, which can avoid the overfitting problem. 
	<mark class="hltr-orange" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=4UCAXBW9)

Gini importance to rank the importance of all potential features (31, 32). 
	<mark class="hltr-orange" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=QH5TPGGP)

-	*Identify the candidate features, then remove irrelevant or redundant features, which may mislead the models.*

It can be observed in Figure 3 that the error value remained at a similar degree when the number of features reached 20. Therefore, we utilized a combination of 20 selected features to predict sepsis in ICU patients (shown in Supplementary Table 3): neutrophils%, D-dimer, neutrophils, eosinophils, lymphocytes, albumin, white blood cells (WBCs), direct bilirubin, potassium, calcium, cholinesterase, magnesium, low-density lipoprotein (LDL), prothrombin time (PT), lymphocytes, lactate dehydrogenase (LDH), basophils%, total cholesterol (TBIL), urea, and platelets (PLT). 
	<mark class="hltr-orange" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=ADJ3PDGD)

![[wangMachineLearningModel2021-4-x47-y318.png]]

![[wangMachineLearningModel2021-4-x46-y64.png]]

-	*Neutrophils %
D-dimer
Neurophils
Eosinophils %
Lymphocytes %
Albumin
White blood cell (WBC)
Direct bilirubin
Potassium
Calcium
Magnesium
LDL*

To our knowledge, most previous studies have developed models to predict the prognosis of sepsis. However, only few researchers have paid attention to the differences in the incidence of sepsis after infection, although it is important for clinical preventive intervention. 
	<mark class="hltr-orange" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=YN3BGN9M)

The variables in our model were mainly blood cells, lipids, liver function, hemagglutination, renal function, electrolyte, enzyme, and others. Interestingly, blood-related variables accounted for a large part of our model; the first five variables in Figure 2 are related to the blood system. 
	<mark class="hltr-orange" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=EB57LJG3)

blood cells, including eosinophils, basophils, lymphocytes, and WBCs, are also associated with the body’s defense against infection 
	<mark class="hltr-yellow" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=3BKXCLGZ)

eosinophilia 
	<mark class="hltr-yellow" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=VSNCSGET)

-	*Distinguishing SIRS from infection*

lymphocyte apoptosis 
	<mark class="hltr-yellow" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=5B5JFN23)

-	*"immune paralysis"*

Platelets are the main effector cells involved in blood coagulation and can promote the development of excessive inflammation, DIC, and microthrombosis (48). PT can reflect the coagulation function of the body, and D-dimer levels increase under hypercoagulable state (49). 
	<mark class="hltr-blue" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=UEBJPP3G)

Albumin which is the most important protein in human plasma, maintains nutrition and osmotic 
	<mark class="hltr-yellow" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=RSYXQI84)

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fpubh. 2021.754348/full#supplementary-material 
	<mark class="hltr-blue" >Highlight</mark> [Page 6](zotero://open-pdf/library/items/?page=6&annotation=6JQR3UQK)

To date, the diagnosis of sepsis has largely relied on determining the presence of infection and organ dysfunction (4). 
	<mark class="hltr-orange" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=highlight-p2x44y684)

To our knowledge, most previous studies have developed models to predict the prognosis of sepsis. However, only few researchers have paid attention to the differences in the incidence of sepsis after infection, although it is important for clinical preventive intervention. 
	<mark class="hltr-orange" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=highlight-p5x44y226)

```dataview
TABLE created, updated as modified, tags, type, related
FROM ""
WHERE contains(related, "wangMachineLearningModel2021")
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