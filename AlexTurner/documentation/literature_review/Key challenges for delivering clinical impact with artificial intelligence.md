---
tags:
  - 📬
publish: "true"
aliases:
  - Key challenges for delivering clinical impact with artificial intelligence
  - kellyKeyChallengesDelivering2019
url: https://bmcmedicine.biomedcentral.com/articles/10.1186/s12916-019-1426-2
DOI: 10.1186/s12916-019-1426-2
citekey: kellyKeyChallengesDelivering2019
keywords: [interpretability, complexity, clinical data, benefits, explainable, ✅, guidelines, challenges, blackbox, keytext, responsible, generalisation, bias, unfairness, evaluation, regulation, safe use, ethics, consequences]
authors: "[Christopher J. Kelly, Alan Karthikesalingam, Mustafa Suleyman, Greg Corrado, Dominic King]"
type: paper
status: 🟥
created: 
updated:
year: 2019
---



> [!meta]+ Metadata
> zotero_link:: [Kelly et al. - 2019 - Key challenges for delivering clinical impact with.pdf](zotero://select/library/items/ZFLGYVDC)
> abstract:: {(abstract)}


his promise has been welcomed as healthcare systems globally struggle to deliver the ‘quadruple aim’, namely improving experience of care, improving the health of populations, reducing per capita costs of healthcare [3], and improving the work life of healthcare providers [4]. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=HE5TTJNQ)

his promise has been welcomed as healthcare systems globally struggle to deliver the ‘quadruple aim’, namely improving experience of care, improving the health of populations, reducing per capita costs of healthcare [3], and improving the work life of healthcare providers [4]. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 1](zotero://open-pdf/library/items/?page=1&annotation=BK4NR4GT)

AI systems have the potential to reduce unwarranted variation in clinical practice, improve efficiency and prevent avoidable medical errors that will affect almost every patient during their lifetime [43]. By providing novel tools to support patients and augment healthcare staff, AI could enable better care delivered closer to the patient in the community. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=GWX62XKN)

-	*Benefits*

Retrospective versus prospective studies While existing studies have encompassed very large numbers of patients with extensive benchmarking against expert performance, the vast majority of studies have been retrospective, meaning that they use historically labelled data to train and test algorithms. Only through prospective studies will we begin to understand the true utility of AI systems, as performance is likely to be worse when encountering real-world data that differ from that encountered in algorithm training. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=2C7CAC4V)

Retrospective versus prospective studies 
	<mark class="hltr-yellow" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=TKLX2ESJ)

the vast majority of studies have been retrospective, meaning that they use historically labelled data to train and test algorithms. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=LKWZZT4X)

Peer-reviewed evidence will be important for the trust and adoption of AI within the wider medical community. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 2](zotero://open-pdf/library/items/?page=2&annotation=GCSGTEYI)

Metrics often do not reflect clinical applicability 
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=SBYD46FL)

accuracy does not necessarily represent clinical efficacy [65]. Despite its universal use in machine learning studies, area under the curve of a receiver operating characteristic curve is not necessarily the best metric to represent clinical applicability [66] and is not easily understandable by many clinicians. As well as reporting sensitivity and specificity at a selected model operating point (required to turn the continuous model output into discrete decision categories), papers should include information about positive and negative predictive values. 
	<mark class="hltr-green" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=26TMZBYE)

Difficulty comparing different algorithms 
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=7KEHP2GG)

To make fair comparisons, algorithms need to be subjected to comparison on the same independent test set that is representative of the target population, using the same performance metrics. Without this, clinicians will have difficulty in determining which algorithm is likely to perform best for their patients. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=BVDEYJLK)

Challenges related to machine learning science AI algorithms have the potential to suffer from a host of shortcomings, including inapplicability outside of the training domain, bias and brittleness (tendency to be easily fooled) [69]. Important factors for consideration include dataset shift, accidentally fitting confounders rather than true signal, propagating unintentional biases in clinical practice, providing algorithms with interpretability, developing reliable measures of model confidence, and the challenge of generalisation to different populations. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=3ZLNRKN3)

Dataset shift 
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=Y5FZY7Q9)

Particularly important for EHR algorithms, it is easy to ignore the fact that all input data are generated within a non-stationary environment with shifting patient populations, where clinical and operational practices evolve over time [70]. The introduction of a new predictive algorithm may cause changes in practice, resulting in a new distribution compared to that used to train the algorithm. Therefore, methods to identify drift and update models in response to deteriorating performance are critical. Mitigations to manage this effect include careful quantification of performance over time to proactively identify problems, alongside the likely requirement for periodical retraining. Data-driven testing procedures have been suggested to recommend the most appropriate updating method, from simple recalibration to full model retraining, in order to maintain performance over time [71]. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=NEF29QRI)

Particularly important for EHR algorithms, it is easy to ignore the fact that all input data are generated within a non-stationary environment with shifting patient populations, where clinical and operational practices evolve over time [70]. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 3](zotero://open-pdf/library/items/?page=3&annotation=S6LNE4KW)

Accidentally fitting confounders versus true signal 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=N7Z6XSC9)

exploitation of unknown confounders that may not be reliable, impairing the algorithm’s ability to generalise to new datasets. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=J54PJEJ9)

Challenges in generalisation to new populations and settings 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=MN7AQIRZ)

Generalisation can be hard due to technical differences between sites (including differences in equipment, coding definitions, EHR systems, and laboratory equipment and assays) as well as variations in local clinical and administrative practices. 
	<mark class="hltr-green" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=R6S4NIYE)

To overcome these issues, it is likely that a degree of site-specific training will be required to adapt an existing system for a new population, particularly for complex tasks like EHR predictions. Methods to detect out-ofdistribution inputs and provide a reliable measure of model confidence will be important to prevent clinical decisions being made on inaccurate model outputs. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=A4ELLJHJ)

Proper assessment of real-world clinical performance and generalisation requires appropriately designed external validation involving testing of an AI system using adequately sized datasets collected from institutions other than those that provided the data for model training. This will ensure that all relevant variations in patient demographics and disease states of target patients in real-world clinical settings are adequately represented in the system where it will be applied [76]. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=AQM99UD6)

Proper assessment of real-world clinical performance and generalisation requires appropriately designed external validation involving testing of an AI system using adequately sized datasets collected from institutions other than those that provided the data for model training. This will ensure that all relevant variations in patient demographics and disease states of target patients in real-world clinical settings are adequately represented in the system where it will be applied [76]. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=PABIQ5CU)

Algorithmic bias 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=UU2267ZL)

Algorithmic bias 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=DQPTBW2Z)

Intertwined with the issue of generalisability is that of discriminatory bias. Blind spots in machine learning can reflect the worst societal biases, with a risk of unintended or unknown accuracies in minority subgroups, and there is fear over the potential for amplifying biases present in the historical data [78]. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=9Y3RNX85)

ntertwined with the issue of generalisability is that of discriminatory bias. Blind spots in machine learning can reflect the worst societal biases, with a risk of unintended or unknown accuracies in minority subgroups, and there is fear over the potential for amplifying biases present in the historical data [78]. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=6KCMKCZZ)

Algorithmic unfairness can be distilled into three components, namely (1) model bias (i.e. models selected to best represent the majority and not necessarily underrepresented groups), (2) model variance (due to inadequate data from minorities), and (3) outcome noise (the effect of a set of unobserved variables that potentially interacts with model predictions, avoidable by identifying subpopulations to measure additional variables) [80]. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=48D7HPK3)

Algorithmic unfairness can be distilled into three components, namely (1) model bias (i.e. models selected to best represent the majority and not necessarily underrepresented groups), (2) model variance (due to inadequate data from minorities), and (3) outcome noise (the effect of a set of unobserved variables that potentially interacts with model predictions, avoidable by identifying subpopulations to measure additional variables) [80]. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=4TMHHMZQ)

Algorithms should be designed with the global community in mind, and clinical validation should be performed using a representative population of the intended deployment population. Careful performance analysis by population subgroups should be performed, including age, ethnicity, sex, sociodemographic stratum 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=AES8DXMS)

Careful performance analysis by population subgroups should be performed, including age, ethnicity, sex, sociodemographic stratum 
	<mark class="hltr-yellow" >Highlight</mark> [Page 4](zotero://open-pdf/library/items/?page=4&annotation=JX4ZX869)

Analysis to understand the impact of a new algorithm is particularly important, i.e. if the spectrum of disease detected using the AI system differs from current clinical practice, then the benefits and harms of detecting this different spectrum of disease must be evaluated. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=IZZHZNJ8)

Susceptibility to adversarial attack or manipulation 
	<mark class="hltr-yellow" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=DFST5CMV)

Logistical difficulties in implementing AI systems 
	<mark class="hltr-yellow" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=94AELPR9)

Achieving robust regulation and rigorous quality control 
	<mark class="hltr-yellow" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=CF8DFQSM)

Human barriers to AI adoption in healthcare 
	<mark class="hltr-yellow" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=4L96VSMM)

Algorithmic interpretability is at an early stage but rapidly advancing 
	<mark class="hltr-yellow" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=4VVY2IUK)

While AI approaches in medicine have yielded some impressive practical successes to date, their effectiveness is limited by their inability to ‘explain’ their decision-making in an understandable way [87]. 
	<mark class="hltr-green" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=5FLLD3ZV)

limited by their inability to ‘explain’ their decision-making in an understandable way [87]. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=LB2IHCJP)

Healthcare offers one of the strongest arguments in favour of explainability [88,89]. Given the combination of the devastating consequences of unacceptable results, the high risk of unquantified bias that is difficult to identify a priori, and the recognised potential for models to use inappropriate confounding variables, explainability enables system verification. This improves experts’ ability to recognise system errors, detect results based upon inappropriate reasoning, and identify the work required to remove bias. In addition, AI systems are trained using large numbers of examples and may detect patterns in data that are not accessible to humans. 
	<mark class="hltr-green" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=EIXPVN65)

Given the combination of the devastating consequences of unacceptable results, the high risk of unquantified bias that is difficult to identify a priori, and the recognised potential for models to use inappropriate confounding variables, explainability enables system verification. This improves experts’ ability to recognise system errors, detect results based upon inappropriate reasoning, and identify the work required to remove bias. In addition, AI systems are trained using large numbers of examples and may detect patterns in data that are not accessible to humans. Interpretable systems may allow humans to extract this distilled knowledge in order to acquire new scientific insights. Finally, recent European Union General Data Protection Regulation legislation mandates a ‘right to explanation’ for algorithmically generated user-level predictions that have the potential to ‘significantly affect’ users; this suggests that there must be a possibility to make results re-traceable on demand 
	<mark class="hltr-yellow" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=T7AVE6VK)

recent European Union General Data Protection Regulation legislation mandates a ‘right to explanation’ for algorithmically generated user-level predictions that have the potential to ‘significantly affect’ users; this suggests that there must be a possibility to make results re-traceable on demand [88]. 
	<mark class="hltr-green" >Highlight</mark> [Page 5](zotero://open-pdf/library/items/?page=5&annotation=8X7F87EH)

At present, a trade-off exists between performance and explainability. The best performing models (e.g. deep learning) are often the least explainable, whereas models with poorer performance (e.g. linear regression, decision trees) are the most explainable. A key current limitation of deep learning models is that they have no explicit declarative knowledge representation, leading to considerable difficulty in generating the required explanation structures [90]. Machine learning methods that build upon a long history of research in traditional symbolic AI techniques to allow for encoding of semantics of data and the use of ontologies to guide the learning process may permit human experts to understand and retrace decision processes more effectively [91,92]. One recent approach replaced end-to-end classification with a twostage architecture comprising segmentation and classification, allowing the clinician to interrogate the segmentation map to understand the basis of the subsequent classification [24]. If ‘black box’ algorithms are to be used in healthcare, they need to be used with knowledge, judgement and responsibility. In the meantime, research into explainable AI and evaluation of interpretability is occurring at a rapid pace [93]. Explainable AI approaches are likely to facilitate faster adoption of AI systems into the clinical healthcare setting, and will help foster vital transparency and trust with their users 
	<mark class="hltr-yellow" >Highlight</mark> [Page 6](zotero://open-pdf/library/items/?page=6&annotation=K9IQLK6Q)

Machine learning methods that build upon a long history of research in traditional symbolic AI techniques to allow for encoding of semantics of data and the use of ontologies to guide the learning process may permit human experts to understand and retrace decision processes more effectively [91,92]. O 
	<mark class="hltr-magenta" >Highlight</mark> [Page 6](zotero://open-pdf/library/items/?page=6&annotation=I4UTIB23)

Developing a better understanding of interaction between human and algorithm 
	<mark class="hltr-green" >Highlight</mark> [Page 6](zotero://open-pdf/library/items/?page=6&annotation=8KA739CY)

evaluation will be essential to ensure that AI systems are safe and effective, using clinically applicable performance metrics that go beyond measures of technical accuracy to include how AI affects the quality of care, the variability of healthcare professionals, the efficiency and productivity of clinical practice and, most importantly, patient outcomes. Independent datasets that are representative of future target populations should be curated to enable the comparison of different algorithms, while carefully evaluating for signs of potential bias and fitting to unintended confounders. Developers of AI tools must be cognisant of the potential unintended consequences of their algorithms and ensure that algorithms are designed with the global community in mind. Further work to improve the interpretability of algorithms and to understand human–algorithm interactions will be essential to their future adoption and safety supported by the development of thoughtful regulatory frameworks. 
	<mark class="hltr-red" >Highlight</mark> [Page 6](zotero://open-pdf/library/items/?page=6&annotation=HGWEB5C7)

Nestor B, McDermott MBA, Chauhan G, Naumann T, Hughes MC, Goldenberg A, et al. Rethinking clinical prediction: why machine learning must consider year of care and feature aggregation. In: Machine Learning for Health (ML4H): NeurIPS; 2018. https://arxiv.org/abs/1811.12583. Accessed 1 May 2019. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 8](zotero://open-pdf/library/items/?page=8&annotation=KP955U7Z)

Chen IY, Johansson FD, Sontag D. Why Is My Classifier Discriminatory? In: 32nd Conference on Neural Information Processing Systems (NeurIPS). 2018. http://papers.nips.cc/paper/7613-why-is-my-classifier-discriminatory.pdf. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 8](zotero://open-pdf/library/items/?page=8&annotation=46RYQM53)

Core MG, Lane HC, van Lent M, Gomboc D, Solomon S, Rosenberg M. Building Explainable Artificial Intelligence Systems. IAAI'06 Proceedings of the 18th conference on Innovative Applications of Artificial Intelligence. Volume 2; 2006. p. 1766–73. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 8](zotero://open-pdf/library/items/?page=8&annotation=X4TI725A)

Holzinger A, Biemann C, Pattichis CS. What do we need to build explainable AI systems for the medical domain? arXiv. 2017; https://arxiv.org/abs/1712.09923. Accessed 1 May 2019. 89. Samek W, Wiegand T, Müller K-R. Explainable artificial intelligence: understanding, visualizing and interpreting deep learning models. arXiv. 2017; http://arxiv.org/abs/1708.08296. Accessed 1 May 2019. 
	<mark class="hltr-yellow" >Highlight</mark> [Page 8](zotero://open-pdf/library/items/?page=8&annotation=5KC66KQA)

```dataview
TABLE created, updated as modified, tags, type, related
FROM ""
WHERE contains(related, "kellyKeyChallengesDelivering2019")
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