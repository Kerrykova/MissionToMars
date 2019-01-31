#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup


# In[2]:


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# In[8]:


def scrape():
    browser = init_browser()
    mars_news = {}

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    mars = soup.find("div", class_="bottom_gradient")
    news_title = mars.find_all("h3")[0].text
    news_p = soup.find("div", class_="rollover_description_inner").get_text()
    
        # Store data in a dictionary
    mars_news = {
        "news_title": news_title,
        "news_p": news_p,
    }

    browser.quit()
    
    return mars_news


# In[ ]:




