
Project folder structure:
* [USE THIS](https://drivendata.github.io/cookiecutter-data-science/)
	* [following project organisation](https://github.com/chop-dbhi/sepsis_01#project-organization)


* https://docs.python.org/3/library/pathlib.html#basic-use
* https://stackoverflow.com/questions/25389095/python-get-path-of-root-project-structure


Indexing:
* For chart_events:
	* HeartRate_Min and RespRate_Min
	* https://github.com/MIT-LCP/mimic-code/blob/main/mimic-iii/benchmark/README.md#benchmark

Time: 
* Extracted the mean, standard deviation, and skew from each of these 3-hour fragments and included them as inputs for training.

Plot first labs of each item ID:
* https://github.com/MIT-LCP/mimic-code/blob/main/mimic-iii/notebooks/first_labs.ipynb

Creating summary statistics with _tableone_
* https://github.com/MIT-LCP/mimic-code/blob/main/mimic-iii/notebooks/tableone-demo.ipynb 

Cohort selection:
* https://github.com/MIT-LCP/mimic-code/blob/main/mimic-iii/tutorials/cohort-selection.ipynb

Sepsis selection:
* https://github.com/MIT-LCP/mimic-code/blob/main/mimic-iii/concepts/sepsis/angus.sql
* [Sirs](https://github.com/MIT-LCP/mimic-code/blob/78f7b6e5a8886f52066b0505c451597590bea862/mimic-iii/concepts/severityscores/sirs.sql)
	* Body temperature (min and max),  Heart rate (max),  Respiratory rate (max),  PaCO2 (min),  White blood cell count (min and max), the presence of greater than 10% immature neutrophils (band forms)
* [qSOFA](https://github.com/MIT-LCP/mimic-code/blob/78f7b6e5a8886f52066b0505c451597590bea862/mimic-iii/concepts/severityscores/qsofa.sql)
	* variables: GCS, respiratory rate, systolic blood pressure
* [mLODS](https://github.com/MIT-LCP/mimic-code/blob/78f7b6e5a8886f52066b0505c451597590bea862/mimic-iii/concepts/severityscores/mlods.sql)
* Variables: GCS,  VITALS: Heart rate, systolic blood pressure, FLAGS: ventilation/cpap,  LABS: WBC, bilirubin, creatinine, platelets,  ABG: PaO2 with associated FiO2


Consider exclusion criteria:
* age
* presented in the ICU for less than 4 hours


## Missing data:
* Static variables (age, height, weight, BMI)
	* mode imputation for outliers / missing values
* dynamic variables
	* forward filling interpolation 
* Key identifiers
	* drop HADM_ID

## Descriptive statistics of sepsis patients:
Demographic, Mean +/- S.D. 


## Evaluation
ROC and stacked bar chart:
https://github.com/MIT-LCP/mimic-code/blob/main/mimic-iii/notebooks/aline-aws/aline_propensity_score.ipynb 

## Model analysis
* https://github.com/chop-dbhi/sepsis_01/blob/master/sepsis/model_analsyis.py



!!!!!
[Pipeline for Hyperparameter generation](https://github.com/MLforHealth/MIMIC_Extract/blob/master/notebooks/Baselines%20for%20Intervention%20Prediction%20-%20Vasopressor.ipynb)

[Parameter optimisation](https://github.com/javiersgjavi/sepsis-review/blob/main/src/classes/ParameterOptimization.py)


https://github.com/YerevaNN/mimic3-benchmarks/blob/master/statistics.md#phenotype-classification 


[XGBoost code](https://github.com/acampillos/sepsis-prediction/blob/master/src/experiments/xgboost_experiments.py)


[No code, but description of process:](https://www.nature.com/articles/s41467-021-20910-4#Sec10):
* SMOTE
* NLP Topic modelling (processing of clinical notes)


[NLP Code](https://github.com/Sapphirine/real-time-sepsis-prediction/blob/master/Feature%20Generation%20-%20Combined.ipynb)

[nan_interpolate and forward fill ](https://github.com/jambo6/physionet_sepsis_challenge_2019/blob/e626f093320d12cd50f4264539bdc9852e5fdda6/src/features/transformers.py#L439C1-L463C16)
