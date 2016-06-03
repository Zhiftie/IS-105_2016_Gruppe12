import unittest
from moduleb import *

"""
Sjekker om table 101 i code() er w. noe den ikke er, da table[101] faktisk er e. 
"""

class TestMsg(unittest.TestCase):
    def setUp(self):
        pass    
    def test_table_entry_4(self):
        self.assertEqual(code()[101], 'w')


if __name__ == '__main__':
    unittest.main()