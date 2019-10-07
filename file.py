# file.py -  - PRL Granlund - (c) RL Dimensions
# October 7, 2019
# v0.9
# object to handle file-specific information and functions; name, directory, contents


class File():

    def __init__(self, filePath, readFileBool):
        self.filePath = filePath
        self.fileName = filePath.split('/')[-1]
        self.directory = self.getDirectoryFromFile(filePath)
        self.extension = filePath.split('.')[-1]
        self.contents = ""
        if readFileBool == True:
            self.readToContents()
        
    def getDirectoryFromFile(self, fileLocation):
        directoryList = fileLocation.split('/')
        directoryList.remove(directoryList[-1])
        # outputDirectory = "/"
        return "/" + "-".join(directoryList)

    def readToContents(self):
        self.contents = open(self.filePath)

    def readFile(self):
        return open(self.filePath)

# To be added later; possibly consolidate with Umbrella class from the script folder
"""def breakdown(self, name):
        fileBreakdown = name.split('.')
        tmpFile = ""
        if len(fileBreakdown) == 2:
            self.newTitle = fileBreakdown[0]
            self.extension = '.' + fileBreakdown[-1]
        elif len(fileBreakdown) > 2:
            for i in range(len(fileBreakdown) - 1):
                tmpFile = tmpFile + fileBreakdown[i]
            self.newTitle = tmpFile
        else:
            print("Not a valid file with extension")
            self.newTitle = self.oldFileStr
"""