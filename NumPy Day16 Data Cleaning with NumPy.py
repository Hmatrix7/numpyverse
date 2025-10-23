#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Detecting Missing or Invalid Data
NumPy uses np.nan for missing values and np.inf for infinity.


# In[1]:


import numpy as np

data = np.array([12, np.nan, 7, np.inf, 9, -np.inf, 15])

# Detect NaN and infinity
print(np.isnan(data))  # True for NaN
print(np.isinf(data))  # True for inf and -inf


# In[3]:


#Removing Missing or Infinite Values
cleaned = data[~np.isnan(data)]        # remove NaN
cleaned = cleaned[~np.isinf(cleaned)]  # remove inf
print(cleaned)


# In[10]:


#Replacing Missing Data
#Sometimes, you don’t want to remove values — you replace them instead
data = np.array([12, np.nan, 7, np.inf, 9, -np.inf, 15])

# Replace NaN with mean of valid numbers
mean_val = np.nanmean(data[np.isfinite(data)])#Compute mean ignoring NaN
data[np.isnan(data)] = mean_val
data[np.isinf(data)] = 0  # Replace inf values with 0
print(data)


# In[5]:


#Logical Filtering Example
scores = np.array([75, 88, 92, 59, np.nan, 101, 0, 85])
scores = scores[np.isfinite(scores)]  # remove NaN

# Keep only scores between 0 and 100
clean_scores = scores[(scores >= 0) & (scores <= 100)]
print(clean_scores)


# In[27]:


test=np.array([10,20,30,40,np.nan,np.nan,99])
mean_v=np.nanmean(test) #calculating mean
test[np.isnan(test)]=mean_v #replacing nan values with mean value 
print(test) #printing values


# In[30]:


test =np.array([10,20,30,40,np.nan,np.inf,10])
mean_vl=np.nanmean(test[np.isfinite(test)])
test[np.isnan(test)]=mean_vl
test[np.isinf(test)]=0
print(test)


# In[ ]:




