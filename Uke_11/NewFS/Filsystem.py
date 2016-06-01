# -*- coding: utf-8 -*-

"""
Masterliste som inneholder samtlige elementer i de andre (underrettede) listene.
Listehierarki: 
* Masterliste
* Directories 
* Filer/directories

Hver gang noe "slettes" i filsystemet skal filsystemet kalle en metode som wiper(frigjør) plassen det aktuelle elementet tar i listen. 


ToDO: Implementere addFile, isDir, isFile, cmd(kommandoer fra brukeren - bruk dictionary), + andre metoder fra ica dokumentet. 
"""

class Filsystem():
    
    #filesystem name
    def __init__(self): 
        self.masterList = [] # new list to contain everthing
        self.rootElementDict = {} # Creates a new dictionary where the root folder is value and the elements are key(s). 
         
        #implements the hierarchy.
        self.masterList.extend(rootList) 
        #self.rootList.extend(elementList)
        
    """
    Value dir/file.
    Key root. 
    """
    def addRoot(self):
        
        
        
    