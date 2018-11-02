
# coding: utf-8

# # Step 1 - Scraping
# 
#  - Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
#  - Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.
# 

# ## NASA Mars News
#  - Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

# In[1]:


import splinter
from bs4 import BeautifulSoup as bs
from splinter import Browser


# In[2]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[4]:


html = browser.html
soup = bs(html, 'html.parser')


# In[5]:


# save latest news attributes to variables.
import time
time.sleep(10)
article = soup.find("div", class_="list_text")
time.sleep(10)
teaser = article.find("div", class_="article_teaser_body").text
title = article.find("div", class_="content_title").text
date = article.find("div", class_="list_date").text

print(f'Article Date:  {date}')
print(f'Article Title:  {title}')
print(f'Article Teaser:  {teaser}')


# ## Mars Space Images - Featured Image
# 
#  - Visit the url for JPL Featured Space Image here.
#  - Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
#  - Make sure to find the image url to the full size .jpg image.
#  - Make sure to save a complete url string for this image.

# In[6]:


url = "https://jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)


# In[7]:


html = browser.html
soup = bs(html, 'html.parser')


# In[8]:


image = soup.find("img", class_="thumb")["src"]
featured_image_url = "https://jpl.nasa.gov"+image


# In[9]:


import requests
import shutil

response = requests.get(featured_image_url, stream=True)
with open('img.jpg', 'wb') as image_file:
    shutil.copyfileobj(response.raw, image_file)
    
# Display the image with IPython.display
from IPython.display import Image
Image(url='img.jpg')    


# In[10]:


print(featured_image_url)


# ## Mars Weather
# 
#  - Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.
# 
# 
# 

# In[11]:


import tweepy
from config import consumer_key, consumer_secret, access_token, access_token_secret


# In[12]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[13]:


target_user = "@MarsWxReport"
tweet = api.user_timeline(target_user , count = 1)

mars_weather=tweet[0]['text']
print(mars_weather)


# ## Mars Facts
#  - Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
#  - Use Pandas to convert the data to a HTML table string.

# In[14]:


import pandas as pd 


# In[15]:


url = "http://space-facts.com/mars/"
browser.visit(url)


# In[16]:


mars_df = pd.read_html(url)
mars_df = mars_df[0]

#type(mars_df)


# In[17]:


#mars_df.head()


# In[18]:


#convert to html table string
table = mars_df.to_html()
print("table created")


# ## Mars Hemispheres
# 
#  - Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
#  - You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
#  - Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
#  - Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
# 
# 
# 

# In[19]:


import time 
from splinter.exceptions import ElementDoesNotExist

url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)


# In[20]:


html = browser.html
soup = bs(html, 'html.parser')


# In[21]:


hemisphere = []

for i in range (4):
    time.sleep(8)
    image = browser.find_by_tag('h3')
    image[i].click()
    html = browser.html
    soup = bs(html, 'html.parser')
    istring = soup.find("img", class_="wide-image")["src"]
    img_title = soup.find("h2",class_="title").text
    img_url = 'https://astrogeology.usgs.gov'+ istring
    dictionary={"title":img_title,"img_url":img_url}
    hemisphere.append(dictionary)
    browser.back()   


# In[22]:


print(hemisphere)

