#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install numpy


# In[1]:


import numpy as numpy


# In[ ]:


#What is NumPy? NumPy = Numerical Python.
#It’s used for Handling large datasets efficiently.
#Performing mathematical and statistical operations.
#Serving as the foundation for pandas, scikit-learn, and many other data tools.


# In[5]:


#Creating Arrays NumPy arrays are like Python lists but more powerful.
import numpy as numpy
arr1=numpy.array([1,2,3,4,5,6])
array2=numpy.array([7,8,9,10,11,12])
print(arr1)
print(array2)


# In[6]:


#Array Attributes
#You can check basic properties
print(arr1.ndim)   # number of dimensions
print(arr1.shape)  # rows and columns
print(arr1.size)   # total elements
print(arr1.dtype)  # data type


# In[10]:


#Creating Special Arrays
np.zeros((3,3))       # 3x3 array of zeros
np.ones((2,4))        # 2x4 array of ones
np.eye(3)             # Identity matrix
np.arange(0,10,2)     # Numbers 0–10 step 2
np.linspace(0,1,5)    # 5 numbers between 0 and 1


# In[11]:


np.ones((3,3)) 


# In[12]:


np.arange(50,100,5) 


# In[ ]:




