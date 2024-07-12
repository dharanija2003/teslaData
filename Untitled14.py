#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install yfinance


# In[4]:


import yfinance as yf

# Extract Tesla stock data
tesla = yf.Ticker('TSLA')
tesla_data = tesla.history(period='1y')
tesla_data.reset_index(inplace=True)
print(tesla_data.head())


# In[8]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Adjust the selector based on the actual page structure
revenue_data = soup.find('selector_for_revenue')  # Change selector accordingly
tesla_revenue = pd.DataFrame(revenue_data)  # Example conversion to DataFrame
print(tesla_revenue.tail())


# In[9]:


gamestop = yf.Ticker('GME')
gme_data = gamestop.history(period='1y')
gme_data.reset_index(inplace=True)
print(gme_data.head())


# In[10]:


url = 'https://gamestop.gcs-web.com/news-releases/news-release-details/gamestop-discloses-first-quarter-2024-results'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

revenue_data = soup.find('selector_for_revenue')  # Change selector accordingly
gme_revenue = pd.DataFrame(revenue_data)  # Example conversion to DataFrame
print(gme_revenue.tail())


# In[12]:


import matplotlib.pyplot as plt

def make_graph(data, title):
    plt.figure(figsize=(10,5))
    plt.plot(data['Date'],data['Close'],label='Tesla Stock Price')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

make_graph(tesla_data,'Tesla Stock Price Over Time')


# In[13]:


make_graph(gme_data, 'GameStop Stock Price Over Time')


# In[ ]:




