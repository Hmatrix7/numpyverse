#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


data = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])

print(np.mean(data))         # overall mean
print(np.median(data))       # median
print(np.std(data))          # standard deviation
print(np.var(data))          # variance


# In[3]:


print(np.mean(data, axis=0))   # mean of each column
print(np.mean(data, axis=1))   # mean of each row


# In[ ]:




