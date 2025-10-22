#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Stacking Arrays

np.vstack() → stack arrays vertically (row-wise)

np.hstack() → stack arrays horizontally (column-wise)

np.dstack() → stack arrays depth-wise (3D)

np.concatenate() → general-purpose stacking

Splitting Arrays

np.vsplit() → split vertically (row-wise)

np.hsplit() → split horizontally (column-wise)

np.array_split() → split into unequal parts


# In[6]:


import numpy as np

# Create sample arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Stacking
v = np.vstack((a, b))
z = np.hstack((a))
y = np.vstack((a))
h = np.hstack((a, b))
d = np.dstack((a, b))

print("Vertical Stack:\n", v)
print("Horizontal Stack:\n", h)
print("Depth Stack:\n", d)
print("test\n",z)
print("test\n",y)

# Splitting
arr = np.array([[1,2,3,4,5,6],
                [7,8,9,10,11,12]])

print("\nHorizontal Split:", np.hsplit(arr, 3))
print("Vertical Split:", np.vsplit(arr, 2))


# In[ ]:




