# arcadian.py -  - PRL Granlund - (c) RL Dimensions
# October 7, 2019
# v0.9
# File shepherd object to create and manage files from a specific base folder

from webwishbone import WebWishbone
from file import File
import os

class Arcadian:

    def __init__(self, baseDirectory):
        self.baseDirectory = baseDirectory
        self.listOfDirectories = WebWishbone.hunt(baseDirectory, True)

    # Read Functions
    def readFromFile(self, location):
        return open(location)

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

    def writeFile(self, file):
        if self.checkForDir(file.directory):
            outputFile = open(file.filePath, "w")
            outputFile.write(file.contents)
        else:
            print("Could not create the directory for this file.")

