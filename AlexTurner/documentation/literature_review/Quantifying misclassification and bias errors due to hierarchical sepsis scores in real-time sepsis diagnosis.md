---
tags:
  - 📬
publish: "true"
aliases:
  - Quantifying misclassification and bias errors due to hierarchical sepsis scores in real-time sepsis diagnosis
  - parenteQuantifyingMisclassificationBias2020
url: https://linkinghub.elsevier.com/retrieve/pii/S174680942030269X
DOI: 10.1016/j.bspc.2020.102116
citekey: parenteQuantifyingMisclassificationBias2020
keywords: [Diagnostic Errors, ✅, sepsis, ICU, bias, misclassification, real-time, limitations]
authors: "[Jacquelyn D. Parente, J. Geoffrey Chase, Knut Moeller, Geoffrey M. Shaw]"
type: paper
status: 🟥
created: 
updated:
year: 2020
---



> [!meta]+ Metadata
> zotero_link:: [Parente et al. - 2020 - Quantifying misclassification and bias errors due .pdf](zotero://select/library/items/EBWXXVCL)
> abstract:: {(abstract)}


Systemic inflammatory response syndrome (SIRS) is common in intensive care unit (ICU) patients, diagnosed when two or more of altered temperature, heart rate, respiratory rate, and white blood cell count are present [1–4]. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=2G7RXTDW)

cell cultures take 24–48 h to return a result, limiting rapid diagnosis, and are not necessarilyspecific or reliable. Thus, ~50 % of sepsis cases diagnosed are “culture negative” [10–12]. 
	<mark class="hltr-blue" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=YH82YXYP)

no single or combined sets of signals providing good accuracy and minimum false positives. 
	<mark class="hltr-red" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=YQVLC27H)

if the SIRS score symptoms are successfully treated, then the diagnosis of sepsis can “disappear”, even when it is clear, hour-to-hour, the infection and organ failure, and thus severe sepsis or worse, remain. 
	<mark class="hltr-green" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=6ERSRQST)

creates a continuous, non-hierarchical sepsis score for hour-to-hour assessment using the same sepsis definition as the hierarchical scores commonly used [4,14,15] in a less continuous more intermittent fashion [29]. 
	<mark class="hltr-orange" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=Z5PPJZMD)

Clinical data comprises hourly measures of: a) model-basedinsulin sensitivity (SI) [32–34]; SIRS score; heart rate; temperature; systolic and diastolic blood pressure; and respiratory rate. SI is a proven metabolic metric in clinical use, diabetes diagnosis and a rangeof other studies showing it reflects patient-specific inflammatory and sepsis state although not to high diagnostic quality levels desired [35–38]. SI is identified from hourly data on insulin and nutrition given, and blood glucose measurements [39,40], and is highly correlated to the state and evolution of metabolic and physiological response [41–45]. 
	<mark class="hltr-blue" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=X8ANX8ET)

![[parenteQuantifyingMisclassificationBias2020-3-x26-y570.png]]

A KDE classifier using a modified sepsis score of Table 1 is used to classify or discriminate cases and controls. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 7](zotero://open-pdf/library/items/?page=7&annotation=3AGSVDEH)

However, the reality of gold standard diagnostics in sepsis, as well as other clinical areas of ICU medicine, require modified or all-new classification or gold-standard metrics [62]. In particular, using positive blood culture results provides a solid classification of infection and thus sepsis, but is not timely enough for early diagnosis and treatment nor accurate enough, resulting in potentially high false positive and false negative rates leading to “culture negative” sepsis diagnoses [10–12] along with ambiguous clinical classifications, which impacts the results of any classifier or diagnostic. This issue, in turn, returns the burden of decision making on clinical inference and experience. There is thus a need for better clinical metrics and gold standards to assess emerging diagnostic methods, as shown here in one example, especially for sepsis where the presence/absence of infection does not yet have a reliable real-time biomarker at this time [24,25,63]. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 9](zotero://open-pdf/library/items/?page=9&annotation=A9UMEJIK)

The issue of ambiguous classification can play an important role and be a majorbias in results.Omitting data which is ambiguous can prevent further misclassification bias [64]. However, it introduces an alternative problem of case-control bias, which has also been identified as a po tential source of overestimation of test accuracy [65]. There are thus competing sources of potential bias in howthe data is managed resulting from the difficulty of classifying sepsis unambiguously, which limits all work in this fieldand is oftennot addressed in discussion of other results and studies. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 9](zotero://open-pdf/library/items/?page=9&annotation=CHA42EWN)

Most clinicians can distinguish between a severely ill patient with suspected sepsis and a healthy control patient without added testing. However, it is solely to remove ambiguity that clinicians seek help from test results to segregate cases and controls. Hence, any classifier faces a potentially limited maximum it can obtain in terms of performance and perfection in a test is unlikelygiven the ambiguity and biases described, which are not able to be mitigated by methods alone at this time. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 9](zotero://open-pdf/library/items/?page=9&annotation=RL83GL4E)

Overall, the results of this study and its methodology show a clear tradeoff between misclassification bias and case control bias due to the lack of a true gold standard metric. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 9](zotero://open-pdf/library/items/?page=9&annotation=QB66D2JC)

Diagnostic performance and quality was assessed using ROC curves, diagnostic odds ratios, sensitivity/specificity, and likelihood ratios for resubstitution (best case), bootstrap (worst case), and .632 bootstrap (expected case) estimates. Considering the expected case test performance, the classifier developed provided good to very good results, potentially able to change clinical decisions, but were not at the highest level of diagnostic accuracy desired for all performance metrics considered. Finally, the results also illustrated more general issues and outcomes related to the development and testing of such computational sepsis diagnostics. In particular, the wide range of quality and performance metrics provided robustness in the ability to assess the potential of the estimator that any one or two metrics could not, avoiding bias in assessing the classifier overall. Likelihood ratios are seen to be a better choice for assessing sepsis diagnostics and classifiers as clinical decision making in sepsis relies on similar odds in making inferences on the presence (or absence) of infection and thus on how treatment should progress. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 9](zotero://open-pdf/library/items/?page=9&annotation=9LNXA27Q)

creates a continuous, non-hierarchical sepsis score for hour-to-hour assessment using the same sepsis defnition as the hierarchical scores commonly used [4,14,15] in a less continuous more intermittent fashion [29]. 
	<mark class="hltr-orange" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=highlight-p2x306y697)

```dataview
TABLE created, updated as modified, tags, type, related
FROM ""
WHERE contains(related, "parenteQuantifyingMisclassificationBias2020")
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