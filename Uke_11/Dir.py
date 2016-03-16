import os, sys, bpy


class Dirs:
    def __init__(self):
        pass
    
    dirList = []

    def makeDir(self):
        self.dirName = raw_input("Please input the name of your brand new directory \n" )
        self.dirList.append( self.dirName )
        return self.dirList
    
    def searchDir(self):
        self.dirName = raw_input("Input searchword to find folder. \n " )
        if self.dirName in dirI:
            print "Woho! Found %s" % self.dirName
        else:
            print "Sorry, %s not found. You could try the list method to find directories!" % self.dirName
        
        
    def removeDir(self):
        self.dirName = raw_input("Input name of directory to delete \n" )
        if self.dirName in dirI:
            dirI.remove( self.dirName )
        else: 
            print "%s not found. You could try the list method to find directories!" % self.dirName
        
        
    def renameDir(self):
        self.dirName = raw_input("Input CURRENT directory name to find it. \n " )
        if self.dirName in dirI:
            print "Woho! Found %s" % self.dirName
            newName = raw_input("Input the new name you'd like for your directory. \n " )
            if newName in dirI:
                print "%s already exists! Use anoter name for your directory. \n "
            else: 
                for self.dirName in dirI:
                    self.dirName.name = newName
        else:
            print "Sorry, %s not found. You could try the list method to find directories!" % self.dirName        
        
        self.dirName = raw_input("New name for directory" ) 
        """
Metodene ovenfor må testes i sammenheng med Filsys.py. 

        """
   
    
        
dir1 = Dirs()
#print dir1.makeDir() #kaller makeDir metode
#dir1.workingDir() kaller workingDir metode
#dir1.statDir(snas)











#Remove
myfile="tmp/foo.txt"
#if file exists, delete it 
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






