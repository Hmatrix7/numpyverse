#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Objectives
By the end of this session, you’ll be able to:

Change the shape of arrays using reshape() and ravel().

Combine arrays using stacking and concatenation.

Split arrays into smaller parts.

Apply these to real-world data organization


# In[ ]:





# In[4]:


#reshape() changes shape
#ravel() flattens back to 1D
import numpy as np

arr = np.arange(12)
print("Original:", arr)

reshaped = arr.reshape(3, 4)
print("\nReshaped to 3x4:\n", reshaped)


# In[5]:


flat = reshaped.ravel()
print("\nFlattened back:\n", flat)


# In[41]:


arr=np.arange(10)
print("arange",arr)
reshape=arr.reshape(2,5)
print("reshape\n",reshape)
flat=reshape.ravel()
print("flat",flat)


# In[46]:


#Stacking Arrays (Combining Data)
#Horizontal (side by side)
a=np.array([[1,2,3,4]])
b=np.array([[5,6,7,8]])
h_stack=np.hstack((a,b))#flattened using np.hstack
print(h_stack)
c=np.array([[1,2], [3,4]])
d=np.array([[5,6], [7,8]])
v_stack=np.vstack((c,d))
print(v_stack)
flattened=v_stack.ravel()#flattened using ravel
print(flattened)


# In[30]:


#Concatenation (Flexible Combination)
#You can join arrays along any axis
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

combined = np.concatenate((a, b), axis=0)
print(combined)


# In[31]:


#Mini Real Example – Combining Monthly Sales Data
jan_sales = np.array([120, 130, 125])
feb_sales = np.array([140, 135, 150])
mar_sales = np.array([160, 155, 165])

# Stack monthly sales
quarter1 = np.vstack((jan_sales, feb_sales, mar_sales))
print("Q1 Sales:\n", quarter1)

# Add total sales column
totals = np.sum(quarter1, axis=1).reshape(3, 1)
final_data = np.hstack((quarter1, totals))
print("\nWith Totals:\n", final_data)


# In[32]:


import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

combined = np.concatenate((a, b), axis=0)
flattened = combined.ravel()

print(flattened)


# In[44]:


import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
b=np.array([[7,8],[9,0]])
combined=np.concatenate((a,b),axis=0)
print("combined\n",combined)
flattened=combined.ravel()
print("flattened",flattened)


# In[ ]:




