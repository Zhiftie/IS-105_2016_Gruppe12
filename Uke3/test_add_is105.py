import unittest
from is105 import add, mult, sub, div

class TestAdd(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_100_7(self):
        self.assertEqual(add(27,20),47)

class TestSub(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_200_80(self):
        self.assertEqual(sub(200, 80),120)

class TestMult(unittest.TestCase):
    def setUp(self):
        pass
    def test_number_25_4(self):
        self.assertEqual(mult(30,4),120)
        
class TestDiv(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_120_5(self):
        self.assertEqual(div(100,5),20)
