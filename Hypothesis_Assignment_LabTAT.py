# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:50:38 2020

@author: RAVI
"""

import pandas as pd
import scipy
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

LabTAT=pd.read_excel("C:\RAVI\Data science\Assignments\Modue 5 Hypothesis\LabTAT.xlsx")
LabTAT

LabTAT.columns="Laboratory1","Laboratory2","Laboratory3","Laboratory4"

##########Normality Test ############
#Ho= Data is normally distributed (no action take)
#Ha=Data is not normally distributed (action take)

stats.shapiro(LabTAT.Laboratory1)
# p-value = 0.55 >0.05 so p high null fly => It follows normal distribution

stats.shapiro(LabTAT.Laboratory2)
# p-value = 0.86 >0.05 so p high null fly => It follows normal distribution

stats.shapiro(LabTAT.Laboratory3)
# p-value = 0.42 >0.05 so p high null fly => It follows normal distribution

stats.shapiro(LabTAT.Laboratory4)
# p-value = 0.66 >0.05 so p high null fly => It follows normal distribution


############## Variance test #########
#Ho= Variance of TAT of all Labs are equal
#H1=atleast 1 Lab variance of TAT are not equal

scipy.stats.levene(LabTAT.Laboratory1,LabTAT.Laboratory2)
#H0=Variance of TAT of Lab 1 is equal to variance of TAT of Lab 2
#H1=Variance of TAT of Lab 1 is not equal to variance of TAT of Lab 2
# p-value = 0.06 > 0.05 so p high null fly accept null hypothesis.

scipy.stats.levene(LabTAT.Laboratory2,LabTAT.Laboratory3)
# p-value = 0.33> 0.05 so p high null fly accept null hypothesis.

scipy.stats.levene(LabTAT.Laboratory3,LabTAT.Laboratory4)
# p-value = 0.15 > 0.05 so p high null fly accept null hypothesis.

scipy.stats.levene(LabTAT.Laboratory4,LabTAT.Laboratory1)
# p-value = 0.221 > 0.05 so p high null fly accept null hypothesis.


############# One - Way Anova###################
#Ho= Average TAT for all the samples is same
#Ha= Averages TAT for all the samples is not same

mod = ols('Laboratory1~Laboratory2+Laboratory3+Laboratory4', data=LabTAT).fit()
aov_table=sm.stats.anova_lm(mod, type=2)
print(aov_table)
#Laboratory2  p-value = 0.166299 > 0.05 so p high null fly accept null hypothesis.
#Laboratory3  p-value = 0.277335 > 0.05 so p high null fly accept null hypothesis.
#Laboratory4  p-value = 0.215323 > 0.05 so p high null fly accept null hypothesis.


#there is no significant difference in the average TAT for all the laboratories.
















