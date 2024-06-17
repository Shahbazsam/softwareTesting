class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverses the digits of an integer.

        Args:
            x: The integer to reverse.

        Returns:
            The reversed integer. If reversing x causes the value to go outside
            the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.
        """
        is_negative = x < 0
        reversed_str = str(abs(x))[::-1]
        reversed_int = int(reversed_str)

        if reversed_int > 2**31 - 1:
            return 0

        return reversed_int if not is_negative else -reversed_int