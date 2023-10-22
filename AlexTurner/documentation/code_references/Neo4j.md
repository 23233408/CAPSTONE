
## Add 
Add database
	> local DBMS (+) 
	> Title 

Start capstone
create database name 
	> call 'patient'
Neo4j Browser

## Creating Nodes

``` neo4j

LOAD CSV WITH HEADERS from 'file:///relations.csv' as pat
MERGE (p:patient{id: pat.SUBJECT_ID})
MERGE (a:admission{id: pat.HADM_ID})
CREATE (icd:icd{title: pat.SHORT_TITLE})
MERGE (p)-[:has]->(a)
MERGE (a)-[:has1]->(icd)

```

``` neo4j
match (nodes) return (nodes)
```