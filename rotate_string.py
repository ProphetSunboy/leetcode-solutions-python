class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        Given two strings s and goal, return True if and only if s can become
        goal after some number of shifts on s.

        A shift on s consists of moving the leftmost character of s to the
        rightmost position. For example, if s = "abcde", then after one shift it
        becomes "bcdea".

        Args:
            s (str): The original string.
            goal (str): The target string.

        Returns:
            bool: True if s can become goal after some number of shifts,
                  False otherwise.

        Example:
            Input: s = "abcde", goal = "cdeab"
            Output: True

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(n).

        LeetCode: Beats 100% of submissions
        """
        return len(s) == len(goal) and goal in s + s
