#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sorting Arrays
import numpy as np

arr = np.array([5, 1, 8, 3, 2])
print(np.sort(arr))


# In[5]:


#Sorting 2D arrays
data = np.array([[3, 1, 2],
                 [9, 7, 8]])
#By row
print(np.sort(data, axis=1))


# In[6]:


#By columns
print(np.sort(data, axis=0))


# In[11]:


#np.unique() — find unique values
vals = np.array([1, 1, 1, 1, 2, 2, 3, 3, 3, 3])
print(np.unique(vals))


# In[12]:


unique, counts = np.unique(vals, return_counts=True)
print(unique)
print(counts)


# In[13]:


#Removing duplicates from real data
names = np.array(["Ann", "Kim", "Ann", "John", "Kim"])
clean = np.unique(names)
print(clean)


# In[15]:


#Sorting with indexing
arr = np.array([50, 10, 30])
idx = np.argsort(arr)
print(idx)
print(arr[idx])  # sorted reorder


# In[ ]:




