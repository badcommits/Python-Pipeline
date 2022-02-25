import unittest

class Testing(unittest.TestCase):

     def test_upper(self):
          string = 'hello world'
          self.assertEqual(string.isUpper(), 'HELLO WORLD')