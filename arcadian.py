# arcadian.py -  - PRL Granlund - (c) RL Dimensions
# October 7, 2019
# v0.9
# File shepherd object to create and manage files from a specific base folder

from webwishbone import WebWishbone
import os

class Arcadian:

    def __init__(self, baseDirectory):
        self.baseDirectory = baseDirectory
        self.listOfDirectories = WebWishbone.hunt(baseDirectory, True)

    # Read Functions


    # Write Functions
    def checkForDir(self, location):
            if os.path.exists(location):
                return True
            else:
                return False

    def confirmDir(self, location):
        if not os.path.exists(location):
            os.makedirs(location)
        return self.checkForDir(location)

    def writeFile(self, fileLocation, fileContents):
        if self.checkForDir(self.getDirectoryFromFile(fileLocation)):
            outputFile = open(fileLocation, "w")
            outputFile.write(fileContents)
        else:
            print("Could not create the directory for this file.")

    def getDirectoryFromFile(self, fileLocation):
        directoryList = fileLocation.split('/')
        outputDirectory = "/"
        for directory in range(0, (len(directoryList)-1)):
            outputDirectory = os.path.join(outputDirectory, directory)
