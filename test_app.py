"""Tests for the test application."""

import unittest
from app import greet, add


class TestApp(unittest.TestCase):
    """Test cases for the application functions."""
    
    def test_greet_default(self):
        """Test greet function with default argument."""
        self.assertEqual(greet(), "Hello, World!")
    
    def test_greet_with_name(self):
        """Test greet function with a specific name."""
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")
    
    def test_add_positive_numbers(self):
        """Test add function with positive numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)
    
    def test_add_negative_numbers(self):
        """Test add function with negative numbers."""
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-10, 5), -5)
    
    def test_add_zero(self):
        """Test add function with zero."""
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)
    
    def test_add_floats(self):
        """Test add function with floating point numbers."""
        self.assertAlmostEqual(add(1.5, 2.3), 3.8)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)


if __name__ == "__main__":
    unittest.main()
