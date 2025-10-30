#!/usr/bin/env python
# coding: utf-8

# In[13]:


#pandas doesn’t show every row by default… it just gives you a “preview”.

#df.head() → first 5 rows
#df.tail() → last 5 rows
#df.sample() → random rows

#This is actually super helpful when datasets are big!


# In[28]:


import pandas as pd

df = pd.read_csv("sales_data.csv")
print(df.head())#df.head() → first 5 rows
print(df.tail())#df.tail() → last 5 rows
print(df.sample())#df.sample() → random rows


# In[15]:


#⚠️ Only do that if your dataset is small (like ours — 20 rows)
#to see all the data
print(df.to_string())


# In[16]:


pd.set_option('display.max_rows', 12)
print(df)


# In[17]:


#Just to confirm… your file still has 20 rows
df.shape


# In[18]:


import numpy as np

data = np.loadtxt("numeric_data.csv", delimiter=",")
print(data)


# In[37]:


max_index = np.argmax(revenue)
print("Top Performer:", data[max_index], "Revenue:", revenue[max_index])


# In[19]:


print(data.shape)


# In[20]:


#Get the average of column 2
print(np.mean(data[:, 1]))


# In[21]:


#Select the last 3 rows
print(data[-3:])


# In[22]:


#Skip Header Row
data =np.loadtxt("numeric_data.csv",delimiter=",",skiprows=1)
print(data)


# In[23]:


#Saving Data to File
np.savetxt("clean_sales.csv", data, delimiter=",")


# In[35]:


units_sold = data[:, 3]
price = data[:, 2]

revenue = price * units_sold
print("Revenue:", revenue[:5])


# In[36]:


max_index = np.argmax(revenue)
print("Top Performer:", data[max_index], "Revenue:", revenue[max_index])


# In[ ]:




