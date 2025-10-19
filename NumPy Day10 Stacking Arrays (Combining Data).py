#!/usr/bin/env python
# coding: utf-8

# In[4]:


#You can combine arrays vertically or horizontally
#Vertical Stack (one on top of another)
import numpy as np
a=np.array([[1,2,3],
           [4,5,6]])
b=np.array([7,8,9])
v_stacked=np.vstack((a,b))
print(v_stacked)


# In[5]:


#Horizontal Stack (side by side)
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])

h_stacked = np.hstack((a, b))
print(h_stacked)


# In[6]:


#Column Stack (1D → as columns)
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

cols = np.column_stack((x, y))
print(cols)


# In[11]:


#Splitting Arrays
#You can split one array into multiple sub-arrays.
#Split Horizontally (by columns)
import numpy as np
arr=np.array([[1,2,3,4,5,6,7,8,9]])
h_split=np.hsplit(arr,3)
print(h_split)


# In[12]:


#Split Vertically (by rows)
arr = np.array([[1, 2],
                [3, 4],
                [5, 6]])
split = np.vsplit(arr, 3)
print(split)


# In[13]:


#Array Transpose and Flatten
#Transpose (swap rows and columns)
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr.T)


# In[15]:


#Flatten (convert multi-D to 1D)
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
#flat=arr.flatten()
print(arr.flatten())


# In[ ]:




