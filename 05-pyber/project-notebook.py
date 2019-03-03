
# coding: utf-8

# # Pyber Ride Sharing

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[2]:


city_data_to_load = "data/city_data.csv"
ride_data_to_load = "data/ride_data.csv"


# In[3]:


# City Data
city_data = pd.read_csv(city_data_to_load)
city_data.head()


# In[4]:


# Ride Data
ride_data = pd.read_csv(ride_data_to_load)
ride_data.head()


# In[5]:


# Merge dataset
combine_city_ride_data = pd.merge(ride_data, city_data, on=["city", "city"])


# In[6]:


combine_city_ride_data.head()


# # Create Bubble Plot

# In[7]:


urban_cities = combine_city_ride_data.loc[combine_city_ride_data["type"] == "Urban"]
suburban_cities = combine_city_ride_data.loc[combine_city_ride_data["type"] == "Suburban"]
rural_cities = combine_city_ride_data.loc[combine_city_ride_data["type"] == "Rural"]


# In[8]:


from helper import *


# In[9]:


urban_ride_count, urban_avg_fare, urban_driver_count = get_ride_count_avg_fare_and_driver_count_by_city(urban_cities)
suburban_ride_count, suburban_avg_fare, suburban_driver_count = get_ride_count_avg_fare_and_driver_count_by_city(suburban_cities)
rural_ride_count, rural_avg_fare, rural_driver_count = get_ride_count_avg_fare_and_driver_count_by_city(rural_cities)


# In[10]:


plt.scatter(
    urban_ride_count, 
    urban_avg_fare, 
    s=10*urban_driver_count,
    c="coral", 
    edgecolor="black",
    linewidths=1,
    marker="o", 
    alpha=0.8,
    label="Urban"
)
plt.scatter(
    suburban_ride_count, 
    suburban_avg_fare, 
    s=10*suburban_driver_count,
    c="skyblue", 
    edgecolor="black",
    linewidths=1,
    marker="o", 
    alpha=0.8,
    label="Urban"
)
plt.scatter(
    rural_ride_count, 
    rural_avg_fare, 
    s=10*rural_driver_count,
    c="gold", 
    edgecolor="black",
    linewidths=1,
    marker="o", 
    alpha=0.8,
    label="Urban"
)
plt.title("Pyber Ride Sharing Data (2016)")
plt.ylabel("Average Fare ($)")
plt.xlabel("Total Number of Rides (Per City)")
plt.grid(True)
lgnd = plt.legend(
    fontsize="small",
    mode="Expanded", 
    numpoints=1,
    scatterpoints=1, 
    loc="best",
    title="City Types", 
    labelspacing=0.5
)
lgnd.legendHandles[0]._sizes = [40]
lgnd.legendHandles[1]._sizes = [40]
lgnd.legendHandles[2]._sizes = [40]
plt.text(43, 30, "Note:\nCircle size correlates with driver count per city.")
plt.show()


# # Total Fares by City Type

# In[11]:


total_fare = combine_city_ride_data.sum()['fare']


# In[12]:


fare_percentage_by_type = combine_city_ride_data.groupby(['type']).sum()['fare']/total_fare
fare_percentage_by_type


# In[13]:


plt.pie(
    fare_percentage_by_type, 
    labels=["Rural", "Suburban", "Urban"], 
    colors=["gold", "lightskyblue", "lightcoral"], 
    explode=[0, 0, 0.1], 
    autopct='%1.1f%%', 
    shadow=True,
    startangle=150
)
plt.title("% of Total Fares by City Type")

plt.show()

