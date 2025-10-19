#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Instead of looping through elements, NumPy performs operations on entire arrays — much faster!


# In[1]:


# Without NumPy (slow)
import numpy as np
data = [1, 2, 3, 4, 5]
squared = [x**2 for x in data]

# With NumPy (fast)
arr = np.array(data)
squared_np = arr**2

print(squared_np)


# In[ ]:




