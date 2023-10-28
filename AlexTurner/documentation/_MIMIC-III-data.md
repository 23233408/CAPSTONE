
[MIMIC-III ERD](https://mit-lcp.github.io/mimic-schema-spy/)



# Database Exploration
	26 tables

How are they related?
Which tables are related?
Dictionary and definitions?

* Is `SEQ_NUM` a good way for us to identify chronology? 
	* No, because individuals could have multiple ICD codes immediately after admission...

## Patients
The patient table defines SUBJECT_ID, a unique identifier for each patient. 
~46k patients
## Admissions
* Patient Information is stored here
`HADM_ID`
A unique identifier for admissions. Each patient can have multiple admissions, multiple `HADM_ID` values. This can be the same value in different hospitals
`ICUSTAY_ID`
A unique identifier for ICU stay of a patient.
One `hadm_id` can be linked to multiple `icustay_id` values; when a patient had a multiple ICU stays during an admission. (e.g., transferring between multiple ICUs)
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
## LABEVENTS
Tracks lab work and analysis
## MICROBIOLOGY EVENTS
tracks cultures used for determining effectiveness of antibiotics
If you have an infection, the healthcare workers will usually take a culture of it and test it in the lab against particular antibodies and develop a particular treatment plan.
used for determining effectiveness of antibiotics
Is this a big issue? the cultures take a while to come back?
## DICTIONARY & Definitions
Description tables are prefixed with "D".
They define items, measurements and procedures. 

### D_CPT
Current Procedural Terminology codes


