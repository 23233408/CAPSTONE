


# Tasks
 

## Nyamka
* Use graph db to calculate centrality (common ICD9 codes)
	* Identify what other conditions are related to sepsis
	* Identify what blood tests are used for sepsis patients
	* Output to python - sorted by popularity (most related to sepsis).

## Kha
* Use graph DB: Item ID abnormal, at given chart time
	* input: filtered time
	* common ICD9 codes (POTENTIAL_SEPSIS), and IS_SEPSIS
	* How many of this have derangements (abnormal flags) in the first 'n' hours? 
	* These are the early indicators! ITEMID of labevents
	* Output to python - sorted by popularity (most related to sepsis).


## Ashwani
### pipeline for creating model input DF
* List of features from feature extraction
* Links_to which table
* Transform 

* have 'time' as a variable input 
	* is there a calculated 'time since admit' in the labevents? 
	* filter chart times in lab events by this input
	* forward fill for NaN


## Amy
### time and 
	* are 100% of the sepsis patients lab results collected? Show this on a graph.
		* Histogram 
			* Do all the sepsis patients do this test?
			* Purpose is to show whether that test is important
	* Time intervals 
		* histogram
			* is adding the best way? 
			* group by different fluid type

* Most common bloods for sepsis
	* All first
	* Again over time


## Alex
### Causal overlay
* Establish causality with chatGPT / the RPH local language model
	* Write prompts to return this in appropriate list format. 
	* Query language model with:
		* Potential causative agents (identified by graph, as well as literature)
			* Determine the causal relationship, ie. Does A cause sepsis? 
	* "does the feature X cause the condition Y, or does the condition Y cause the feature X, or is there no relation?"
		* get yes or no. Will identify 20 or 30.

### Set up modelling pipeline for traditional ML models



# Shiv
* feature selection PCA? 
* chart events before the time
	* make admit time to chart time?
	* treat first chart time as the first delta(t)





# Later
## Modelling with selected feature 
- From these 20 or 30, we look back at the truth, and see what are common. 
	- we will run into data processing issues here. We handle this by either:
		- Training, starting modelling with the first few data points (time at 4hrs)
		- Standard feature engineering, which is your traditional machine learning (no deep learning). But with heavy feature engineering.


## Data preparation
### feature selection
* What other symptoms/diseases are sepsis patients having?
* We need to prepare the data so that they have these abstractions, for example high heart rate, high bacteria count, etc. 




## Other tasks:
[x] Drop missing HADM_ID
[x] give the proportion of missing data as a reason



* Calculate how many lab events occur on average per admission.
	* Shiv got 382 on average.



OPTIONAL
> What is the importance of finding fluids?
* For each fluid test, what is the average number of itemids? Is it all of them/subset? Does this change over time for each IS_SEPSIS patient? Which of them are changing over time? If there is a change of time 
	* For one HADM_ID
		* first 2 hours, average of fluid_1 is 10
		* last 
	* For IS_SEPSIS patients 

* time & Itemid histogram - By fluid 





* Research:
	* Topic Modelling (for text data)
	* SciKit Survival








_____




Access the RPH server:
`ssh -L localhost:5000:localhost:5000 alex@146.118.68.235`


# Node centrality

``` neo4j
LOAD CSV WITH HEADERS FROM 'file:///uti.csv' as rec
MERGE (person:Admission{id:rec.HADM_ID})
MERGE (disease:DIAG{id:rec.SHORT_TITLE})
MERGE (person)-[:HAS]
```

``` neo4j
MATCH (p:Admission)-[:HAS]-(d:DIAG{id:'Severe sepsis'})
RETURN p,d
```

Graph centrality will tell us: 
* what node that has sepsis, has the second most common node
* We should use graph centrality to identify the most "important" nodes within a graph.
* To identify nodes that have something in common with sepsis. 

How to calculate centrality:
* Popularity index: The number of edges that are pointing to that node indicates the most popular. Popular meaning severe sepsis connected to other conditions




You get nodes which are very popular, just by expanding them out.
* Severe sepsis is connected to one admission and could be connected to another admission.
* Drilling down will give another common thing between people with severe sepsis as well as something else (commonality). For example, we saw Atril fribulation.







## Causal overlay

To know if the nodes identified in graph centrality should be included in the ML model, we need to do causal overlay. 

* Use language model to identify causality. And to verify the relationship. 
	* It could be a risk factor, but doesn't cause sepsis
	* Usually, the top ones are causal, I.e.  Septicemia NOS leads to septic shock
* EG:  Is there any relation between UTI and Sepsis?
	* The pathway is: UTI, leads to acute kidney injury, leads to sepsis

We don't use data mining because, for example, it could tell us that UTI causes sepsis, not sepsis causes UTI.





ChatGPT query:
* "We have a neo4j schema of patients P->[:has]->ICD diagnosis. I would like to know the top 10 most popular ICD nodes that patients share with ICD: sepsis. Can you write the cypher query?"

sp = shared patient


``` neo4j
MATCH (N)
WITH N, SIZE(N) as degree
```

``` neo4j
MATCH (d:DIAG{id:'Severe sepsis'})<-[:HAS]-(p:Admission)-[:HAS]->(icd:DIAG)
WHERE d <> icd
WITH icd, COUNT(p) as sp
ORDER BY sp DESC
LIMIT 30
RETURN icd.id as ICD_code, sp

```





What other symptoms/diseases are sepsis patients having.
* We need to prepare the data so that they have these abstractions (biomarkers, demographics, etc), for example high heart rate or high bacteria count
* We can't use disease, because they are clinical codes which come after. 

We want to reduce the fields:
* First filter the fields using chatGPT, then do the Graph, then chatGPT again to verify. 

_____


## Detecting sepsis early
@ 1:00:30

Aiming to detect sepsis in the first 4 hours of patient's admission
* Main thing is: HOW we clean the data
* Only keep the first 4 hours of patient tests
* Then, slowly, progressively, we should increase the number of features


## Identifying early indicators of sepsis
* Start with the first four hours of data.
	* See how the derangements are (the abnormal flags) using graph & charts 
	* Do we have any? How many are in first 4 hours? These are the early indicators.

* We will run into curse of dimensionality (200+ features)
	* This is when you would go into looking at most important signs

* Input these into ChatGPT, which will reduce all this to maybe 20 or 30 features
	* Because ChatGPT is trained on on PubMed data. PubMed is like all of medical research in the last 40 years. 

Do this first with the Labevents table. 

Microbiology table:
* culture bacteria
* Antibiotic sensitivity
* Need to know the timing statistics. ???


## Instrument variables identification
For sepsis and non sepsis patients, at the first four hours of presentation:
* Compare the first 4 hours, and then next 4 hours with the distribution of total. 
* Compare this with distributions first to see if anything shows up. These are the instrument variables -- variables which have a direct effect on the disease.

	* Urine and blood are most important tests!

#todo
1. Are 100% of the patients bloods collected in the first 4 hours? They won't be, but we need to show this on a graph.
3. What are the most common bloods tests taken for sepsis patients?


## Graph

Need to identify which are the most related item IDs at different points in time, and then train the model on this. 

To know what to throw at the model, we need to establish causality first. 
* Need to identify which are the most related item IDs to sepsis at different points in time. 
* These item IDs will change at different points in time.

1. Filter first hour in pandas
	1. identify the relevant itemIDs
2. Filter only the second hour
	1. identify the relevant itemIDs

Then look at what are most common bloods, and establish the most common bloods for sepsis. Because bloods could be for both sepsis and none sepsis. The only way to do this is through centrality, through graph.

Graph
* ICD title 
* Lab items connected with diagnosis
* Get a sense of what admissions, diagnosis and derangements (abnormal flags)




----


# COX PH and Survival analysis:

#todo
Research scikit survival

If there is increasing risk of sepsis it will be the line at the top (patient 1)
As you feed in more data, the bottom line (patient 2) indicates you you won't have a lot of sepsis

Can also use gradient boosted models.
Time dependent AUC / ROC. The AUC ROC will change over time. The accuracy may not be very good in the beginning, but it may increase.

survival probability, which means there is huge probability of survival big interval or hazard function. Cumulative hazard.

The model accuracy will change over time. So, if you use the first four hours of Bloods, along with the patient's past history, for that a patient, the first time you've seen, you should know is history because he would have had previous admissions to the hospital. Right. And based on that, for the first three hours, if you till the time, you get the blood results, and based on the admission text, this admission diagnosis. And also based on the bloods, and urine cultures, for the first four hours or three hours, you will get some accuracy. But as you keep adding more data, that accuracy would increase. Because as you're getting closer to sepsis, your markers would increase.


But it gives you risk of one patient with respect to the other. So if you have one patient who has a risk, like here you have saved one patient who has a risk, like this concordance who has a survival probability like this (on top), he's going to survive forever.

As you add more data, it will increase in terms of time. So you increase the data points (which solves the computational problem)


----








## Calculating dispersion of tests to identify time intervals
@1:55:00

To solve computation problems:
* Look at the dispersion of tests (all blood tests taken over time).
* How many events are taken?

For example, we may have admission at 5pm, but the first test at 8pm, so we need to take from the first test. If the average first test is after 3hours, then this is the time that we will use. 

Model Validation: Tasks
* For 80% of sepsis patients, how many tests do you need in the first n minutes?
* 80% of all sepsis patients need the first 30minutes before their first test

	* This may be only 40 test records, so we can discard the rest. Then we check the accuracy of this model. 

Using only admission text, and bloods, can we predict TTE (time to event) early? 

At this point in time:
* Does it accurately identify if this is an at risk sepsis patient?
* Check SKLearn to see if there are any characteristics shown.
* Then we can add more data by moving the time horizon to next point, and repeat the process. 


____
## SKlearn / sklearn survival 





* structured ML methods require Correct feature engineering and correctly structured data
* For structured ML methods (sklearn and survival), we need to be very picky about what goes into the model. As we increase the number of fields, the accuracy will drop.

### Survival analysis
Survival analysis is stochastic (relative risk), not deterministic (yes/no).
* Meaning you would only say that this person here is relatively at more risk than the other person. 
* In the plot, if we get all of the people at the top who are having sepsis, we are successful.
* One line represents one admission's TTE 


SciKit survival:
* The target, the thing that you're training on, is:  this is true (yes/no) for this amount of time (t)

Time to event:
* Just like in your in your classification problem, you will have true and false. Here the targets are: true and false, as well as the time 

For a patient that comes with these symptoms, your machine learning model will give you the risk of the survivability at this time as a curve. It will tell you that from this time to this time this fellow's thing would drop. We are predicting this curve at this time.

For feature explainability, we should use SHAP




____

### Survival analysis with SciKit survival
* Model training: do the prediction on the other data. 
	* After model training, we do prediction with different timestamps.
	* Then we plot the chart to see what the difference is between the risk scores. 

Survival input:
* Like a static machine learning model: All the time features should be in a single frame. 

Survival output:
* The survival model gives us a temporal risk. 
* For sepsis people, survivability would fall off, meaning they are going to die soon. For non-sepsis people, it would stay.

Why?
* For 10 patients in the ward, you can categorise them with a risk score - the risk here is 40, here it is 20 (given from the survival curve pattern)

_____

Feature selection:
* chatGPT - relationship between features

### EDA
* graph DB 
	* for Centrality (show what the cohorts are skewed towards)
		* associations
		* when you have derangements (like when there is an abnormal flag)
if you engineer this well, then the visualisations from Graph will be good
* chart with time: 4h, 2h

## Feature engineering & data preparation
### Structured data 

* don't have to normalise
* has to be small dimensions
- Important to worry about the temporal aspects
	- Was there a difference in the bloods in the last 4hrs? WBC in the last 3hrs?

### Text data 
* Add admission text
	* Need to identify what the difference is for using text/not using text
* Use BOW, TFIDF 
	- It takes most common words related to sepsis (eg "Chest pain"), sets up a dictionary, checks how many times the words repeats, and turns this into a vector

### Data preparation steps

**1.1** 
* bloods, culture, urine, demographics, past comorbidities
* Fix on particular blood tests. Use nanmean and forward filling for NaN values

**1.2**
* try 1hr, 3hr, 10, 24hr after admission
* Identify time interval difference between successive tests using the data
	* "Usually, when I take hemoglobin, they also take my other things at the same time. That's one batch, another batch is at another point in time, etc. That's how we structure our features."

**1.3**
* add text (using Topic modelling)
	- Gives a vector for text (eg admission text). We then concatenate the vector with the structured data into one model. 



## Model training:
1. SKlearn: traditional ML
	* RF, GBM, LR

2. Survival (another kind of process)
- use either RF or Gradient boosting (GBM)
- Targets are a little different
## Model verification
* Graph 
	* associations
	* when you have derangements (like when there is an abnormal flag)



_____


## Data preparation (time intervals)

For second group, we can specify the time interval in as one of the features, and give it as a single time. 
Batch, time step, features

We only input the fixed interval in both models. 
We forward fill (the closest to the fixed interval (ie time at 2hrs)) the whole dataframe.

Feature engineering has to be one row. 
One admission at different points in time is one row. 
[admission 1, the first four hours]
[admission 1, next four hours]

Each of these would go to the model. The values of these features will be forward filled. Specify the time interval, then forward fill the data frame. The output is yes or no, for each row. 



For every admission:
1. do the first n (e.g. 2) hours for all the different admissions. 
	* Model outcome for one admission: yes or no? 
	* Model outcome for another admission: yes or no? 
	* And then we compare to our ground truth, and then we can see the accuracy. 
2. After doing the first n hours, we add one more row for each admission (another 2 hours). 
3. Continue adding time till we reach an acceptable rate


For all patients, how many blood tests were taken over time?
Plotting (scatter plot) this will give us peaks, concentrations.  This is how we will find our prediction interval. 

For all patients. Take time stamps of lab events. Plot this. 
If this is too hard, then just do 1hr, then next hour.
Sepsis patients. Take time stamps of lab events. 

First training: average value of the first 2 hours.
Second training: average value of the first 4 hours. 


the problem with continuity. So sometimes it can lag Yes, sometimes it can lag No, sometimes it can time Yes, again, that's fine here, we would not just take time in the last two hours, but we'll time in the last four hours time in the last 12 hours. So, to begin with this will be done in the beginning. 

So, when you take a snapshot, how would you put temporal data inside? 
Use the last one, or use the average over the last four hours, or the average over the last 12 hours.
Last four hours as features. Only the important ones.
Last twelve hours as features. 

Take the time of lab events, plot the points of time from admission. Number of tests for that time. For each patient. 





______


## LSTM
* If we've done graph properly, we shouldn't use LSTM
* Because the data is multimodal (we have text and structured data), LSTM has to use  attention. And maybe include topic modelling. 
* Ragged tensor flow 
	* used for when you don't have constant/fixed batches
	* The LSTM batch is nothing but type (a category). 
* explainability using TimeSHAP
### LSTM and NaN
* masking to deal with NaN values. Replace NaN with -100, and model will ignore that.
* Keras masking (tensor flow). Pytorch doesn't have fill in value. 


## Working with LSTM
If we use LSTM, we pass time as a feature (delta T 1, delta T 2, delta T 3)

Each time comes with a data point. Take 4 data points. At each data point, you would have NaN. Then we have time (delta T)

delta T: you've got a blood sample after two hours, of WBC count
You have WBC and some other value (platelets) after 3 hours. 
delta T = 2. The value of the WBC count is the value you receive at this point (2 hours), and the value of platelets is the value you receive of platelets at this time. But you don't have this platelet value, so you put minus 100, minus 100. 
And then the next time frame, you put three hours. 

Fixed features, at time. 

Features will be rows. And the column will be delta T. You just have to create a list, and then get a list of lists. Each patient has multiple times, but fixed features. We use the list structure. 
Convert this into the ragged. Then pass this to the LSTM.

___

## RPH methods
CNN with MC dropout
- have to be very particular with calibration
	- calibration curve: actual probability versus predicted probability
- ideal line is linear

### Linear calibration:
* Regression means you model, your softmax or your sigmoid, predicts a value between zero and one.
* Requires the true score

_______


## Other off-topic resources

**UMAP:** for error analysis, if we get a chance


**Pandarallel**
- how you parallelise your CPU cores 
- to speed up the execution of Pandas operations by parallelizing the computations

DEEP IV (instrumental variable) --- don't use this.. too elaborate

**Azure autoML:**  automatically train on many models

**data leakage:** All of the lab_items will show as abnormal at the end of their stay if they reach the severe sepsis phase, because the patient's organs will be failing. 

**delta flag:** used to update previous values. It's a redundancy. 