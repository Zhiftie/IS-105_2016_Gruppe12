"""
https://gist.github.com/Cmoen11/cc7bc0d7f22fdcea5c65db55d6c612f2

"""


totalspace = 32 # 32 blokker totalt
filespace = [] 
#Hver item i lista filespace blir en block. 

def create_block():
    filespace.append(
        {
            'filename':'',
            'content':''
        }    
        
    )
def create_harddisk():
    #Oppretter 32 blokker, hver av blokkene har en adresse i index, f.eks. 1, 2, 3.
    for i in range (0, totalspace):
        create_block()


create_harddisk()
for i in filespace :
    print i
    
    

