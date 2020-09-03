# webwishbone.py - PRL Granlund - (c) RL Dimensions
# October 5, 2019
# v0.9
# Simple script for pulling local webfiles from a directory tree.

import os

class WebWishbone(object):
    
    @staticmethod
    def hunt(directory, htmlHunter):
        listOfDirectoryAndFiles = []
        for dirPath, __, files in os.walk(directory):
            for filename in files:
                if htmlHunter == True:
                    if (filename.endswith(".htm") or filename.endswith(".html")) and not filename.startswith(".DS_Store"):
                        listOfDirectoryAndFiles.append((dirPath, filename))
                else:
                    if not filename.startswith(".DS_Store"):
                        listOfDirectoryAndFiles.append((dirPath, filename))
        return listOfDirectoryAndFiles