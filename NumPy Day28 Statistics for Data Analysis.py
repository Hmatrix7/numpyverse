#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Mean, Median, Mode (mode = from SciPy later but I’ll explain)
#Standard Deviation & Variance
#Percentiles
#Correlation
#Real dataset example


# In[6]:


import numpy as np

scores = np.array([40, 50, 60, 70, 80, 90])

print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Std Dev:", np.std(scores))
print("Variance:", np.var(scores))
print("25th percentile:", np.percentile(scores, 25))
print("75th percentile:", np.percentile(scores, 75))


# In[9]:


#Correlation
#Relationship between two variables (scale −1 → +1)
#If values close to 1 → strong positive relationship
height = np.array([160, 165, 170, 175, 180])
weight = np.array([55, 60, 65, 72, 80])

correlation = np.corrcoef(height, weight)
print(correlation)


# In[12]:


sales = np.array([200, 250, 300, 270, 320, 400, 390])

print("Mean:", np.mean(sales))
print("Median:", np.median(sales))
print("Std Dev:", np.std(sales))
print("Min:", np.min(sales))
print("Max:", np.max(sales))
print("90th percentile", np.percentile(sales,90))


# In[14]:


temps = np.array([30, 31, 29, 35, 40, 38, 37])
humidity = np.array([60, 58, 65, 70, 75, 72, 71])
correlation = np.corrcoef(temps,humidity)
print(correlation )


# In[ ]:




