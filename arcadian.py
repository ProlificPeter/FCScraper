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
        self.listOfFiles = []
        self.populateListOfFiles(False)

    # Object Helper Functions
    def populateListOfFiles(self, readFileBool):
        fileObjList = []
        for files in self.listOfDirectories:
            dirPath, fileName = files
            path = os.path.join(dirPath, fileName)
            if not readFileBool == True:
                fileObjList.append(self.createFileObjFromPath(path))
            else:
                fileObjList.append(self.createFullFileObjFromPath(path))
        self.listOfFiles = fileObjList
    
    def getListOfFilesFromRoot(self, readFileBool):
        self.populateListOfFiles(readFileBool)
        tempList = self.listOfFiles
        return tempList

    
    def retrieveListOfFiles(self, directoriesList, readFileBool):
        fileObjList = []
        for files in directoriesList:
            dirPath, fileName = files
            path = os.path.join(dirPath, fileName)
            print(path)
            fileObjList.append(self.createFileObjFromPath(path))
        return self.listOfFiles

    # File Handle Functions
    def copyContentsOfFile(self, file, newFilePath):
        newFile = File(newFilePath, False)
        newFile.contents = file.contents


    # Read Functions
    def readFromFile(self, location):
        return open(location)

    def createFileObjFromPath(self, path):
        return File(path, False)

    def createFullFileObjFromPath(self, path):
        return File(path, True)

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
            outputFile.close()
        else:
            print("Could not create the directory for this file:" + file.directory)

