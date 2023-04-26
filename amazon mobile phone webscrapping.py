#!/usr/bin/env python
# coding: utf-8

# This notebook is about the usage of requests and beautifulsoap to scrap data from amazon website and create a csv file out of it. For now, i have worked on one data only, in future will plan to work on many more data. One problem i found with this project, was that the class names were the same and hence i couldnt retrieve the data easily.

# In[1]:


import requests
from bs4 import BeautifulSoup
import csv


# In[10]:


headers= { 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
  }
a=requests.get('https://www.amazon.in/Samsung-Storage-Battery-Octa-Core-Processor/dp/B0BZCWLJHK/',headers=headers)
print(a.status_code)


# In[13]:


soup=BeautifulSoup(a.content,'html.parser')


# In[86]:


price=soup.find(class_='a-price-whole').get_text()
discount_per=soup.find(class_="a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage").get_text()[1:]
OS=soup.find(class_="a-size-base prodDetAttrValue").get_text()
cc=soup.find(id='productTitle').get_text().strip()
name=(cc[0:20])
color=(cc[23:33])
ram=(cc[34:38])
storage=(cc[39:53])
cam=(cc[57:72])
battery=(cc[74:92])
dd=soup.find('span',class_='a-list-item').get_text()
cat=dd.strip()
ee=soup.find('div',class_='a-section brand-snapshot-flex-badges-section').get_text().strip()
pos_reviews=(ee[13:17])
recent_orders=(ee[60:64])


# In[88]:


head=['name','color','ram','storage','camera clarity (megapixels)','battery storage (MAh)','category','positive review %','recent orders (K)','discount %','price']
data=[name,color,ram,storage,cam,battery,cat,pos_reviews, recent_orders,discount_per,price]
with open('mobile_phone_data_scrapped.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(head)
    w.writerow(data)

