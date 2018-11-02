
# Step 1 - Scraping

 - Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
 - Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.


## NASA Mars News
 - Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.


```python
import splinter
from bs4 import BeautifulSoup as bs
from splinter import Browser
```


```python
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
```


```python
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
```


```python
html = browser.html
soup = bs(html, 'html.parser')
```


```python
# save latest news attributes to variables.

article = soup.find("div", class_="list_text")
teaser = article.find("div", class_="article_teaser_body").text
title = article.find("div", class_="content_title").text
date = article.find("div", class_="list_date").text

print(f'Article Date:  {date}')
print(f'Article Title:  {title}')
print(f'Article Teaser:  {teaser}')
```

    Article Date:  July 25, 2018
    Article Title:  JPL's 'Martians' Are Coming to Griffith Observatory
    Article Teaser:  On July 30, when Mars and Earth are closer than they've been since 2003, JPL scientists and engineers will be at a free public event at Griffith Observatory in Los Angeles.
    

## Mars Space Images - Featured Image

 - Visit the url for JPL Featured Space Image here.
 - Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
 - Make sure to find the image url to the full size .jpg image.
 - Make sure to save a complete url string for this image.


```python
url = "https://jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)
```


```python
html = browser.html
soup = bs(html, 'html.parser')
```


```python
image = soup.find("img", class_="thumb")["src"]
featured_image_url = "https://jpl.nasa.gov"+image
```


```python
import requests
import shutil

response = requests.get(featured_image_url, stream=True)
with open('img.jpg', 'wb') as image_file:
    shutil.copyfileobj(response.raw, image_file)
    
# Display the image with IPython.display
from IPython.display import Image
Image(url='img.jpg')    
```




<img src="img.jpg"/>




```python
print(featured_image_url)
```

    https://jpl.nasa.gov/spaceimages/images/wallpaper/PIA22608-640x350.jpg
    

## Mars Weather

 - Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.





```python
import tweepy
from config import consumer_key, consumer_secret, access_token, access_token_secret
```


```python
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
```


```python
target_user = "@MarsWxReport"
tweet = api.user_timeline(target_user , count = 1)

mars_weather=tweet[0]['text']
print(mars_weather)
```

    Radar analysis from the Mars Express orbiter indicates liquid water beneath the Planum Australe region.… https://t.co/w8dh3RJOST
    

## Mars Facts
 - Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
 - Use Pandas to convert the data to a HTML table string.


```python
import pandas as pd 
```


```python
url = "http://space-facts.com/mars/"
browser.visit(url)
```


```python
mars_df = pd.read_html(url)
mars_df = mars_df[0]

type(mars_df)
```




    pandas.core.frame.DataFrame




```python
mars_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Equatorial Diameter:</td>
      <td>6,792 km</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Polar Diameter:</td>
      <td>6,752 km</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mass:</td>
      <td>6.42 x 10^23 kg (10.7% Earth)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Moons:</td>
      <td>2 (Phobos &amp; Deimos)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Orbit Distance:</td>
      <td>227,943,824 km (1.52 AU)</td>
    </tr>
  </tbody>
</table>
</div>




```python
#convert to html table string
table = mars_df.to_html()
print(table)
```

    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>0</th>
          <th>1</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Equatorial Diameter:</td>
          <td>6,792 km</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Polar Diameter:</td>
          <td>6,752 km</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Mass:</td>
          <td>6.42 x 10^23 kg (10.7% Earth)</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Moons:</td>
          <td>2 (Phobos &amp; Deimos)</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Orbit Distance:</td>
          <td>227,943,824 km (1.52 AU)</td>
        </tr>
        <tr>
          <th>5</th>
          <td>Orbit Period:</td>
          <td>687 days (1.9 years)</td>
        </tr>
        <tr>
          <th>6</th>
          <td>Surface Temperature:</td>
          <td>-153 to 20 °C</td>
        </tr>
        <tr>
          <th>7</th>
          <td>First Record:</td>
          <td>2nd millennium BC</td>
        </tr>
        <tr>
          <th>8</th>
          <td>Recorded By:</td>
          <td>Egyptian astronomers</td>
        </tr>
      </tbody>
    </table>
    

## Mars Hemispheres

 - Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
 - You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
 - Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
 - Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.





```python
import time 
from splinter.exceptions import ElementDoesNotExist

url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)
```


```python
html = browser.html
soup = bs(html, 'html.parser')
```


```python
hemisphere = []

for i in range (4):
    time.sleep(5)
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
```


```python
print(hemisphere)
```

    [{'title': 'Cerberus Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg'}]
    
