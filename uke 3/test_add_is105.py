import unittest
from is105 import add

class TestAdd(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_100_7(self):
        self.assertEqual(add(100,7), 20)
        

if __name__ == '__main__':
    unittest.main()
    
    