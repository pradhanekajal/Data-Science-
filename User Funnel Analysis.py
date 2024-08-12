#!/usr/bin/env python
# coding: utf-8

# # To Analyze the user Funnel by using the python 
# #User Funnel Analysis - a way to understand how users interact with a website or an application. 
# #By tracking user flow as they move through various stages of the funnel, companies can identify areas where users are giving up or getting stuck.
# #This enables them to take action to improve user experience and increase conversion. 
# #For example, if a lot of users leave the website after adding items to the cart, the company may look for ways to make the checkout process faster and easier.

# In[7]:


import pandas as pd

# Specify the file path where 'CardioGoodFitness.csv' is located
file_path = 'C:\\Users\\RENT IT\\Downloads\\user_data.csv'

data = pd.read_csv(file_path)


# In[9]:


# Get the number of rows in the DataFrame (length of the CSV data file)
file_length = len(data)

print("Length of the CSV data file:", file_length)


# In[10]:


print(data.head())


# In[ ]:


#The stage column contains the stages of the flow of the users. 
#For example, when you visit Amazon, the first stage will be the homepage of Amazon, 
#and the last page will be the page where you proceed with the payment.


#So, let’s have a look at the stages in this dataset:


# In[14]:


print(data["stage"].value_counts())


# In[ ]:


#Homepage & Product


# In[17]:


import plotly.graph_objects as go
import plotly.io as pio

# Set the default template using the plotly.io.templates configuration object
pio.templates.default = "plotly_white"



# In[18]:


#Define the Funnel Stages

funnel_stages = ['homepage', 'product_page', 'cart', 'checkout', 'purchase']


# In[20]:


#Number of Users

#calculate the number of users and conversions for each stage
num_users = []
num_conversions = []

for stage in funnel_stages:
    stage_users = data[data['stage']==stage]
    num_users.append(len(stage_users))
    num_conversions.append(stage_users['conversion'].sum())


# In[21]:


#Funnel Chart

#create a funnel chart
fig = go.Figure(go.Funnel(
    y=funnel_stages,
    x=num_users,
    textposition='inside',
    textinfo='value',
    name='Users'
))

fig.add_trace(go.Funnel(
    y=funnel_stages,
    x=num_conversions,
    textposition='inside',
    textinfo='value',
    name='Conversions'
))

fig.update_layout(
    title='Funnel Analysis',
    funnelmode = 'stack'
)

fig.show()


# In[ ]:


# From Above Analysis we can see the users on home page is quit volatile.
#from homepage to purchase the conversion is 1.3% only 
# as per my point of view to increase the conversion rate we can do promotions,
#AB testing or may be some new product launch.

