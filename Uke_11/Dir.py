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




#Remove rmdir
def rmdir(self, cmd):
    if len(cmd) < 2 or cmd[1] == '':
        print 'rmdir - remove directory'
        print 'usage: rmdir <dir_name>'
    else:
        name = cmd[1]
        if self.curr.is_dir(name):
            self.curr.remove(name)
            print 'Directory deleted.'
        else:
            print name, ' - invalid directory.' 
    
    
#Sjekker om noden er en mappe (is_dir):
##Return True if path is an existing directory

def is_dir(self, name):
    if(self.is_file(name)) and self.get(name).type == 'dir':
        return True
    return False

    
#Bytte til spesifisert mappe(chdir):
## Change the directory
def chdir(self, cmd):
    if len(cmd) < 2 or cmd[1] == '':
        print 'chdir - change directory.'
        print 'usage: chdir <dir_name>'
    else:
        name = cmd[1]
        if name == '..':
            if self.curr.parent is not None:
                self.curr = self.curr.parent
            elif self.curr.is_dir(name):
                self.curr = self.curr.get(name)
            else:
                print name, ' - invalid directory.'






