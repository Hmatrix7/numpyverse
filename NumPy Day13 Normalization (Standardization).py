#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

data = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])

# Compute column-wise mean and std
mean = data.mean(axis=0)
std = data.std(axis=0)

# Normalize
normalized = (data - mean) / std

print("Mean:", mean)
print("Standard Deviation:", std)
print("Normalized Data:\n", normalized) 


# In[2]:


#Min–Max Normalization
#Scales values to a range of [0, 1]

#Xnorm=(X−Xmin)/(Xmax−Xmin) 


# In[3]:


data = np.array([[2, 4],
                 [6, 8],
                 [10, 12]])

min_val = data.min(axis=0)
max_val = data.max(axis=0)

normalized = (data - min_val) / (max_val - min_val)
print(normalized)


# In[4]:


#Row-wise vs Column-wise Normalization
#Use the axis parameter to control how normalization is applied:
#axis=0 → normalize columns (each feature)
#axis=1 → normalize rows (each observation)
row_norm = (data - data.mean(axis=1, keepdims=True)) / data.std(axis=1, keepdims=True)
print(row_norm)


# In[ ]:




