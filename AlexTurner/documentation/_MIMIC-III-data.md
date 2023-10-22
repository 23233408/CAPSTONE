


## Building the database


# Database Exploration
	26 tables

	How are they related?
	Which tables are related?
	Dictionary and definitions?

* Is `SEQ_NUM` a good way for us to identify chronology? 
	* No, because individuals could have multiple ICD codes immediately after admission...

## PATIENT
Patient table defines subject_ID
SUBJECT_ID is a unique identifier for each patient. 
~46k patients in the


Patient Information

- Each patient is unique with its own “subject_id”.
    
- Each hospital admission of a patient is unique with
    
    “hadm_id”.
    
- Each ICU stay of a patient is unique with “icustay_id”.
    
- That means,
    
    - One subject_id can be associated with multiple hadm_id's
        
        when a patient had multiple admissions.
        
    - One hadm_id can be linked to multiple icustay_id  
        when a patient had a multiple ICU stays during an admission. (e.g., transferring between multiple ICUs)
## ADMISSIONS

* Each patient can be admitted to hospital multiple times

* Each admission requires a unique admissions id,  `HADM_ID`
* Each patient can have multiple `HADM_ID`
* This can be the same value in different hospitals


## DIAGNOSES_ICD
Each row in corresponds to a diagnosis code associated with a specific hospital admission. 

`SEQ_NUM`
Indicates the order in which the diagnosis codes were recorded during that specific patient's admission. It helps to provide context about the chronological sequence of diagnoses given to a patient during their hospital stay.

## ICUSTAY_ID
Average stay

## CHART EVENTS
EMR (electronic medical record) for patients while they are in the ICU
- specific to the ICU
		
## NOTE EVENTS
- significant amounts of textual data

## PRESCRIPTIONS
- Tracks all prescriptions given during ICU stay



LABEVENTS
Tracks lab work and analysis

MICROBIOLOGY EVENTS
tracks cultures used for determining effectiveness of antibiotics
If you have an infection, the healthcare workers will usually take a culture of it and test it in the lab against particular antibodies and develop a particular treatment plan.
used for determining effectiveness of antibiotics
***** is this a big issue? the cultures take a while to come back?


## DICTIONARY & Definitions
‘D’ refers to dictionary
define items, measurements, procedures

### D_CPT
Current Procedural Terminology codes


