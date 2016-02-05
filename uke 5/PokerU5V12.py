# -*- coding: utf-8 -*-

import random #random generator
import math 
import itertools
from collections import defaultdict
import string

def poker(hands):
    #Returner en liste med vinnerhendene. 
    return allmax(hands, key =hand_rank)

def allmax(iterable, key=lambda x:x):
    maxi = max(iterable, key=key)
    return [element for element in iterable if key(element) == key(maxi)]

def hand_rank(hand):
    #Returnerer en verdi som viser hvor høyt hånden kan rangeres.
    groups = group(['--23456789TJQKA'.index(r) for r, s in hand]) # Kortet "10" kunne vært definert som både "10" og "T". Vi velger her "T" slik at alle to siffer tall får heller en bokstav. 
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4
    #Her^ defineres kravene for å ha straight.
    flush = len(set([s for r, s in hand])) == 1
    return (
        9 if (5, ) == counts else #5 like valørkort på håneden
        8 if straight and flush else 
        7 if (4, 1) == counts else #4 like kort + 1 ulik.
        6 if (3, 2) == counts else #3 like + et par = fullt hus.
        5 if flush else
        4 if straight else
        3 if (3, 1, 1) == counts else #3 like + 2 ulike.
        2 if (2, 2, 1) == counts else #2 par + 1 ulik.
        1 if (2, 1, 1, 1) == counts else #1 par + 3 ulike.
        0), rank
# Verdiene til de ulike kombinasjonene. ^

def group(items):
    # Returnerer en liste av telleren, x, hvor de høyeste tellerne og tallene kommer først
    groups = [(items.count(x), x) for x in set (items)]
    return sorted(groups, reverese = True)

def unzip(pairs):  #Pakker ut "pairs". 
    return zip(*pairs)

def card_ranks(hand):
    # Returner en liste med rangeringen på kortene, sortert etter høyest rang først.
    # Ess = 14
    # Konge = 13 osv...
    ranks = [14 if r == 'A' else
             13 if r == 'K' else
             12 if r == 'Q' else
             11 if r == 'J' else
             10 if r == 'T' else
             int (r)
             for r, s in hand]
    ranks.sort(reverse = True)
    return ranks if ranks != [14, 5, 4, 3, 2] else [5, 4, 3, 2, 1]

def straight(ranks):
    #Hvis kravene for straight er oppfylt returneres True
    return sum(ranks) - min(ranks)*5 == 10

def flush(hand):
    #Hvis alle kortene har like type(f.eks. ruter, spar) returneres True
    suits = [s for r, s in hand]
    return len(set(suits)) == 1
def two_pair(ranks):
    #Har en spiller to par, returneres to ranker som et par, rangeres høyest-lavest.
    result = [r for r in set(ranks) if ranks.count(r) == 2] #
    if len(result) ==2:
        return (max(result), min(result))
    
def kind(n, ranks):
    #Returner den første forekomsten av samme type kort som det finnes nøyaktig n av i den aktuelle hånden.
    for r in set(ranks):
        if ranks.count(r) == n:
            return r
        return None

def deal(numhands, n = 5, deck = [r+s for r in "23456789TQKA" for s in "SDHC"]):
    "Returnerer en liste med antall hender bestående av n(5) kort hver"
    random.shuffle(deck)
    deck = iter(deck) 
    return [[next(deck) for card in range (n)] for hand in range(numhands)]

def shuffle(deck):
    n = len(deck) #Lengden på decket.
    
    for i in range(n-1):
        j = random.randrange(i, n) #Tillater oss å produsere valg over et vilkårlig stot utvalg.
        deck[i], deck[j] = deck[j], deck[i]




def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    s1 = "AS 2S 3S 4S 5C".split() # A-5 straight
    s2 = "2C 3C 4C 5S 6S".split() # 2-6 straight
    s3 = "TC JC QC KS AS".split() # 10-A straight    
    tp = "5S 5D 9H 9C 6S".split() # two pair
    ah = "AS 2S 3S 4S 6C".split() # A high
    sh = "2S 3S 4S 6C 7D".split() # 7 high
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([sf]) == [sf]
    assert poker([sf] + 99*[fh]) == [sf]
    assert poker([s1, s2]) == [s2]
    assert poker([s1, tp]) == [s1]
    
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert card_ranks(['AC', '3D', '4S', 'KH']) == [14, 13, 4, 3]        


    assert (card_ranks(['AS', '2C', '3D', '4H', '6S']) >
            card_ranks(['2D', '3S', '4C', '6H', '7D']))  
    
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)

    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    assert two_pair(tpranks) == (9, 5)
    assert two_pair([10, 10, 5, 5, 2]) == (10, 5)    

    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False

    assert flush(sf) == True
    assert flush(fk) == False

    return 'tests pass'    

hand_names = [
    'High Card',
    'Pair',
    '2 Pair',
    '3 Kind',
    'Straight',
    'Flush',
    'Full House',
    '4 Kind',
    'Straight Flush',
    ]

def test_shufflers(shufflers=[shuffle, shuffle1], decks=['abc','ab']):
    for deck in decks:
        print
        for f in shufflers:
            test_shuffler(f, deck)

def factorial(n): return 1 if (n <= 1) else n*factorial(n-1) 
"""
Hvis n ikke er integrert eller negativ skal ikke programme kunne kjøre, og derfor gi feilkoden ValueError.
Dette gjøres for å forhindre ugyldige antall verdier. 
"""

"""
1. Vi er usikre på hvordan vi skal få programmet til å kjøre, og har dessverre ikke nok tid til å utvike en funksjon eller ny fil 
som kan få det til å kjøre.
2. Vi er usikre på hvordan syntaxen til en unittest skal se ut med våres pokerprogram, og har derfor valgt å bruke assert tester i
programmet. Assert testene er direkte kopiert fra kilden(se .pdf i github), da vi ikke har mer tid til å lage egne.
3. Vi er ikke 100% sikre på hva alt av koden som er brukt betyr, men har kommentert det meste. 

"""