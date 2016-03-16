class Files:
    def __init__(self):
        pass
    

# Opprett en ny fil.
def newFile():
    if os.path.exists('location\filename.txt'):
        print "File exists"
    else:
        open("location\filename.txt", 'w')

# Søk i filen.
def searchFile():
    with open('file.txt', 'r') as searchfile:
        for line in searchfile:
            if 'searchphrase' in line:
                print line

# Gi en fil et nytt navn.                
def renameFile():
    for fileName in os.listdir("."):
        os.rename(fileName, fileName.replace("Filnavn", "NyttFilNavn"))

# Slette en fil.
def slettfil():
    os.remove()