
**Identify sepsis occurrences**

Establish the criteria for identifying patients with sepsis
- Which score and why?
	- We chose qSOFA over SOFA because of the non-disponibility of laboratory data in a systematic form, while qSOFA considers only measures taken from physical examination and the occurrence of infections. However, due to the missing values Glasgow coma scale, we did not consider it in our study for the qSOFA criteria.

Given that the definition of sepsis is evolving, with Sepsis-3.0 being published in 2016, in order to identify sepsis occurrences, we will test two strategies, comparing the results with ICD-9 codes related to sepsis.
(i) search for the ICD-9 codes belonging to the ICD-9 short title groups relating to sepsis over the 
in primary, secondary, and death ICD-10 fields over the records relate
(ii) applying the criteria from qSOFA proposed by [2] as an alternative way to identify patients with sepsis.


(i) respiratory rate higher than 22 per minute, (ii) systolic blood pressure lower than 100 Hg



**Identify inclusion and exclusion criteria for modelling**
- treatment of missing values
- individuals with age less than 18.



**Identify features from MIMIC-III data** 
Clinical and laboratory data associated with 53,423 age ≥ 16 patients from 2001 to 2012 and 7870 neonates from 2001 to 2008 admitted in ICU were documented [13]. The database mainly included charted events such as demographics, vital signs, laboratory tests, vital status, medications, image reports, and clinical outcomes. All patients with sepsis (ICD9 code: 99,591) in MIMICIII (version 1.4) were enrolled in this study.





Imputing
  

Identify outcome measures

- What do we use as our standard definition of sepsis?

- This will be used as our primary target for developing the model

  

* We used the clinical surveillance criteria proposed by Rhee et al5

(Figure E1, available online at http://www.annemergmed.com).

  

  

  

Data ingestion

  

data cleaning

  

data exploration

  

feature engineering

  

Modelling - supervised / unsupervised

  

Model evaluation & tuning

  

Model selection