#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Load & Handle Missing Values
import numpy as np

data = np.genfromtxt("employees.csv", delimiter=",", skip_header=1)
print(data)


# In[5]:


data = np.genfromtxt("employees.csv", delimiter=",",
                     skip_header=1, filling_values=0)
print(data)


# In[6]:


data = np.genfromtxt("employees.csv", delimiter=",", skip_header=1)
col_means = np.nanmean(data, axis=0)
inds = np.where(np.isnan(data))
data[inds] = np.take(col_means, inds[1])
print(data)


# In[9]:


scores = np.genfromtxt("scores.csv", delimiter=",", skip_header=1)

mean = np.nanmean(scores)
scores = np.where(np.isnan(scores), mean, scores)

np.savetxt("clean_scores.csv", scores, delimiter=",")


# In[ ]:




