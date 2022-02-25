import unittest

class Testing(unittest.TestCase):

     def test_upper(self):
          string = 'hello world'
          self.assertEqual(string.Upper(), 'HELLO WORLD')