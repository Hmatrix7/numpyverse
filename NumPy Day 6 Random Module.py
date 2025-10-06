#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A module is simply a single Python file (.py)
#that contains Python code — functions, classes, variables, or even runnable code.
#It helps organize code into manageable sections.


# In[ ]:


#A package is a collection of modules organized in a directory that
#contains a special __init__.py file (even if it's empty). 
#This file tells Python that the directory should be treated as a package.


# In[1]:


import numpy as np


# In[5]:


print(np.random.rand())


# In[6]:


print(np.random.rand(5))


# In[7]:


print(np.random.rand(2,3))


# In[25]:


#arr → the array or range to choose from
#size → how many items you want to pick
#replace → whether you can pick the same item more than once
#replace=True (with replacement)
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr) 
print(np.random.choice(arr, size=3))
print(np.random.choice(arr, size=3, replace=False))


# In[29]:


import numpy as np
np.random.seed(42)
print(np.random.rand(3))


# In[42]:


# Normal distribution (mean=0, std=1)
print(np.random.normal(100, 10, 5))

# Uniform distribution (between 0 and 10)
print(np.random.uniform(0, 10, 5))


# In[34]:


print(np.random.rand(3,3))


# In[41]:


import numpy as np
matrix = np.random.randint(10, 50, size=(3,3))
print(matrix)

                         


# In[40]:


import numpy as np

matrix = np.random.randint(10, 50, size=(3, 3))
print(matrix)


# In[44]:


#Exercise 6: Random Sampling Simulation
#Simulate rolling a 6-sided die 10 times, showing each result.
#Hint: use np.random.randint(1, 7, size=10)
print(np.random.randint(1, 7, size=10))


# In[ ]:




