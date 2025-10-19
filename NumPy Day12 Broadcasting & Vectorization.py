#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Broadcasting
#These are core concepts that make NumPy powerful and fast 
#— they allow operations on arrays of different shapes without writing loops
#Broadcasting lets NumPy automatically expand smaller arrays during arithmetic operations
#so they match the shape of the larger array


# In[2]:


import numpy as np

a = np.array([1, 2, 3])
b = 2
print(a + b)
#NumPy “broadcasts” the scalar 2 to match the shape of [1, 2, 3]


# In[3]:


A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[10],
              [20]])
print(A + B)
#Broadcasting with Different Shapes


# In[4]:


#Vectorized Operations (No Loops)
#Instead of using Python for loops, NumPy applies operations to all elements at once (fast!)


# In[5]:


x = np.arange(5)
y = np.arange(5, 10)

# Normal way
result = [a + b for a, b in zip(x, y)]

# NumPy way (vectorized)
result_np = x + y
print(y)
print(x)
print(x+y)


# In[6]:


#Broadcasting Rules
#Compare shapes from right to left.
#Dimensions must be equal or one of them must be 1.
#If these rules fail → ValueError


# In[7]:


A = np.ones((3, 4))
B = np.ones((3, 1))
print((A + B).shape)  #works → (3, 4)


# In[13]:


A = np.ones((4, 3))
B = np.ones((1, 3))
print((A + B).shape)  #works → (3, 4)


# In[31]:


C = np.ones((2, 3))
D = np.ones((3, 2))
print(C + D) #ValueError: shapes (2,3) and (3,2) not compatible


# In[ ]:


#	What It Does
#np.zeros(shape)	Creates array filled with 0s
#np.ones(shape)	Creates array filled with 1s
#np.empty(shape)	Creates an uninitialized array (random values in memory)
#np.full(shape, fill_value)	Creates array filled with any number you choose


# In[33]:


#Normalizing Data
#Broadcasting is super helpful in data analysis
#This normalizes each column (feature) — common in preprocessing for machine learning
data = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])

mean = data.mean(axis=0)
std = data.std(axis=0)

normalized = (data - mean) / std
print(normalized)


# In[ ]:




