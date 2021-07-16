#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing all necessary libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# State wise COVID tests file

tests = pd.read_csv("StatewiseTestingDetails.csv")
tests


# In[3]:


# Total cases in india
cases = pd.read_csv("covid_19_india.csv")
cases


# In[4]:


# Total Vaccination details
vaccine = pd.read_csv("covid_vaccine_statewise.csv")
vaccine


# In[5]:


# Checking the column names of tests file
tests.head(4)


# In[6]:


# Checking the column names of Vaccine file

vaccine.head(4)


# In[7]:


# Checking the information of tests file

tests.info()


# In[8]:


# grouping the states in tests file to check the state wise positive cases
state_positive = tests.groupby(["State"]).Positive.sum()


# In[9]:


#plotting the result
state_positive.plot(kind= "hist", figsize = (20,10))


# In[10]:


# Information about the cases file
cases.info()


# In[11]:


# Description about the cases file.
cases.describe()


# In[12]:


# checking the colomns of cases file
cases.head(2)


# In[13]:


# creating a new column "Active" to see the active cases of each state
cases["Active"] = cases.Confirmed - (cases.Cured+cases.Deaths)


# In[14]:


#confirming the change
cases.head(4)


# In[15]:


# Calculating the sum of Active cases
cases.Active.sum()


# In[16]:


#calculating the sum of deaths
cases.Deaths.sum()


# In[17]:


#calcluating the sum of cured
cases.Cured.sum()


# In[18]:


#calculating the sum of confirmed
cases.Confirmed.sum()


# In[19]:


#renaming the state column for easy purpose
cases.rename(columns={"State/UnionTerritory":"State"},inplace=True)


# In[20]:


#confirming the chage
cases.head(2)


# In[21]:


# grouping the states in cases file to check the state wise death cases
# Here taking the max() because the count is the addition of each day

Deaths_Statewise= cases.groupby("State").Deaths.max().sort_values()


# In[22]:


#Plotting the deaths Vs state
Deaths_Statewise.plot(kind="bar",figsize=(15,5))
plt.xlabel("States")
plt.ylabel("No.of Deaths")


# In[23]:


# grouping the states in cases file to check the state wise Active cases

Active_Statewise = cases.groupby("State").Active.max().sort_values()


# In[24]:


#plot
Active_Statewise.plot(kind="bar",figsize=(15,10))


# In[25]:


# grouping the states in cases file to check the state wise cured cases

Cured_Statewise= cases.groupby("State").Cured.max().sort_values()


# In[26]:


#plot
Cured_Statewise.plot(kind="bar",figsize=(15,5),ylim=(0,6000000))


# In[27]:


#changing the date column type from object type to datetime
cases.Date = pd.to_datetime(cases.Date, dayfirst=True)


# In[28]:



# checking the last date of the sample collection
cases.Date.max()


# In[29]:


# To check the cases, deaths and vaccination in 2 years, I sliced the data into first wave and second wave

firstwave = cases.set_index("Date").loc["2020-02-28" : "2020-12-30" ]


# In[30]:


#second wave
Secondwave = cases.set_index("Date").loc["2020-12-30" : "2021-6-30" ]


# In[31]:


#checking the first wave columns
firstwave.head()


# In[32]:


#dropping the unnecessary columns
firstwave.drop(["ConfirmedIndianNational","ConfirmedForeignNational","Time"], axis=1)


# In[33]:


## grouping the states in first wave file to check the state wise death cases

firstwave.groupby("State").Deaths.max().sort_values().plot(kind="bar",figsize=(15,5))


# In[34]:


#calculating the deaths
firstwave.Deaths.max()


# In[35]:


## grouping the states in second wave file to check the state wise deaths cases

Secondwave.groupby("State").Deaths.max().sort_values().plot(kind="bar",figsize=(15,5))


# In[36]:


#calculating the second wave deaths max
Secondwave.Deaths.max()


# In[37]:


#calculating the first wave confirmed max
firstwave.Confirmed.max()


# In[38]:


#calculating the second wave confirmed max
Secondwave.Confirmed.max()


# In[39]:


### grouping the states in first wave file to check the state wise Confirmed cases

firstwave.groupby("State").Confirmed.max().sort_values().plot(kind="bar",figsize=(10,5))


# In[42]:


#checking the tests file again.
tests.head(4)


# In[41]:



#plotting the total samples collected by each state in tests file.
tests.groupby("State").TotalSamples.max().sort_values().plot(kind="bar", figsize=(10,5))


# In[ ]:




