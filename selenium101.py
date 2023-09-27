import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import rfeed

#url of the page we want to scrape
url = "https://www.comune.parma.it/it/novita/notizie"
  
# initiating the webdriver in headless mode
op = webdriver.ChromeOptions()
op.add_argument('--headless')
driver = webdriver.Chrome(options=op) 
driver.get(url) 

# this is just to ensure that the page is loaded
time.sleep(5) 

  
html = driver.page_source
# this renders the JS code and stores all
# of the information in static HTML code.

items_ = []
  

soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find_all(class_="card-title")
#print("there are " + str(len(all_divs)) + " card titles")
all_descriptions = soup.find_all(class_="mb-3 card-text")
#print("there are {} card descriptions".format(all_descriptions))
for i in range(0, len(all_divs)):
#for d in all_divs:
    d = all_divs[i]
    ah = d.find('a')
    #print(ah.text)
    #print(all_descriptions[i].string)
    #print("https://www.comune.parma.it" + ah['href'])
    item = rfeed.Item(title=ah.text, link="https://www.comune.parma.it" + ah['href'], description=all_descriptions[i].string)
    items_.append(item)


# Create RSS Feed
feed = rfeed.Feed(title="Novità Comune di Parma", description="Novità del comune di Parma", language="it", items=items_, link=url)
  
driver.close() # closing the webdriver

rss=feed.rss()
print(rss)
# redirect output from file when running from command line
# for example:
# python3 selenium101.py > feed.rss

