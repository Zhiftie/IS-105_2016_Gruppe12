# -*- coding: utf-8 -*-
import io
import string


'''
Module med eksempler i uke 04 (informasjonsteori)
Løsninger for klasseoppgavene 25.01.2016 implementeres her
Løsningsforslag innleveres i gruppe-repositorien.
GRUPPENR: ...
STUDENTER: ...
'''
n = 8

def encode(text):
    encoded = ''
    for letter in text:
        encoded += bin(ord(letter))[2:].zfill(8)
    return encoded

def decode(sourcecode,n):
    text = ''
    with open(sourcecode, 'r') as inf:
        while True:
            chunk = inf.read(n) # Read n characters at time from an open file
            if chunk == '':             # This is one way to check for the End Of File in Python 
                break
            if chunk != '\n':
                text += chr(int(chunk, 2))
                pass 
    return text
    #'''
    #Decode a sourcecode using chunks of size n
    #'''
    # You will need a dictionary holding the mapping between binary string and ASCII chars



def test():
    '''
    A placeholder for some test cases.
    It is recommended that you use some existing framework, like unittest,
    but for a temporary testing in a development version can be done 
    directly in the module.
    '''
    
    lol = decode('sourcecode.txt', 8)
    lal = encode('HAHAHAH') 
    print(lal)
    print(lol)
    pass

print decode("sourcecode.txt", n)


