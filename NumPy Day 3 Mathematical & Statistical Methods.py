#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#sum() → sum of elements
#mean() → average
#min() / .max() → minimum & maximum
#std() / .var() → standard deviation & variance


# In[2]:


import numpy as np


# In[2]:


arr=np.array([10,20,30,40,50])


# In[5]:


print("sum",arr.sum())
print("max",arr.max())
print("min",arr.min())


# In[7]:


print("Mean",arr.mean())
print("standard deviation",arr.std())
print("variance",arr.var())


# In[12]:


#Row-wise and column-wise operations
arr2=np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print("Column sums:", arr2.sum(axis=0))  
print("Row sums:", arr2.sum(axis=1))    


# In[4]:


#Median and Percentiles
data=np.array([7, 8, 5, 6, 9, 10, 15])
print(np.median(data))
print(np.percentile(data,25))
print(np.percentile(data,75))
print(np.percentile(data,50))


# In[18]:


#mini real-world dataset challenge
import numpy as np

scores = np.array([[78, 85, 90],   # Student 1
                   [88, 92, 76],   # Student 2
                   [94, 70, 80],   # Student 3
                   [65, 95, 85],   # Student 4
                   [70, 88, 89]])  # Student 5


# In[23]:


#Find the average score for each subject.
print("average score for each subject",scores.mean(axis=0))


# In[24]:


##Find the average score for each student.
print("average score for each student",scores.mean(axis=1))


# In[25]:


#Find the highest score in each subject.
print("highest score in each subject",scores.max(axis=0))


# In[26]:


#Which student has the highest overall average?
# Step 1: Calculate average per student (row-wise)
student_avg = scores.mean(axis=1)
print("Student averages:", student_avg)

# Step 2: Find the highest average
highest_avg = student_avg.max()
print("Highest average:", highest_avg)

# Step 3: Find which student(s) has this highest average
top_student = np.argmax(student_avg) + 1   # +1 to match student number
print("Top student:", top_student)


# In[32]:


#mean across subjects and students
print("mean across subjects",scores.mean(axis=0))
print("mean across students",scores.mean(axis=1))


# In[33]:


#What is the median score across all students and subjects?
median_score = np.median(scores)
print("Median score:", median_score)


# In[ ]:




