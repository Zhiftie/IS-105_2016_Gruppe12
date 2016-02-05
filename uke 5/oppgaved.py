mappingA2B = {"F" : "11", "D": "10", "A": "011", "B" : "010", "E" : "001", "C":"000"}
mappingB2A = {"11" : "F", "10" : "D", "011" : "A", "010" : "B" , "001" : "C"}

m = "FDABEC" #1110011010001000
n = 2   
lres = []
res = ""
def encode(m):
    eString = ""
    for letter in m:
        if letter in m: 
            eString = eString + mappingA2B[letter]    
    return eString

res = encode(m)

def chunks2(res, n):
    for i in range(0,len(res),n):
        yield lres[i:i+n]
    
#lres = chunks2(res, n)

def chunks(res, n):
    [res[i:i+n] for i in range(0,len(res),n)] 
    print res

lres = chunks(res, n)

def decode(res):
    it = 0
    ferdigM = ""
    while it <= len(res):
        pass

def printlres():
    for item in lres:
        print str(item)

encode(m)
chunks(res, n)
printlres()




        
        