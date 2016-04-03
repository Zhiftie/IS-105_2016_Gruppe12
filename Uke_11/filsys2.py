"""
Creates a dictionary serving as memory.
"""
fl = []
def makeIndex(maxSize):
   memIndex = {}
   for i in xrange(0,maxSize):
      memIndex[str(i)] = None
   return memIndex
"""

"""
def unusedInd():
   ui2 = []
   for i in xrange(0,len(index)):
      ui2.append(str(i))
   return ui2

def newFile():
   name = raw_input("Input Filename >>> ")
   cont = raw_input("Input Filecontent >>> ")
   bits = list(cont)
   fl.append(name)
   return name, bits
   
"""
returns the location of the different bits in "memory" 
"""
def fillInd():
   for i in f1[1]:
      adresse = []
      for k in xrange(1,len(f1[1])):
         index[str(k)]  = str(i)
         adresse.append(k)
      return adresse
         
"""
returns the content of a file from the index using the adress list
"""
def showContent(fn): #
   loop over adresse liste:
      use items from list as keys for the memory dictionary
      store values from index dict as string
   return the content string
"""
Lists all files
"""
def ls():
   for item in fl:
      print item
   
      
   
   
   
   
         
      
    
index = makeIndex(127)
i2 = unusedInd()
f1 = newFile()
fillInd()
f1 = fillInd()
print index