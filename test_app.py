import unittest
from app import factorial, is_positive


class TestApp(unittest.TestCase):
    def test_factorial(self):
        """Test the factorial function."""
        self.assertEqual(factorial(0), 1)  # 0! is 1
        self.assertEqual(factorial(1), 1)  # 1! is 1
        self.assertEqual(factorial(5), 120)  # 5! is 120
        self.assertEqual(factorial(7), 5040)  # 7! is 5040

    def test_factorial_negative_input(self):
        """Test factorial with a negative input (should raise an error)."""
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_is_positive(self):
        """Test the is_positive function."""
        self.assertTrue(is_positive(5))  # 5 is positive
        self.assertFalse(is_positive(-3))  # -3 is not positive


if __name__ == '__main__':
    unittest.main()
