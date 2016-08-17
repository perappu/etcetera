#!/usr/bin/env python
# encoding: utf8
'''A simple script for compiling a JSON request into a CSV.

Heavily edited and extremely untested version of something I did for work.'''

import requests
import json
import csv
import datetime
from datetime import date

def __unicode__(self):
   return unicode(self.some_field) or u''

def getDayOfTheWeek(year, month, day):
    '''Get the day of the week from the year, month, and day. Assumes they are passed as strings.

       I needed this for the original script and decided to hang onto it.'''

    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    dayOfTheWeek = datetime.date(int(year), int(month), int(day)).weekday()

    return days[dayOfTheWeek]

def buildCSV(url, nameOfFile):
    '''Builds a CSV off an arbitrary JSON request.

    ...or it would, if JSON wasn't quite as flexible with its structure.

    Will need to be adjusted to account for your data. Currently assumes the
    requested JSON is a list of single depth dictionaries.'''

    # Build the csv
    with open(nameOfFile + '.csv', 'wt',newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Get JSON response
        apiResponse = requests.get(url)
        apiResponse = apiResponse.json()

        for i, dict in enumerate(apiResponse):

            # If it's the first item, write the header first
            if i == 0:
                header = list(dict.keys())
                writer.writerow(header)

            writer.writerow(list(dict.values()))

def main():
    '''Main function gets parameters for buildCSV(). 
    
    Given url will need to have any required parameters/tokens included.
    Currently not checking if the given file name is valid, so have fun.'''

    url = input("Enter API url: ")
    nameOfFile = input("Enter name of file: ")

    buildCSV(url, nameOfFile)
    
    print("Done!")

if __name__ == '__main__':
    main()