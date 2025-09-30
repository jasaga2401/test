"""
Unit tests for the hello module.
"""

import unittest
from hello import greet


class TestGreet(unittest.TestCase):
    """Test cases for the greet function."""
    
    def test_greet_default(self):
        """Test greet with default parameter."""
        result = greet()
        self.assertEqual(result, "Hello, World!")
    
    def test_greet_with_name(self):
        """Test greet with a custom name."""
        result = greet("Python")
        self.assertEqual(result, "Hello, Python!")
    
    def test_greet_with_empty_string(self):
        """Test greet with an empty string."""
        result = greet("")
        self.assertEqual(result, "Hello, !")


if __name__ == "__main__":
    unittest.main()
