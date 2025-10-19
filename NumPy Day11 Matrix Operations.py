#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Matrix Addition & Subtraction
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Addition:\n", A + B)
print("Subtraction:\n", A - B)


# In[ ]:


#Matrix Multiplication
#There are two types:
#Element-wise multiplication → A * B
#Matrix multiplication (dot product) → A @ B or np.dot(A, B)


# In[2]:


print("Element-wise multiplication:\n", A * B)
print("Matrix multiplication:\n", A @ B)


# In[3]:


#Transpose of a Matrix
#Swaps rows and columns.
print("Transpose of A:\n", A.T)


# In[4]:


#Matrix Inverse & Determinant
#(Only valid for square matrices)
print("Determinant of A:", np.linalg.det(A))
print("Inverse of A:\n", np.linalg.inv(A))


# In[9]:


#Identity Matrix
#Definition:
#An Identity Matrix is a square matrix (same number of rows and columns) that has:
#All 1’s on the main diagonal (from top-left to bottom-right),
#All 0’s everywhere else
#When you multiply any matrix  A by the identity matrix I, it doesn’t change A*1=A
#A Zero Matrix (also called Null Matrix) is a matrix where all elements are 0
#Property:When you add or multiply a zero matrix: A+0=A, A*0=0


# In[10]:


#Identity & Zero Matrices
I = np.eye(3)     # 3x3 Identity matrix
Z = np.zeros((3,3))
print("Identity Matrix:\n", I)
print("Zero Matrix:\n", Z)


# In[ ]:




