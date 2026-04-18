# First solution
class Solution:
    def mirrorDistance(self, n: int) -> int:
        """
        Given an integer n, return its mirror distance, defined as abs(n - reverse(n)),
        where reverse(n) is the integer formed by reversing the digits of n.

        Args:
            n (int): The integer for which to compute the mirror distance.

        Returns:
            int: The mirror distance between n and its digit-reversal.

        Example:
            Input: n = 123
            Output: 198
            Explanation: reverse(123) = 321, abs(123 - 321) = 198

        Time Complexity: O(log n), where n is the value of the integer.
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        mirror = 0
        m = n
        while m > 0:
            mirror = mirror * 10 + m % 10
            m //= 10

        return abs(n - mirror)


# Second solution
class Solution:
    def mirrorDistance(self, n: int) -> int:
        """
        Given an integer n, return its mirror distance, defined as abs(n - reverse(n)),
        where reverse(n) is the integer formed by reversing the digits of n.

        Args:
            n (int): The integer for which to compute the mirror distance.

        Returns:
            int: The mirror distance between n and its digit-reversal.

        Example:
            Input: n = 123
            Output: 198
            Explanation: reverse(123) = 321, abs(123 - 321) = 198

        Time Complexity: O(log n), where n is the value of the integer.
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        return abs(n - int(str(n)[::-1]))
