#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
def fetch_title(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string
        return title
    else:
        return f"Error: Unable to fetch the page (status code: {response.status_code})"

url = 'https://example.com'
title = fetch_title(url)
print(f"Title of the webpage: {title}")


# In[ ]:




