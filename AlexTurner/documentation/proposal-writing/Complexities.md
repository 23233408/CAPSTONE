






## Aim

The model operates on time series data and predicts the probability of a patient developing sepsis based on the historical medical data of the patient



* The aim is to create a continuous, non-hierarchical sepsis score for hour-to-hour assessment using the same sepsis definition as the hierarchical scores commonly used [4,14,15] in a less continuous more intermittent fashion [29].” 

## Background

Sepsis is a life-threatening condition with high mortality rates. Early detection and treatment are critical to improving patient outcomes. Our primary objective is to develop a machine learning model capable of predicting the onset of sepsis earlier, using a minimal set of streaming physiological data in real time.

Sepsis is among the leading causes of death in hospitals, including at Royal Perth Hospital. Delays in treatment can significantly increase the risk for multi-organ dysfunction and ultimately death. Critically ill patients admitted to the intensive care unit (ICU) are monitored for acute physiological deterioration by bedside monitors that produce substantial amounts of data, the analysis of which can reveal important “physiomarkers” that predict the onset of sepsis. 


A number of predictive algorithms have been developed to identify patients at risk for sepsis using electronic medical record data. These methods often employ time-delayed variables, that can take several hours to become available for clinical decision making, 

While effective in sepsis analysis retrospectively, these present challenges when applied to aid real-time decision support for the patient. 

We will aim to develop a predictive model using a minimal set of automatically captured continuous physiological sensor data in order to identify the onset of sepsis. 

We implemented the Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3) criteria to identify sepsis cases and then used machine learning methods to extract features and apply a Support Vector Machine (SVM) classifier to predict the onset of sepsis earlier than clinical suspicion.



**Standard clinical variables for sepsis diagnosis**


* Patients in the ward are generally stable and may be recovering from surgeries, receiving treatment for chronic conditions, or being monitored for less severe illnesses. The care provided in the ward is focused on maintaining stability, managing symptoms, and providing routine medical care.




## Prior prediction & treatment
* Alternate scoring systems


There are standard clinical variables that have been used for sepsis diagnosis. There are also clinical variables for sepsis diagnosis, highlighted from various academic studies.

The clinical diagnosis scoring ranges are:
* Systemic Inflammatory Response Syndrome (SIRS) Criteria (range, 0-4 criteria)
* Quick Sequential [Sepsis related] Organ Failure Assessment (qSOFA) (Range, 0-3 points)
* Sequential [sepsis-related] organ failure assessment (SOFA) (Range, 0-24 points)

-----


“Various disease scoring systems and diagnostic criteria are used in hospitals to identify patients with sepsis [17,18]. Systemic Inflammatory Response Syndrome (SIRS) is one of the first sepsis diagnostic criteria [19,20]. The Third International Consensus Definitions for Sepsis (Sepsis-3) is a redefinition of sepsis introduced in 2016 that emphasises the lethal nature of sepsis if not immediately recognised, compared to that of a straightforward infection. 

This definition emphasizes the priority of the non-homeostatic host response to infection, the possible lethality that is hugely over a straightforward infection, and the need for instant recognition. 
The Sequential Organ Failure Assessment (SOFA) scoring system is used to track a person’s status during the ICU to determine the gamut of a person’s organ function or failure rate in Sepsis-3 guidelines. This predominant score is based on six different ratings: the mean arterial pressure, serum glucose, bilirubin, PaO2/FiO2 ratio, platelets, and creatinine. In the SOFA scoring system, an acute change higher than two or more points in the total SOFA score can indicate organ failure consequent to the infection. A higher SOFA score is correlated with an increase in the probability of mortality [21].” ([Rafiei et al., 2021, p. 2]

## **Complexities** 
### Data leakage

* Train the model only on information that would have been available before the onset of sepsis for each patient

**Survivorship Bias:** If you only include data from patients who survived sepsis, your model might learn features that are unique to survivors but not relevant for early detection. This bias can lead to poor performance on new data where not all patients survive.

**Time-Dependent Variables:** If you include variables that can change over time (like medications administered), your model might "see into the future" by using information that isn't available during prediction.


The amount of data is limited. Therefore, the train-test split of data faces a trade off, for avoiding overfitting. Hence, careful considerations has to be taken into account for efficient sampling. 

### Handling multimodal data 
- The dataset contains a mix of structured data
- relative weights of these
- Some health diagnoses can be made on a single lab value or a single threshold, however 
	- A clinical diagnoses of sepsis is based on a constellation of the signs, symptoms and lab values. Oftentimes these clinical diagnoses are based on additive scoring systems that requires an admixture of positive and negative hallmarks prior to confirmatory labeling.

### Missing values
* Missing ICD-9 codes
	* T-sne for clustering

### Imbalanced dataset
* splitting dataset
	* Performance evaluation
	* At the patient encounter level, the prevalence of sepsis in our case-control sample is 6.15%, which is equivalent to the estimated sepsis’s prevalence of around 6% in hospitals[19](https://www.nature.com/articles/s41467-021-20910-4#ref-CR19). We utilised 
		* we applied the synthetic minority over-sampling technique (SMOTE) to achieve 1:1 balanced data for sepsis cases and non-sepsis controls (at the clinical note level).
		* For comparative purposes, we also develop, test, and report the models without any oversampling to present the possibility of operating this algorithm in a normal clinical environment where the prevalence of sepsis is relatively low
	* SMOTE (oversampling instead of undersampling)
	* The amount of data is limited. Therefore, the train-test split of data faces a trade off, for avoiding overfitting. Hence, careful considerations has to be taken into account for efficient sampling.


* The overall recommendation in clinical suspicion of infection is to use the SOFA score of two or more points for patients in ICU




### Missing data 
* Multiple multivariable imputations were utilised for addressing missing data to maximise statistical power and minimise bias.
  * Identify general characteristics of sepsis in MIMIC-III dataset
  * 50-60% of sepsis cases are missed in clinical coding - Missing ICD-9 codes
  * misclassification and missed diagnosis


* “if the SIRS score symptoms are successfully treated, then the diagnosis of sepsis can “disappear”, even when it is clear, hour-to-hour, the infection and organ failure, and thus severe sepsis or worse, remain.” (Parente et al., 2020, p. 2)


### Generalisability 
* How to generalise model to WA hospitals
		* HADM_ID is not unique across hospitals
* Interpretability of the model
	* Adoption of the model by healthcare workers
	* Alert fatigue
	* Trust
	* Accuracy-interpretability trade-off in machine learning
	* A more complex model may provide a greater accuracy, however it will be less likely to be interpreted by the healthcare worker. 
	* "computational healthcare studies (including sepsis detection8–11,30,36) often choose statistics, intrinsically interpretable ML models and/or feature selection methods for analysis, instead of stateof-the-art ML models with higher accuracy."

* Accuracy of the prediction
	* alert burnout - healthcare providers to ignore alerts
	* high degree of false-positive alerts


* Multiple types of data, with time series such as heart rate, respiratory rate etc.), and 
	- as well as other none time series data

* Time & alert fatigue
	* Traditional machine learning models will need to keep track of the state.
	* This can often lead to spikes in risk alert
	* They need to sustain the risk over time, so that it is only alerting the healthcare staff if it is sure 


### Feature selection
	* Resources for collecting data
	* Simplify 
* Ambiguity with biological markers
	* Updated sepsis definition
	* the MIMIC-III public database included data before 2012, while the new definition of Sepsis-3.0 was published in 2016
	* Differences in the definition of sepsis in different phrases should be considered when applying our ANN model. Second, due to a high percentage of missing values in MIMIC-III, not all the variables which may affect the clinical outcomes in sepsis were included and analyzed. Some variables including the percentage of patients that received antibiotics, and the timing of such were not analyzed,” (Su et al., 2022, p. 9)

* “Events are irregularly sampled, include outlier data values, and can be entirely missing for some features and patients. Additionally, the same feature can be assigned multiple codes, which further complicates any processing.” (Saqib et al., 2018, p. 4039)

### Modelling
* How to work with time series data for lab events
	* How to combine the admission information 
	* Time series:
		* “Recurrent neural network (RNN) is known to learn time series data but has its own limitation of vanishing and exploding gradients as a result of weight updation through backpropagation. Long short term memory (LSTM) networks, on the other hand, were developed for the detection of long-term dependencies in real-time series data and advancement on RNN.” (Sharma et al., 2022, p. 2)

* Local explanation provided (via post-hoc analysis using LIME/SHAP)
* As such, features obtained from local explanations will not be a good representation of the additional relevant features needed for timely sepsis detection. Thus, global interpreter for state-of-art-model is essential because it can aid the task of identifying relevant sepsis factors. Moreover, a global interpreter allows black-box models to retain their high accuracy, while becoming more transparent to human beings.

Different observations conducted over time
* Standardise particular features

### Time
Moreover, sepsis treatment consists of modeling irregularly-sampled time series with long-term dependencies [9]
In the accurate prediction of sepsis onset, the computational models need to simulate and understand irregularly collected data over time, particularly focusing on the relationships between past and present data points. This technique helps to address the complexities and dynamics of sepsis progression, which often involve subtle changes over time.



Administration of general antibiotics is not effective

* Success of antibiotics prevents the progression of sepsis




## Benefits
Treatment for non-severe sepsis is cheaper - catch before it progresses



- **Adaptive Learning:** Design models that can adapt to changes in the data distribution over time. This could help the model accommodate changes in clinical coding practices.





## Questions

* Dividing the data into ranges
* Should we have any of these sorts of flowcharts included in our proposal?
* Identifying features for different models 
* Should we create a table appendix for clinical variables identified for sepsis diagnosis in other academic studies?
* More specific about LSTM
	* Use PyTorch
	* [Using SHAP library for a PyTorch model](https://jamesmccaffrey.wordpress.com/2022/10/11/an-example-of-using-the-shap-library-for-a-pytorch-model/) 
	* explain predictions of convolutional neural networks with _PyTorch_ and _SHAP_
* LSTM has two modes: mode 1=vitals & demographics, mode 2 adds lab results
	* **SSP: Early prediction of sepsis using fully connected LSTM-CNN model** 




### Preprocessing
Preprocessing techniques are required for the model make sense of the data.

- - Use techniques like oversampling, undersampling, or synthetic data generation to balance the classes.
- **Time Series Preprocessing:**
    
    - Convert time series data into appropriate formats for modeling (e.g., feature extraction, aggregation, or transformation).
    - Consider different ways of representing temporal relationships, such as sliding windows or lagged features.

#### Outliers
• Edge cases and outliers in the data should not be ignored as they are special disease patterns.

- **Active Case Identification:** Implement proactive case identification strategies that capture cases at risk of being missed by clinical coding. This might involve leveraging additional data sources or algorithms to flag potential sepsis cases.
    
- **Synthetic Data Generation:** If the dataset suffers from class imbalance due to missed cases, consider generating synthetic data for the underrepresented class (sepsis cases). This can help balance the training dataset and improve model performance.
    
- **Temporal Patterns:** Exploit temporal patterns and trends in patient data to identify potential sepsis cases. Changes in vital signs, lab results, or other clinical parameters might signal the onset of sepsis.


