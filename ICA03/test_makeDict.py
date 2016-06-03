import unittest
from makeDict import testString, makeDict

class TestCode(unittest.TestCase):
    def setUp(self):
        pass
    def test_makeDict(self):
        self.assertEqual(makeDict(testString)[3], testString[2])