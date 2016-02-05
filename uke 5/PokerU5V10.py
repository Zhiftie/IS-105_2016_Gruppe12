import random #random generator
import math 
import itertools
from collections import defaultdict

def poker(hands):
    #Returner en liste med vinnerhendene. 
    return allmax(hands, key =hand_rank)

def allmax(iterable, key=lambda x:x):
    maxi = max(iterable, key=key)
    return [element for element in iterable if key(element) == key(maxi)]

def hand_rank(hand):
    #Returnerer en verdi som viser hvor høyt hånden kan rangeres.
    groups = group(['--23456789TJQKA'.index(r) for r, s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14,5,4,3,2):
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

def unzip(pairs):
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
    #Hvis kravene for straight er oppfylt S