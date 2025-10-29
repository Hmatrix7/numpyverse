#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Vectorized Operations (no loops!)
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr * 2)
print(arr + 10)
print(arr ** 2)


# In[7]:


def square(x):
    return x * x

vec_square = np.vectorize(square)
print(vec_square(arr))


# In[8]:


#Apply function to rows/columns
#np.apply_along_axis()
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

def row_sum(row):
    return np.sum(row)

print(np.apply_along_axis(row_sum, axis=1, arr=matrix))


# In[9]:


#Column operation
print(np.apply_along_axis(row_sum, axis=0, arr=matrix))


# In[10]:


#Real Data Example — Normalize scores
#normalized = (x − min) / (max − min)
scores = np.array([50, 70, 90, 100])

norm = (scores - np.min(scores)) / (np.max(scores) - np.min(scores))
print(norm)


# In[20]:


data = np.array([3, 6, 9, 12])
data1 = data*3
def square(x):
    return x*x
vector_square=np.vectorize(square)
print(data1)


# In[21]:


print(vector_square(data))


# In[ ]:




