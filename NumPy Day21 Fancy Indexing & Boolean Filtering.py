#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Fancy Indexing (Indexing using lists/arrays)
#You can pass lists of indices to grab multiple elements at once
import numpy as np
arr=np.array([10,20,30,40,50,60,70,80])
idx=[0,2,4]
print(arr[idx])


# In[2]:


arr=np.array([[0,1,2],
             [3,4,5],
             [7,8,9]])
row=[0,2]
col=[1,2]
print(row,col)


# In[3]:


#This pairs them:
#Picks element at (0,1) → 6
#Picks element at (2,0) → 9
matrix = np.array([[5, 6, 7],
                   [1, 2, 3],
                   [9, 8, 4]])

rows = [0, 2]
cols = [1, 0]

print(matrix[rows, cols])


# In[4]:


#boolean Indexing — Filter values based on conditions
arr=np.array([2,4,5,6,7,3,9])
mask=arr>4
print(mask)
print(arr[mask])


# In[5]:


arr = np.array([3, 10, 15, 20, 25, 2])

mask = arr > 10
print(mask)
print(arr[mask])


# In[6]:


#Replace values using Boolean Indexing
arr = np.array([3, 10, 15, 20, 25, 2])
arr[arr < 10] = -1
print(arr)


# In[7]:


#task
sales = np.array([120, 45, 200, 90, 150, 30])
#Show only sales ≥ 100
mask = sales >=100
print(sales[mask])


# In[8]:


#Replace grades below 50 with 0
grades = np.array([50, 75, 85, 40, 92, 67, 30])
grades[grades<50]=0
print(grades)


# In[9]:


print(arr[(arr > 5) & (arr < 20)])


# In[ ]:




