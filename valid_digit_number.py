class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        """
        Determine whether an integer n is a valid number based on digit x.

        A number is considered valid if:
            - It contains at least one occurrence of digit x, and
            - It does not start with digit x.

        Args:
            n (int): The integer to check.
            x (int): The digit to search for in n.

        Returns:
            bool: True if n is valid according to the criteria, False otherwise.

        Example:
            Input: n = 101, x = 0
            Output: true

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        return str(x) in str(n) and not str(n).startswith(str(x))
