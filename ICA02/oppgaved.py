mappingA2B = {"F" : "11", "D": "10", "A": "011", "B" : "010", "E" : "001", "C":"000"}
mappingB2A = {"11" : "F", "10" : "D", "011" : "A", "010" : "B" , "001" : "E", "000" : "C"}

m = "FDABEC" #1110011010001000
n = 2   
lres = []
res = ""
melding = ""
# 
def encode(m):
    eString = ""
    for letter in m:
        if letter in m: 
            eString = eString + mappingA2B[letter]    
    return eString

res = encode(m)
# deler stringen res opp i bits og legger de inn i listen lres
def chunks(res):
    for x in range(len(res)): 
        lres.append(res[:1])
        
        res = res[1:]
    return lres

lres = chunks(res)

def decode(lres): #Sjekker første index i lres. Ut fra resultatet                
    it = 0        #sjekker den neste index og genererer en nøkkel i dict 
    ferdigM = ""
    for bit in lres:
        if len(lres) is 0:
            break
        if lres[0] is ("1") and lres[1] is ("1"):# index 0 = 1 og index 1 = 0
            key = lres[0] + lres[1]
            del lres[0] 
            del lres[0]
            ferdigM += mappingB2A[key]
        
        if lres[0] is ("1") and lres[1] is ("0"): 
            key = lres[0] + lres[1]
            del lres[0]
            del lres[0]
            ferdigM += mappingB2A[key]
        
        if lres[0] is "0": 
            if lres[1] is "0": 
                if lres[2] is "1": 
                    key = lres[0] + lres[1] + lres[2]
                    del lres[0]
                    del lres[0]
                    del lres[0]
                    ferdigM += mappingB2A[key]
                
                elif lres[2] is "0":
                    key = lres[0] + lres[1] + lres[2]
                    del lres[0]
                    del lres[0]
                    del lres[0]
                    ferdigM += mappingB2A[key]
            
            if lres[1] is "1":# Får feilmelding her når listen er tom 
                if lres[2] is "1":
                    key = lres[0] + lres[1] + lres[2]
                    del lres[0]
                    del lres[0]
                    del lres[0]
                    it +=1
                    ferdigM +=mappingB2A[key]
                
                if lres[2] is "0":
                    key = lres[0] + lres[1] + lres[2]
                    del lres[0]
                    del lres[0]
                    del lres[0]
                    it +=1
                    ferdigM +=mappingB2A[key]            
    
    print ferdigM       
    return ferdigM
    
                
melding = decode(lres)

encode(m)
chunks(res)
decode(lres)






        
        