import unittest
from PokerU5V12 import *

class PokerTest(unittest.TestCase):
    def setUp(self):
        pass
    def test():
        "Test cases for the functions in poker program"
        sf = "6D 7C 8C 9C TC".split() # Straight Flush
        fk = "9D x 9S 9C 7D".split() # Four of a Kind
        fh = "TD TC TH 7C 7D".split() # Full House
        s1 = "AS 2S 3S 4S 5C".split() # A-5 straight
        s2 = "2C 3C 4C 5S 6S".split() # 2-6 straight
        s3 = "TC JC QC KS AS".split() # 10-A straight    
        tp = "5S 5D 9H 9C 6S".split() # two pair
        ah = "AS 2S 3S 4S 6C".split() # A high
        sh = "2S 3S 4S 6C 7D".split() # 7 high
        assert poker([sf, fk, fh]) == [fk]
        assert poker([fk, fh]) == [fk]
        assert poker([fh, fh]) == [fh, fh]
        assert poker([sf]) == [sf]
        assert poker([sf] + 99*[fh]) == [sf]
        assert poker([s1, s2]) == [s2]
        assert poker([s1, tp]) == [s1]
"""
Her prøvde vi å lage en generell test for pokerprogrammet, men vi klarer ikke å få den til å fungere. 
Vi klarer ikke få den til å vise feilmeldinger, til tross for at i testen finnes det feil. 

"""