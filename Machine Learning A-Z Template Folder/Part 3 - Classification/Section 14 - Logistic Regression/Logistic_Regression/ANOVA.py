# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 19:30:31 2019

@author: User1
"""

#One-Way ANOVA using STATSMODELS
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

data = pd.read_csv('Social_Network_Ads.csv')
data.boxplot('EstimatedSalary',by='Gender')
model = ols('EstimatedSalary - Gender', data=data).fit()
anova_table = sm.stats.anova_lm(model,typ=2)
print(anova_table) 