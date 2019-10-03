# Script to retrieve 2008 stats
#(C) Peter RL Granlund, RL Dimensions

# Import statements
import requests
import sys
import time
import constants
from Labrador import Labrador
from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor, as_completed


def boxScoresForYear(year):
    # fetch holding page
    result = requests.get(constants.MVFC_BASE_URL + year + "/confstat.htm")
    #Display status in case of error
    print(result.status_code)

    # Fetch and store the content to a variable
    src = result.content

    # create BS object with the source content
    soup = BeautifulSoup(src, features='html.parser')

    games = soup.find("table")

    shadow = Labrador(year, constants.MISSOURI_VALLEY_FOOTBALL, constants.MVFC_BASE_URL, constants.BASE_DIRECTORY)
    
    links = []

    for idx, row in enumerate(games.find_all("a")):
        link = row.get('href')
        links.append(link)
        print("Box Score Number: " + str(idx) + " - " + link)


    # Find all the box scores for the year, fetch the URL, and download the file to be saved
    with ProcessPoolExecutor(max_workers=4) as boxExecutor:
        boxStart = time.time()
        boxFutures = [ boxExecutor.submit(shadow.retrieveBoxScore, boxScoreLink) for boxScoreLink in links ]
        boxResults = []
        for result in as_completed(boxFutures):
            boxResults.append(result)
        boxEnd = time.time()
        print("Time Taken for box scores: {:.6f}s".format(boxEnd-boxStart))


#def handleBoxScoresForYear(year, boxscores):

def checkYear(year):
    if year < 10:
        return "0" + str(year)
    else:
        return str(year)

boxScoresForYear(checkYear(18))

'''
with ProcessPoolExecutor(max_workers=4) as yearExecutor:
    yearStart = time.time()
    yearFutures = [ yearExecutor.submit(boxScoresForYear, checkYear(year)) for year in range(18,19) ]
    yearResults = []
    for result in as_completed(yearFutures):
        yearResults.append(result)
    yearEnd = time.time()
    print("Time Taken: {:.6f}s".format(yearEnd-yearStart))
'''
# Deprecated Argument Check
"""
if not len(sys.argv) > 0:
    boxScoresForYear(checkYear(sys.argv[0]))
else:
        print("No Arguments Passed, dummy.")
"""

# Deprecated Loop for all years.
"""
# Loop for each year (WIP)
boxScoresForYear("09")
for year in range(10,19):
    boxScoresForYear(year)

# Retrieve 08's box scores
# boxScoresForYear("08")
"""