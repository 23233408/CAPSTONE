## Missingno

[https://github.com/ResidentMario/missingno](https://github.com/ResidentMario/missingno)  
Missingno offers a visual summary of the completeness of a dataset. This example brings some intuitive thoughts about `ADMISSIONS` table:

- Not every patient is admitted to the emergency department as there are many missing values in `edregtime` and `edouttime`.
- `language` data of patients is mendatory field, but it used to be not.

``` python
# !conda install -c conda-forge missingno -y
import missingno as msno
msno.matrix(a)
```