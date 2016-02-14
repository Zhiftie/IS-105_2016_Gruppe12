# -*- coding: utf-8 -*-

def compress(uncompressed):
    dictionarySize = 127
    dictionary = dict((chr(i), chr(i)) for i in xrange(dictionarySize))
    
    
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dictionarySize
            dictionarySize += 1
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result



#def decompress(compressed):
    #"""Decompress a list of output ks to a string."""

    ## Build the dictionary.
    #dictionarySize = 127
    #dictionary = dict((chr(i), chr(i)) for i in xrange(dictionarySize))
    

    #w = result = compressed.pop(0)
    #for k in compressed:
        #if k in dictionary:
            #entry = dictionary[k]
        #elif k == dictionarySize:
            #entry = w + w[0]
        #else:
            #raise ValueError('Bad compressed k: %s' % k)
        #result += entry

        ## Add w+entry[0] to the dictionary.
        #dictionary[dictionarySize] = w + entry[0]
        #dictionarySize += 1

        #w = entry
    #return result

compressed = compress('hei')
print (compressed)
