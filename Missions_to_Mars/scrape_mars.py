#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import dependies
from bs4 import BeautifulSoup as bs
import requests
import json
import splinter
import pandas as pd


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
news_title = titles[0].text.strip()
news_title


# In[5]:


#extract paragraph
p_results = soup.find_all("div", class_ = "article_teaser_body")
news_p = p_results[0].text
news_p


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
featured_image_url = first + second
featured_image_url


# In[9]:


#visit url with splinter
url = 'https://space-facts.com/mars/'
browser.visit(url)
html = browser.html


# In[10]:


#load page in bs
soup = bs(html, 'html.parser')
print(soup.prettify())


# In[11]:


#extract and append table to pandas
    #define tables
mars_data_col1 = []
mars_data_col2 = []

#extract and append col1
chart1 = soup.find_all("td", class_ = "column-1")

for i in range(9):
    mars_data_col1.append(chart1[i].text)
    
#extract and append col2
chart2 = soup.find_all("td", class_ = "column-2")

for i in range(9):
    mars_data_col2.append(chart2[i].text)
    
#zip table
mars_data = pd.DataFrame(zip(mars_data_col1,mars_data_col2))


# In[12]:


#display table
mars_data


# In[19]:


#CERBERUS

#visit url with splinter
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
browser.visit(url)
html = browser.html

#load page in bs
soup = bs(html, 'html.parser')
print(soup.prettify())

#extract title
title1 = soup.find_all("h2", class_ = "title")
cerb_title = title1[0].text
cerb_title

#extract url
link1 = soup.find_all("a", target = "_blank")
cerb_link = link1[4]
cerb_link


# In[20]:


#SCHIAPARELLI

#visit url with splinter
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
browser.visit(url)
html = browser.html

#load page in bs
soup = bs(html, 'html.parser')
print(soup.prettify())

#extract title
title2 = soup.find_all("h2", class_ = "title")
sch_title = title2[0].text
sch_title

#extract url
link2 = soup.find_all("a", target = "_blank")
sch_link = link2[4]
sch_link


# In[23]:


#SYRTIS

#visit url with splinter
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
browser.visit(url)
html = browser.html

#load page in bs
soup = bs(html, 'html.parser')
print(soup.prettify())

#extract title
title3 = soup.find_all("h2", class_ = "title")
sy_title = title3[0].text
sy_title

#extract url
link3 = soup.find_all("a", target = "_blank")
sy_link = link3[4]
sy_link


# In[26]:


#VALL

#visit url with splinter
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
browser.visit(url)
html = browser.html

#load page in bs
soup = bs(html, 'html.parser')
print(soup.prettify())

#extract title
title4 = soup.find_all("h2", class_ = "title")
vall_title = title4[0].text
vall_title

#extract url
link4 = soup.find_all("a", target = "_blank")
vall_link = link4[4]
vall_link


# In[29]:


#create dictionary

hemisphere_image_urls = [
    {"title": cerb_title, "img_url": cerb_link},
    {"title": sch_title, "img_url": sch_link},
    {"title": sy_title, "img_url": sy_link},
    {"title": vall_title, "img_url": vall_link},
]


# In[30]:


hemisphere_image_urls


# In[ ]:




