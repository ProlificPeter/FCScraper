# Script to retrieve FCS stats
#(C) PRL Granlund, RL Dimensions
#
# FYI: Needs to be updated to support different format of years for different conferences.
#       Currently only functional for initial scraping of Missouri Valley.

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
    requestUrl = constants.MVFC_BASE_URL + year + "/confstat.htm"
    print("Go Fetch!: " + requestUrl)
    result = requests.get(requestUrl)

    #Display status in case of error
    print(result.status_code)
    src = result.content

    # create BS object with the source content and find tables where the box score links are stored
    soup = BeautifulSoup(src, features='html.parser')
    games = soup.find("table")

    # Create a labrador object that will be used by the Processor Pool, and pass in the required information for the year.
    shadow = Labrador(year, constants.MISSOURI_VALLEY_FOOTBALL, constants.MVFC_BASE_URL, constants.BASE_DIRECTORY)
    
    #Create the links list that will be iterated through by the Process Pool, and populate it with the text from the hrefs.
    links = []
    for idx, row in enumerate(games.find_all("a")):
        link = row.get('href')
        links.append(link)
        print("Year " +  year + " | Box Score #" + str(idx + 1) + " - " + link)


    # Find all the box scores for the year, fetch the URL, and download the file to be saved on an 8-thread pool
    with ProcessPoolExecutor(max_workers=8) as boxExecutor:
        boxStart = time.time()
        boxFutures = [ boxExecutor.submit(shadow.retrieveBoxScore, boxScoreLink) for boxScoreLink in links ]
        boxResults = []
        for result in as_completed(boxFutures):
            boxResults.append(result)
        boxEnd = time.time()
        print("Time Taken for box scores: {:.6f}s".format(boxEnd-boxStart))

#Check the year to pass a year-specific string value if necessary; convert the year int to a string
def checkYear(year):
    if year < 10:
        return "0" + str(year)
    else:
        return str(year)

# Initial Load process; kicks off a 4-process pool that accesses a specified range of years (currently '16)
with ProcessPoolExecutor(max_workers=4) as yearExecutor:
    yearStart = time.time()
    yearFutures = [ yearExecutor.submit(boxScoresForYear, checkYear(year)) for year in range(16,17) ]
    yearResults = []
    for result in as_completed(yearFutures):
        yearResults.append(result)
    yearEnd = time.time()
    print("Time Taken: {:.6f}s".format(yearEnd-yearStart))