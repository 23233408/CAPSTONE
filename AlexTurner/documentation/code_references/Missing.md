## Missingno

[https://github.com/ResidentMario/missingno](https://github.com/ResidentMario/missingno)  
Missingno offers a visual summary of the completeness of a dataset. 

Use on Admissions table:
- Not every patient is admitted to the emergency department as there are many missing values in `edregtime` and `edouttime`.


``` python
# !conda install -c conda-forge missingno -y
import missingno as msno
msno.matrix(a)
```