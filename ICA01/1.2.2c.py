a = "1"
b = "0"
text = "01011" # xyz
for i, c in enumerate(text):
    text = i,c
     

ascii = {"0": "X","10": "Y","11": "Z"}

#Formålet med denne blocken var at koden skulle sjekke en bit av text 
#dersom biten ikke var 0 skulle neste bit sjekkes. De to bitsene utgjør en av keyene i ascii dictionaryen.
for c in text:
    if c == "0":
        ec = ascii[c]
        print ec
    if c == "1" and next(c) == a:
        if c == a:
            print ascii["10"]
        elif c == b:
            print ascii["11"]
            
        if next(c) == "0":
            ec = (c+next(c))
            print ec
    
        
        #print ascii ["10"]

        
    
    
        
    