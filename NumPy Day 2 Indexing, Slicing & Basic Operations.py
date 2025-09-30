#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Indexing (Picking single elements)


# In[14]:


import numpy as np
arrb1=np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]]
)

print(arrb1[0, 0])   # First row, first column → 10
print(arrb1[1, 2])   # Second row, third column → 60
print(arrb1[-1, -1]) # Last row, last column → 90
print(arrb1[0, 0])
print(arrb1[1, 0])
print(arrb1[2, 2])


# In[ ]:


#Slicing (Picking ranges of elements)


# In[ ]:


#array[start:end:step]
#start → where slicing begins
#end → where slicing stops (not included)
#step → skip interval (default = 1)


# In[45]:


# Take a row
print(arrb1[0])       # [10 20 30]

# Slice first 2 rows
print(arrb1[0:2])     # [[10 20 30]
                    #  [40 50 60]]

# Slice second column
print(arrb1[:, 1])    # [20 50 80]

# Take first 2 elements from last row
print(arrb1[-1, 0:2]) # [70 80]


# In[46]:


print(arrb1[:,0:2])    


# In[47]:


print(arrb1[0])


# In[48]:


print(arrb1[0:2])


# In[49]:


print(arrb1[:,2])


# In[50]:


print(arrb1[0:2,0:3])


# In[51]:


#Fancy Indexing (Selecting with lists/arrays)
#You can select multiple rows/columns using lists of indices.
print(arrb1[[0, 2]])      # First & third rows
print(arrb1[:, [0, 2]])   # First & third columns


# In[54]:


#Boolean Indexing (Condition-based selection)
print(arrb1>50)
print(arrb1[arrb1>50])


# In[ ]:




