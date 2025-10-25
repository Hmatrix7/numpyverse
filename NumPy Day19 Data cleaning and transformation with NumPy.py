#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

data = np.array([45, 60, np.nan, 72, 59, np.nan, 81])

# Detect missing values
print(np.isnan(data))

# Count missing values
print(np.sum(np.isnan(data)))


# In[4]:


#Replace NaN with Mean
cleaned = np.where(np.isnan(data), np.nanmean(data), data)
print(cleaned)


# In[6]:


#Remove NaN values
no_nan = data[~np.isnan(data)]
print(no_nan)


# In[18]:


#Detecting Outliers
#Outliers can distort your analysis.
#One common method: Z-score.
data = np.array([45, 60, 59, 72, 81, 90, 200])  # 200 is an outlier

mean = np.mean(data)
print("mean",mean)
print("std",std)
std = np.std(data)

z_scores = (data - mean) / std
print(z_scores)

# Flag values with |z| > 2 as outliers
outliners= data[np.abs(z_scores)>2]
print(outliners)
# Removing Outliers
filtered=data[np.abs(z_scores)<2]
print(filtered)


# In[20]:


#example
data = np.array([10, 12, 15, 20, 100])  # 100 might be an outlier
mean = np.mean(data)
std = np.std(data)

z_scores = (data - mean) / std
abs_z_scores = np.abs(z_scores)

# Find outliers
outliers = data[abs_z_scores > 2]
print("outliners",outliners)


# In[ ]:




