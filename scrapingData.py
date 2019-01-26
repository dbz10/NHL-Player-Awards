# -*- coding: utf-8 -*-

# import libraries
import requests
import time
from bs4 import BeautifulSoup
import csv 


# specify the url
years = range(1923,2017 + 1)
addresses = ["https://www.hockey-reference.com/awards/voting-{}.html#all-hart-stats".format(yr) for yr in years]
for pg in addresses:
    time.sleep(1) #pause the code for a sec
    r = requests.get(pg)
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(r.text, "html.parser")
    for tag in soup.findAll("td"):
        name = tag['data-stat']
        value = tag['csk']
        
            
with open('hart.csv', 'w', newline='') as csvfile:
    hockeywriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    hockeywriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    hockeywriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])