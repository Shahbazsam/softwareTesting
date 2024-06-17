import unittest
from solution import Solution

class ReverseIntegerTest(unittest.TestCase):

    def setUp(self):
        """Setup method for the test class."""
        self.solution = Solution()

    def test_reverse_positive_integer(self):
        """Test case for reversing a positive integer."""
        self.assertEqual(self.solution.reverse(123), 321)

    def test_reverse_negative_integer(self):
        """Test case for reversing a negative integer."""
        self.assertEqual(self.solution.reverse(-123), -321)

    def test_reverse_integer_with_zero(self):
        """Test case for reversing an integer with trailing zeros."""
        self.assertEqual(self.solution.reverse(120), 21)

    def test_reverse_integer_overflow(self):
        """Test case for reversing an integer that causes overflow."""
        self.assertEqual(self.solution.reverse(1534236469), 0)

    def test_reverse_integer_overflow_negative(self):
        """Test case for reversing an integer that causes overflow (negative)."""
        self.assertEqual(self.solution.reverse(-2147483648), 0)

if __name__ == '__main__':
    unittest.main()