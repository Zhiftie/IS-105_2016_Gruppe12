import unittest
from code_flip import code

class TestCode(unittest.TestCase):
    def setUp(self):
        pass
    def test_code(self):
        self.assertEqual(code()[' '], 7)