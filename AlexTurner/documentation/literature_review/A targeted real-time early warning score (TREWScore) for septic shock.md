---
tags:
  - 📬
publish: "true"
aliases:
  - A targeted real-time early warning score (TREWScore) for septic shock
  - henryTargetedRealtimeEarly2015
url: https://www.science.org/doi/10.1126/scitranslmed.aab3719
DOI: 10.1126/scitranslmed.aab3719
citekey: henryTargetedRealtimeEarly2015
keywords: [TREWS, risk factor, ✅, keytext, Cox proportional hazards, early warning, high risk]
authors: "[Katharine E. Henry, David N. Hager, Peter J. Pronovost, Suchi Saria]"
type: paper
status: 🟥
created: 
updated:
year: 2015
---



> [!meta]+ Metadata
> zotero_link:: [Henry et al. - 2015 - A targeted real-time early warning score (TREWScor.pdf](zotero://select/library/items/DJTACRAZ)
> abstract:: {(abstract)}
> related:: schinkelArtificialIntelligenceEarly2023
> related:: adamsProspectiveMultisiteStudy2022
> related:: asurogluDeepLearningApproach2021
> related:: amorimAutomatedEarlyWarning2017


![[henryTargetedRealtimeEarly2015-2-x199-y187.png]]

Example patient features and risk trajectory. (A) Example features over time are shown for a patient developing septic shock (time of shock onset indicated by the red line). Point in time data used to calculate TREWScore are displayed in the black box, along with the associated time to onset and the onset of sepsis-related organ dysfunction (indicated by the blue line). Feature measurements are indicated by circles that are filled for new observations or hollow otherwise. Features displayed are Glasgow Coma Scale (GCS), platelets, ratio of blood urea nitrogen to creatinine (BUN/creatinine), arterial pH, temperature, bicarbonate, respiratory rate (RR), white blood cell count (WBC), heart rate/systolic blood pressure (SBP) (shock index),SBP,andheartrate.(B) The TREWScore over time for the patient in (A) is shown in blue. Risk predictions are made as new measurements are added to the EHR, as if in real time. The horizontal dashed gray line indicates the detection threshold corresponding to a sensitivity of 0.85. The figure portrays two sets of potential detection criteria: (i) Identify the patient as at high risk of septic shock the first time the risk score crosses the detection threshold. (ii) Identify the patient only after the risk score remains above the detection threshold for at least 8 hours or some other desired length of time. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=EKAMBD5E)

the MIMIC-II database, albeit large, reflects patients admitted to the Beth Israel Deaconess Medical Center between 2001 and 2007 (40); additional validation with data from other hospitals is needed. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=I9TSS3HR)

-	*Limitations*

Third, some of the features in the model are defined by ICD-9 (International Classification of Diseases, Ninth Revision) codes. The sensitivity and specificity of these codes are very diagnosis-dependent (52). For example, one study found that ICD-9 codes for severe sepsis and septic shock were undercoded among patients admitted to the hospital with a confirmed diagnosis of severe sepsis or septic shock (53). Moreover, coding practices were biased to more frequently code more severe cases (53). This limitation can often be overcome by extracting diagnosis-related information from the discharge notes using automated techniques (54). 
	<mark class="hltr-yellow" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=PCAHMCWI)

-	*Limitations of diagnostic criteria*

(i) patient-specific measurement streams were processed to compute features (candidate risk factors); and (ii) the coefficients used in the targeted early warning score were estimated using a supervised learning algorithm. The learning algorithm automatically selected thefeaturesthatwerepredictiveofsepticshock,andtheresultingoutput was a model containing the list of predictive features and their coefficients. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 6](zotero://open-pdf/library/items/?page=6&annotation=5G4DLVWP)

-	*Model development*

To develop a model for predicting an individual’s risk of developing septic shock, we fit a Cox proportional hazards model using the time until the onset of septic shock as the supervisory signal. Intuitively, this approach assumes that at times approaching the onset of shock, the sepsis severity level is worse than at times well before the onset. The risk of shock at a time t given the features X at that time, denoted by l(t|X), is computed from two parts: a time-varying baseline hazard function, l0, that computes the instantaneous probability that the onset of septic shock occurs at time t and a second term that weights an individual’s feature values at time t by learned regression coefficients b (see equation below) (56). lðtjX Þ¼l0ðtÞ expfX bT g A key challenge with training this model is the presence of unknown or censored event times (38, 39). Censoring occurs in two ways. Clinical interventions may influence the observed time of septic shock by delayingtheonsetofsepticshock(intervalcensoring)orbypreventingthe development of septic shock entirely (right censoring after treatment). 
	<mark class="hltr-yellow" >Highlight</mark> [Page 6](zotero://open-pdf/library/items/?page=6&annotation=WFUW2W6V)

-	*Model development - estimating model coefficients*

Whereas right censoring after treatment is naturally accounted for by the Cox proportional hazards model, the model does not a priori account for interval censoring. Model parameter estimation for the Cox proportional hazards model in the presence of interval censoring has been addressed using the expectation-maximization algorithm (57) and multiple imputation–based approaches (56). Here, we used the latter because this approach was much less computationally intensive and simpler to implement using available software. The multiple imputation approach handles censoring by imputing multiple copies of the development data set. On the subjects for whom the time to event is interval-censored, this approach imputes the exact event time within each copy by sampling from the estimated baseline hazard function (56). Each copy is analyzed separately, and then the results are combined using Rubin’sequations(58). To impute the exact event times for each copy, the baseline hazard function was fit using a multiple imputation method (MIICD R package, version 2.0). For computational efficiency, the baseline hazard function was estimated from a subset of 400,000 time-to-event and feature pairs from the development set (59). The resulting baseline hazard function was then used to repeatedly sample the event time for each interval-censored sample and generate N complete copies of the development data set. Individual copies differ only in the imputed event times. For our experiments, we set N = 100. A separate model was trained from each of the N copies of the development data set. Individual time-to-event models were learned as a Cox proportional hazards model with lasso regularization (glmnet R package, version 1.9-8) (60, 61). Using lasso regularization causes the model to automatically select a sparse subset of features that are most predictive of the labeled outcome (62). The regularization parameter, which controls the degree of parsimony in the learned model, was determined to be 0.01 using 10-fold cross-validation on the first sampled data set and was fixed to this value for training the subsequent models. To predict on data from a new subject, predicted risk values were obtained from each of the N models. The resulting predictions were then combined using Rubin’s equations, which compute the final risk value as the average of risk values outputted from each of the N models (56, 58). Combining the Cox proportional hazards model with the multiple imputation approach allows the model to incorporate information from both interval- and right-censored patients. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 7](zotero://open-pdf/library/items/?page=7&annotation=Q4AM3Q8T)

-	*Cox proportional hazards model methods*

www.sciencetranslationalmedicine.org/cgi/content/full/7/299/299ra122/DC1 Materials and Methods Table S1. Sample feature coefficients learned by TREWScore for a single imputation of the development data set. 
	<mark class="hltr-blue" >Highlight</mark> [Page 7](zotero://open-pdf/library/items/?page=7&annotation=S6R5VPKV)

```dataview
TABLE created, updated as modified, tags, type, related
FROM ""
WHERE contains(related, "henryTargetedRealtimeEarly2015")
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