# Python script to demonstrate unit testing the add() function

# Import the required module(s)
import unittest
from add import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 2), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-3, -5), -8)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-4, 2), -2)