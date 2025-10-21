#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Today we’ll explore how to generate random numbers, simulate datasets, and understand random distributions using NumPy 
#— a key skill for data analysts and data scientists
#NumPy’s random module helps generate random values efficiently


# In[4]:


import numpy as np

# Random float numbers between 0 and 1
a = np.random.rand(5)
print(a)

# Random integers
b = np.random.randint(1, 10, size=5)
print(b)


# In[5]:


#Random Arrays and Shapes
# 2D array of random floats (3x3)
arr = np.random.rand(3, 3)

# 2D array of random integers
ints = np.random.randint(10, 50, size=(2, 4))


# In[6]:


np.random.seed(42)
print(np.random.rand(3))


# In[8]:


np.random.seed(42)
print(np.random.rand(3))


# In[ ]:




