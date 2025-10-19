#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Function	Description
np.sum()	Sum of elements
np.mean()	Mean (average)
np.median()	Median
np.std()	Standard deviation
np.var()	Variance
np.min() / np.max()	Minimum and Maximum
np.argmin() / np.argmax()	Indices of min/max values


# In[7]:


import numpy as np

data = np.array([12, 45, 23, 56, 34, 67, 89])

print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Lower quartile:", np.percentile(data,25))
print("Upper quartile:", np.percentile(data,75))
print("Median:", np.percentile(data,50))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
print("Min:", np.min(data))
print("Max:", np.max(data))
print("Index of Min:", np.argmin(data))
print("Index of Max:", np.argmax(data))


# In[8]:


arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print("Column-wise mean:", np.mean(arr, axis=0))  # mean of each column
print("Row-wise mean:", np.mean(arr, axis=1))     # mean of each row


# In[ ]:




