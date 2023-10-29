However, the accuracy-interpretability trade-off6,7 in ML is still an open research challenge, where model complexity is directly proportional to higher accuracy, but inversely proportional with human-interpretability. Examples of these can also be seen in sepsis detection8–27. As a result, even though ML has greatly advanced healthcare data analysis28–35, computational healthcare studies (including sepsis detection8–11,30,36) often choose statistics, intrinsically interpretable ML models and/or feature selection methods for analysis, instead of stateof-the-art ML models with higher accuracy. Moreover, there is no guarantee that local explanation provided (via post-hoc analysis using LIME37/SHAP38,39) for one instance in the dataset will be the same for a different instance in the same dataset, even if they share the class membership. As such, features obtained from local explanations will not be a good representation of the additional relevant features needed for timely sepsis detection. Thus, global interpreter for state-of-art-model is essential because it can aid the task of identifying relevant sepsis factors. Moreover, a global interpreter allows black-box models to retain their high accuracy, while becoming more transparent to human beings. Various works have addressed the challenge of creating global interpreters, and some notable examples include40

#interpretability
#local-features
#global-features


Accuracy-interpretability trade-off in machine learning
A more complex model may provide a greater accuracy, however it will be less likely to be interpreted by the healthcare worker. 
"computational healthcare studies (including sepsis detection8–11,30,36) often choose statistics, intrinsically interpretable ML models and/or feature selection methods for analysis, instead of stateof-the-art ML models with higher accuracy."
