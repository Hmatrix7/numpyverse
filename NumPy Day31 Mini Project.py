#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd

data = pd.read_csv("sales_data.csv",skiprows=1)
print(data)


# In[14]:


import pandas as pd

# Load data
data = pd.read_csv("sales_data.csv")

# Calculate Revenue
data["Revenue"] = data["Price"] * data["UnitsSold"]

print(data.head())  # Preview with revenue


# In[16]:


# Group by product and sum revenue
product_revenue = data.groupby("ProductName")["Revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Product:")
print(product_revenue)

# Top product
top_product = product_revenue.idxmax()
top_revenue = product_revenue.max()

print(f"\n Top Product: {top_product} — Revenue: {top_revenue}")


# In[ ]:




