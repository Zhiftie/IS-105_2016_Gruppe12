from Dir import Dirs as d
class Filsys():
    
    def __init__(self, sysname):
        self.dirName = sysname
        self.dirI= []
    
    def addDir(self):
        self.dirName = raw_input("Name folder >>>")
        self.nDir = d()
        self.dirI.append(self.nDir)
        return self.dirI
    
    def checkI(self, i):
        return self.dirI[i]
        
    def removeEmptyListElements(self):
        while '' in dirI:
            dirI.remove('')
    """
^^^^^^^ metoden^^^^^^ burde legges inn i remove metoden, slik at
bruker slipper å tenke på slikt. 
    """
        
fs = Filsys("Sys1")

