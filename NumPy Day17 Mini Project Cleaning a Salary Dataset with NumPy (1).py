#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Mini Project: Cleaning a Salary Dataset with NumPy


# In[1]:


import numpy as np

# Employee salaries (in USD per month)
salaries = np.array([
    50000, 52000, np.nan, 49000, np.inf, 47000, 0, 51000, -np.inf, 55000, 999999
])

print("Raw Salaries:\n", salaries)


# In[4]:


#Detect Missing / Invalid Values
print("Nan Values:\n",np.isnan(salaries).sum())
print("Infinity Values:\n",np.isinf(salaries).sum())


# In[12]:


#Replace NaN and Infinite Values
mean_val=np.nanmean(salaries[np.isfinite(salaries)])#Compute mean ignoring NaN
salaries[np.isnan(salaries)]=mean_val
salaries[np.isinf(salaries)]=0
print(salaries)


# In[13]:


# Replace NaN with mean of valid numbers
valid = salaries[np.isfinite(salaries)]  # remove inf and nan temporarily
mean_val = np.mean(valid[(valid > 0) & (valid < 200000)])  # avoid extreme outliers
salaries[np.isnan(salaries)] = mean_val

# Replace inf and -inf with 0
salaries[np.isinf(salaries)] = 0

print("After replacing NaN and Inf:\n", salaries)


# In[19]:


#Handle Outliers
#Sometimes data looks valid but isn’t realistic — like 999999
# Define a realistic salary range (example: 10,000–200,000)
clean_salaries=salaries[(salaries>=10000) & (salaries<=200000)] 
print("Clean Salaries:\n", clean_salaries)


# In[20]:


#Basic Insights After Cleaning
print("Mean of data",np.mean(clean_salaries))
print("Median of data",np.median(clean_salaries))
print("Standard deviation",np.std(clean_salaries))


# In[ ]:





# In[1]:


#example two
import numpy as np

# Simulated messy salary data (some missing, invalid, or extreme values)
salaries = np.array([35000, 48000, np.nan, 52000, -999, 61000, 200000, 47000, 0, 56000])
print("Original:", salaries)


# In[2]:


print(np.isnan(salaries))


# In[4]:


print(~np.isnan(salaries)) #negate or flips


# In[11]:


# Detect NaN values
print(np.isnan(salaries))

# Detect impossible or invalid values (like negatives or placeholders)
invalid_mask = (salaries < 10000) | (salaries > 150000)
print(invalid_mask)


# In[17]:


# Replace NaN and invalid with median or mean
valid_salaries = salaries[~np.isnan(salaries) & ~invalid_mask]
print("valid salaries",valid_salaries)
mean_salary = np.mean(valid_salaries)
print("Mean",mean_salary)
cleaned_salaries = np.where(np.isnan(salaries) | invalid_mask, mean_salary, salaries)
print("Cleaned salaries:", cleaned_salaries)


# In[22]:


mean = np.mean(cleaned_salaries)
std = np.std(cleaned_salaries)
print("Mean",mean)
print("standard deviations",std)
# Define outliers as values beyond 2 standard deviations
outlier_mask = (cleaned_salaries > mean + 2*std) | (cleaned_salaries < mean - 2*std)
print("Outliers:", cleaned_salaries[outlier_mask])

# Replace outliers with mean
cleaned_salaries[outlier_mask] = mean
print("Final Cleaned Data:", cleaned_salaries)


# In[ ]:




