# -*- coding: utf-8 -*-

# import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#import csv 
#from datetime import datetime

# specify the url
addresses = ["http://www.repository.voxforge1.org/downloads/sq/Trunk/Audio/Original/48kHz_16bit/"]
for pg in addresses:
    i=1
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
            i += 1
            time.sleep(1) #pause the code for a sec