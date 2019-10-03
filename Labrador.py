# Class for the Retrieving Objects

import wget
import os

class Labrador:
    def __init__(self, year, conference, baseUrl, baseLocation):
        self.year = year
        self.conference = conference
        self.updatedRootURL = baseUrl + year + "/"
        self.updatedBaseLocation = baseLocation + conference + "/" + year + "/"


    def retrieveBoxScore(self, url):
        parseUrl = url.split('/')
        fileName = parseUrl[-1]
        if len(parseUrl) == 1:
            newUrl = self.updatedRootURL + url
        else:
            newUrl = url
        fullFilePath = self.updatedBaseLocation + fileName
        #print(fullFilePath)
        if self.checkForDir(self.year):
            wget.download(newUrl, fullFilePath)
            return "Success at " + fileName
        else:
            print("Error with directory access for " + fileName)

    def checkForDir(self, year):
        if not os.path.exists(self.updatedBaseLocation):
            os.makedirs(self.updatedBaseLocation)
        if os.path.exists(self.updatedBaseLocation):
            return True
        else:
            return False