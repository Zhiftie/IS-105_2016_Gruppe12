# -*- coding: utf-8 -*-

"""
Masterliste som inneholder samtlige elementer i de andre (underrettede) listene.
Listehierarki: 
* Masterliste
* Directories 
* Filer/directories

Hver gang noe "slettes" i filsystemet skal filsystemet kalle en metode som wiper(frigjør) plassen det aktuelle elementet tar i listen. 


ToDO: Implementere addFile, isDir, isFile, cmd(kommandoer fra brukeren - bruk dictionary), + andre metoder fra ica dokumentet. Fikse struktur.
"""

class Filsystem():
    
    def __init__(self): 
        pass    
    
    masterList = [] # new list to contain everthing
    global rootElementDict 
    rootElementDict = {} # Creates a new dictionary where the root folder is value and the elements are key(s). 
    
    #implements the hierarchy.
    masterList.extend(rootElementDict) 
    
   
        
        
    """
    Value dir/file.
    Key root. 
    """
    def addRoot(key, value): 
        rootElementDict[key] = value
        
    """
    Skal printe ut alle keys og values i dictionarien. 
    """
    def stats():
        for key, value in rootElementDict.iteritems():
            print key, value
        

    
    
fs = Filsystem()
fs.addRoot("rootMappe" "DirMappe")
fs.stats

        
        
        
    