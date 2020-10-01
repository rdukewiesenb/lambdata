"""
Example tests using the standard documentation
"""

import unittest



"""
DOCUMTNETATION:
Inheriting from unittest.TestCase class.
Undercores indicate what we are testing
    Ex. `test_[thing we're testing]`
`FOO` means a boolean 'yes' or 'no', 'pass' or 'fail.'
"""
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()