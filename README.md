# Web-scraping Challenge

## Table of Contents
  * [Introduction](#introduction)
  * [Scraping](#scraping)
    * [NASA Mars News](#news)
    * [JPL Mars Space Images - Featured Image](#images)
    * [Mars Facts](#facts)
    * [Mars Hemisphere<](#hemisphere)
    

# <a name="lat">Introduction</a>

The purpose of this project is to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 
The following outlines what you need to do.


# <a name="scraping">Scraping</a>

The initial scraping was completed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
A Jupyter Notebook file called mission_to_mars.ipynb was created and this was used to complete all of the scraping and analysis tasks. The data scraped was the following:
Splinter was used to navigate the sites when needed and BeautifulSoup was used to help find and parse out the necessary data.

## <a name="news">NASA Mars News</a>
- Scraped the NASA Mars News Site and collect the latest News Title and Paragraph Text.

## <a name="images">JPL Mars Space Images - Featured Image</a>
- Visited the url for JPL Featured Space Image
- Used splinter to navigate the site and find the image url for the current Featured Mars Image and assigned the url string to a variable called featured_image_url.


## <a name="facts">Mars Facts</a>

- Visited the Mars Facts webpage and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

- Used Pandas to convert the data to a HTML table string.

## <a name="hemisphere">Mars Hemisphere</a>

- Visited the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.

- Each of the links to the hemispheres were selected in order to find the image url to the full resolution image.

- Both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name were saved. A Python dictionary was used to store the data using the keys img_url and title.

- Appended the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

