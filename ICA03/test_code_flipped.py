import unittest
from code_flip import rev_table

class TestCode(unittest.TestCase):
    def setUp(self):
        pass
    def test_codeReverse(self):
        self.assertEqual(rev_table()[' '], 7)