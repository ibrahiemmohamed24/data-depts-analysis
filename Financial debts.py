#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

# Data
data = {
    "Name": ["mr mahmoud", "omar fares", "aymen adel", "eng esraa", "mohra atia"],
    "Year": [2021, 2021, 2018, 2021, 2021],
    "Old Loan": [400, 100, 23, 1100, 1750],
    "Price of Gold in the Past": [780, 780, 600, 780, 780]
}

# Create DataFrame
df = pd.DataFrame(data)

# Current price of gold
current_gold_price = 3250

# Calculate New Loan
df["New Loan"] = df["Old Loan"] * current_gold_price / df["Price of Gold in the Past"]
df["Price of Gold Now"] = current_gold_price

# Display the DataFrame
print(df)


# In[7]:


# Adding exchange rate columns and calculating loan values in USD
exchange_rates_past = {2018: 16, 2021: 19}
current_exchange_rate = 47

df["Exchange Rate in the Past"] = df["Year"].map(exchange_rates_past)
df["Old Loan in USD"] = df["Old Loan"] / df["Exchange Rate in the Past"]
df["New Loan in USD"] = df["New Loan"] / current_exchange_rate
df["Current Exchange Rate"] = current_exchange_rate


# In[8]:


# Print the DataFrame with the new changes
print(df)


# In[9]:


# Calculate the new loan amount in EGP
df["New Loan in EGP"] = df["New Loan in USD"] * current_exchange_rate

# Print the DataFrame with the new changes
print(df)


# In[10]:


# Adding exchange rate columns and calculating loan values in USD
exchange_rates_past = {2018: 16, 2021: 19}
current_exchange_rate = 47

df["Exchange Rate in the Past"] = df["Year"].map(exchange_rates_past)
df["Old Loan in USD"] = df["Old Loan"] / df["Exchange Rate in the Past"]
df["New Loan in USD"] = df["Old Loan in USD"]
df["New Loan in EGP"] = df["New Loan in USD"] * current_exchange_rate
df["Current Exchange Rate"] = current_exchange_rate

# Print the DataFrame with the new changes
print(df)


# In[11]:


# Remove the column "Old Loan in USD"
df.drop(columns=["Old Loan in USD"], inplace=True)

# Print the DataFrame without the removed column
print(df)


# In[12]:


# Define the desired column order
desired_columns = ["Name", "Year", "Old Loan", "Price of Gold in the Past", "Price of Gold Now", "New Loan", "Exchange Rate in the Past", "Current Exchange Rate", "New Loan in USD", "New Loan in EGP"]

# Reorder the columns in the DataFrame
df = df[desired_columns]

# Print the arranged DataFrame
print(df)


# In[13]:


# Rename a single column in the DataFrame
df = df.rename(columns={"New Loan": "New Loan by Gold"})

# Print the DataFrame with the renamed column
print(df)


# In[ ]:




