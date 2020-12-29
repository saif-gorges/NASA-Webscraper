#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import dependies
from bs4 import BeautifulSoup as bs
import requests
import json
import splinter


# In[2]:


#execute chrome driver
executable_path = {'executable_path' : 'chromedriver.exe'}
browser = splinter.Browser('chrome', **executable_path)
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
html = browser.html


# In[3]:


#load page in bs
soup = bs(html, 'html.parser')
print(soup.prettify())


# In[4]:


#extract title
content = soup.find('div', class_ = 'content_page')
titles = content.find_all('div',class_ = 'content_title')
print(titles[0].text.strip())


# In[5]:


#extract paragraph
p_results = soup.find_all("div", class_ = "article_teaser_body")
p_results[0].text


# In[6]:


#visit url with splinter
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html = browser.html


# In[7]:


#use bs to get url
soup = bs(html, 'html.parser')
featured_img = soup.find('article', class_ = 'carousel_item')['style']


# In[8]:


#build URL
second = featured_img.split('/spaceimages')[1].split("''")[0]
second
first = url.split('?')[0]
final = first + second
final


# In[ ]:




