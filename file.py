# file.py -  - PRL Granlund - (c) RL Dimensions
# October 7, 2019
# v0.9
# object to handle file-specific information and functions; name, directory, contents


import os

class File():

    def __init__(self, filePath, readFileBool):
        self.filePath = filePath
        self.fileName = filePath.split('/')[-1]
        self.directory = self.getDirectoryFromFile(filePath)
        self.extension = filePath.split('.')[-1]
        self.contents = ""
        if readFileBool == True:
            self.readToContents()
    
    def getContentsOfFile(self):
        return self.contents
        '''if len(self.contents) == 0:
            self.readToContents
            return self.contents
        else:
            return self.contents'''
        
    def getDirectoryFromFile(self, fileLocation):
        directoryList = fileLocation.split('/')
        directoryList.remove(directoryList[-1])
        # outputDirectory = "/"
        return "/".join(directoryList)

    def findExtension(self):
        return self.filePath.split('.')[-1]

    def readToContents(self):
        with open(self.filePath, 'r') as content_file:
            content = content_file.read()
            content_file.close()
        self.contents = self.sanitizeText(content)

    def readFile(self):
        with open(self.filePath, 'r') as content_file:
            content = content_file.read().decode('utf-8','ignore')
            content_file.close()
        self.contents = self.sanitizeText(content)

    def sanitizeText(self, text):
        content = text
        content.replace('&nbsp;', ' ')
        content.replace('&#149;', '')
        return content


    def updatePath(self):
        self.filePath = os.path.join(self.directory, self.fileName)

    def setFileName(self, newName):
        if len(newName.split('.')) > 0:
            self.fileName = newName
            self.extension = self.findExtension()
        else:
            print("Unable to accept new name due to lack of file extension")
        

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