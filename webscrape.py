from bs4 import BeautifulSoup
import pandas as pd
import csv
import os
import time
import requests

# Scrapes data from hockey-reference

try:
    full_data= pd.read_csv("hockey-data-hart.csv")    
except:
    # Scrape data
    # specify the url
    years = range(1936,2018 + 1)
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
            time.sleep(0.1) #pause the code for a sec
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
                    

# Scrape data
# specify the url
identifier = ['skaters','goalies']
addresses = ["https://www.hockey-reference.com/leagues/NHL_2019_{}.html".format(tag) for tag in identifier]
names = ['player',
         'age',
         'team_id',
         'pos',
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

try:
    pd.read_csv("2019-data.csv")
except:
    with open('2019-data.csv'.format(identifier), 'w') as csvfile:    #Create the csv file
        hockeywriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        hockeywriter.writerow(names)
        for pg in addresses:
            time.sleep(0.1) #pause the code for a sec
            r = requests.get(pg)
            # parse the html using beautiful soup and store in variable `soup`
            soup = BeautifulSoup(r.text, "html.parser")
            values = []  #first value

            #Go through the stats and add them to a list
            for line in soup.findAll("tr"):
                # print(line,"\n")
                
                for stat in names:
                    val = line.find(attrs={"data-stat" : stat})
                    if val == None:
                        values.append('')
                    else:
                        values.append(val.string)

                print("Writing values {} to csv".format(values))
                hockeywriter.writerow(values)
                values = []  