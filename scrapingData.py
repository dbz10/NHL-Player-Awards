# -*- coding: utf-8 -*-         

# import libraries
import requests
import os
import time
from bs4 import BeautifulSoup
import csv 

path = 'D:\\Documents\\Research\\stunning-parakeet'
try:
    os.chdir(path)
except:
    print('Wrong directory broseph')
    
# specify the url
years = range(1924,2018 + 1)
addresses = ["https://www.hockey-reference.com/awards/voting-{}.html#all-hart-stats".format(yr) for yr in years]
names = ['Year',  
         'player',
         'age',
         'team_id',
         'pos',
         'votes',
         'pct_of_vote',
         'first',
         'second',
         'third',
         'fourth',
         'fifth',
         'goals',
         'assists',
         'points',
         'plus_minus',
         'wins_goalie',
         'losses_goalie',
         'ties_goalie',
         'goals_against_avg',
         'save_pct',
         'ops',
         'dps',
         'gps',
         'ps']

with open('hockey-data-hart.csv', 'w') as csvfile:    #Create the csv file
    hockeywriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    hockeywriter.writerow(names)
    for i, pg in enumerate(addresses):
        time.sleep(1) #pause the code for a sec
        r = requests.get(pg)
        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(r.text, "html.parser")
        values = [years[i]]  #first value
        
        #Go through the stats and add them to a list
        for tag in soup.findAll("td"):
            if tag.string == 'None': #don't save 'None' string
                values.append('') 
            elif tag['data-stat']=='team_id': #use proper team name
                try: #though it may not exist
                    values.append(tag.contents[0]['title'])
                except:
                    values.append(tag.string)
            else:
                values.append(tag.string)
            if tag['data-stat']=='ps': #if last value in row start on next line
                hockeywriter.writerow(values)
                values = [years[i]]  #set first value again     
                
