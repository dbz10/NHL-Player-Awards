# -*- coding: utf-8 -*-

# import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#import csv 
#from datetime import datetime

# specify the url
years = range(1923,2017 + 1)
addresses = ["https://www.hockey-reference.com/awards/voting-{}.html#all-hart-stats".format(yr) for yr in years]
for pg in addresses:
    r = requests.get(pg)
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(r.text, "html.parser")
    for tag in soup.findAll("a"):
        link = tag['href']
        if ".tgz" in link:
            download_url = pg + link
            filename = 'vf_{}.tgz'.format(i)
            urllib.request.urlretrieve(download_url,'./'+filename) 
            print(filename)
            time.sleep(1) #pause the code for a sec