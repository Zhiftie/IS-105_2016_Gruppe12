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
    
    def workingDir(self):
        print "Current working dir : %s" % os.getcwd()
        
    def statDir(self, searchWord):
        searchWord = raw_input("Please input the name of the directory you want information about. \n" )
        for searchWord in dirList:
            return os.stat(searchWord)
    
        
dir1 = Dirs()
#print dir1.makeDir() #kaller makeDir metode
#dir1.workingDir() kaller workingDir metode
#dir1.statDir(snas)







