import unittest
from moduleb import code

class TestCode2(unittest.TestCase):
    def setUp(self):
        pass
    def test_code_2(self):
        self.assertEqual(code()[14],"SO")
        
if __name__ == '__main__':
    unittest.main()