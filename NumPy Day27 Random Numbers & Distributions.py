#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#NumPy gives us np.random for
#Random integers
#Random floats
#Choosing random samples
#Probability distributions
#Setting a seed for reproducibility


# In[1]:


import numpy as np
#Random integers
print(np.random.randint(1, 10))        # single value
print(np.random.randint(1, 10, size=5))  # array


# In[3]:


#Random floats
print(np.random.rand(4))     # 1D
print(np.random.rand(2,3))   # 2D


# In[6]:


#Probability distributions
#loc = mean
#Used for most statistical models!
#scale = standard deviation
normal_data = np.random.normal(loc=50, scale=10, size=5)
print(normal_data)


# In[7]:


#Choosing random samples
choices = np.random.choice([1, 2, 3, 4], size=3)
print(choices)


# In[9]:


#With probabilities
choices = np.random.choice([0, 1], size=10, p=[0.7, 0.3])
print(choices)


# In[12]:


#Reproducibility — set a seed
np.random.seed(42)
print(np.random.rand(3))


# In[13]:


#Shuffle data (useful in ML train/test split)
arr = np.array([1,2,3,4,5])
np.random.shuffle(arr)
print(arr)


# In[14]:


#Mini Challenges 
#Generate a 5x5 matrix of random integers from 10 to 99
import numpy as np
arr=np.random.randint(10,99, size=(5,5))
print(arr)


# In[ ]:


#Create 50 student scores (normal distribution) with
#mean = 70

#std = 12
#Then print:
#min score
#max score
#average score


# In[29]:


normal_data=np.random.normal(loc=70,scale=12,size=50)
print(normal_data)
print(np.round( np.max(normal_data)))
print(np.round( np.min(normal_data)))
print(np.round( np.mean(normal_data)))
print(np.max(normal_data))
print(np.min(normal_data))
print(np.mean(normal_data))


# In[27]:


import numpy as np

# Generate scores
scores = np.random.normal(loc=70, scale=12, size=50)

# Print min, max, and mean values
print("Min score:",np.round( np.min(scores)))
print("Max score:", np.round(np.max(scores)))
print("Average score:",np.round( np.mean(scores)))


# In[25]:


#If you want scores to look like real exam values (no decimals + within 0–100 range)
scores = np.clip(np.round(scores), 0, 100)
print(scores)


# In[ ]:


Q3
Given:

teams = np.array(["A", "B", "C", "D"])

Randomly select 10 teams with probabilities:

A: 40%

B: 30%

C: 20%

D: 10%


# In[30]:


import numpy as np

teams = np.array(["A", "B", "C", "D"])
probabilities = [0.4, 0.3, 0.2, 0.1]

selection = np.random.choice(teams, size=10, p=probabilities)
print(selection)


# In[33]:


Assets=np.array(["UCHUM","LBRT","SCOM","KENG"])
Probabilities=[0.1,0.2,0.3,0.4]
selection=np.random.choice(Assets,size=10, p=Probabilities)
print(selection)


# In[ ]:




