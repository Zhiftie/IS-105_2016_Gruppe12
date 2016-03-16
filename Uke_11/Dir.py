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

import os
myfile="tmp/foo.txt"

#Remove
##if file exists, delete it 
def deleteFileIfExist():
    if os.path.isfile(myfile):
        os.remove(myfile)
    else: #Show an error
        print("Errror: %s file not found" % myfile)
    
    
#Sjekker om noden er en mappe (is_dir):
##Return True if path is an existing directory. This follows symbolic links, so both islink() and isdir() can be true for the same path.
def checkIfNodeIsDir():
    if os.path.isdir(path):
        print "it's a directory"
    else:
        print "it's a file"
    
#Bytte til spesifisert mappe(chdir):
## Change the directory
def changeDirectory():
    os.chdir( path )
    
#Slette Mappe
def deleteDir():
    os.remove()






