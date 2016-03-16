import os
import sys

class Dirs:
    def __init__(self):
        pass
    
    dirList = []

    def makeDir(self):
        self.dirName = raw_input("Please input the name of your brand new directory \n" )
        self.dirList.append( self.dirName )
        return self.dirList
dir1 = Dirs()
print dir1.makeDir()