#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[8]:


#Element-wise Operations
a=np.array([2,4,6])
b=np.array([1,3,5])
print(a+b)
print(a-b)
print(a*b)
print(a / b) 


# In[12]:


#Universal Functions (ufuncs)
arr = np.array([1, 10, 100])
print(np.sqrt(arr))
print(np.sum(arr))
print(np.exp(arr))
print(np.log(arr))


# In[14]:


#Broadcasting lets you operate on arrays of different shapes without writing loops.
#Broadcasting with Scalars
arr = np.array([5, 10, 15])
arrb=100
print(arr+arrb)


# In[15]:


#Broadcasting with 2D and 1D
x = np.array([[1, 2, 3],
              [4, 5, 6]])
y = np.array([10, 20, 30])
print(x+y)


# In[20]:


#Aggregate Functions with axis
arr = np.array([[2, 4, 6],
                [1, 3, 5]])
print(np.sum(arr))
print(np.sum(arr,axis=0))
print(np.sum(arr,axis=1))

