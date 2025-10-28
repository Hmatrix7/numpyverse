#!/usr/bin/env python
# coding: utf-8

# In[3]:


#np.where() — Find indices that match a condition
import numpy as np
arr=np.array([5,12,7,20,3,15])
indices = np.where(arr>10)
print(indices) 
#Use it to extract values
print(arr[indices])


# In[5]:


indices = np.where(arr<10,0,arr)
print(indices)


# In[6]:


arr2 = np.where(arr < 10, 0, arr)
print(arr2)


# In[9]:


#np.take() — Grab by index list
data = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])

selected = np.take(data, [0, 2], axis=1)
print(selected)


# In[10]:


selected = np.take(data, [0, 2], axis=0)
print(selected)


# In[11]:


#Boolean Filtering
age = np.array([18, 25, 16, 30, 22, 14, 28])

adults = age[(age >= 18) & (age <= 30)]
print(adults)


# In[12]:


#Small Real-World Data Filtering Example
temps = np.array([28, 30, 35, 33, 29, 38, 40, 36, 31, 27, 26, 29])
print(temps[temps > 33])


# In[13]:


temps_fixed = np.where(temps < 28, 28, temps)
print(temps_fixed)


# In[ ]:




