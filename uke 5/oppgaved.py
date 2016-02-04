mappingA2B = {"F" : "11", "D": "10", "A": "011", "B" : "010", "E" : "001", "C":"000"}
mappingB2A = {"11" : "F", "10" : "D", "011" : "A", "010" : "B" , "001" : "C"}

m = "FDABEC" #1110011010001000
n1 = 2 # Chunk lengde for decoding
n2 = 3 #  
res = ""
lres = list()
def encode(m):
    it = 0
    res = ""
    while it <= len(m):
        for letter in m:
            if letter in m:
                res = res + mappingA2B[letter]
                it += 1
    print "Original String: %r , Kodet String: %r" % (m,res)
    return res

def chunks(res, n1):
    [lres[i:i+n1] for c in range(0,len(res),n1)] 
    return lres 


def decode(res):
    it = 0
    ferdigM = ""
    while it <= len(res):
        pass

def print_lres(lres):
    for item in lres:
        print str(item)

encode(m)
chunks(res, n1)        
print_lres(lres)


        
        