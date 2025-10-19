#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Basic Mathematical Functions
Function	Description	Example
np.add(a, b)	Element-wise addition	np.add([1,2], [3,4]) → [4,6]
np.subtract(a, b)	Subtraction	np.subtract([5,6], [2,3]) → [3,3]
np.multiply(a, b)	Multiplication	np.multiply([2,3], [4,5]) → [8,15]
np.divide(a, b)	Division	np.divide([10,20], [2,4]) → [5,5]
np.power(a, b)	Exponentiation	np.power([2,3], 2) → [4,9]
np.sqrt(a)	Square root	np.sqrt([4,9]) → [2,3]
np.exp(a)	Exponential	np.exp([1,2]) → [2.718, 7.389]
np.log(a)	Natural log	np.log([1, np.e, np.e**2]) → [0,1,2]


# In[ ]:


Trigonometric Functions
Function	Description
np.sin(x)	Sine
np.cos(x)	Cosine
np.tan(x)	Tangent
np.degrees(x)	Convert radians → degrees
np.radians(x)	Convert degrees → radians


# In[2]:


import numpy as np
angles=np.array([0, 30, 45, 60, 90])
radians=np.radians(angles)

print("Sine:", np.sin(radians))
print("Cosine:", np.cos(radians))
print("Tangent:", np.tan(radians))


# In[ ]:




