#  -*- coding: utf-8-*-
import table as tab
def decode(message): 
    table = tab.code()
    string = ""
    code_for_string = []
    for byte in message:
        symbol = byte
        if (string + table[symbol] in table.values():
            string = string + symbol
#leser tekst som skal komprimeres i bytes. 
#Sjekker også om symbolet og stringen som leses allerede finnes i dictionary. 
        else:
            for k,v in table.iteritems(): 
                if v == string:
                    code_for_string.append(k) #Hvis det finnes en tilsvarende value i dictionary som er lik symbol vil det lages en ny liste.
            table[max(table.keys())+1] = string + table[symbol]
            string = symbol
    for k,v in table.iteritems():
        if v == string:
            code_for_string.append(k)
    return code_for_string