#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ testing for largest int """
    def test_none(self):
        self.assertEqual(max_integer([]), None)
        self.assertIsNone(max_integer([]))

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_max(self):
        self.assertEqual(max_integer([4, 6, 8, 46]), 46)

    def test_type(self):
        self.assertRaises(TypeError, max_integer((1, 2)))

if __name__ is "__main__":
    unittest.main()
