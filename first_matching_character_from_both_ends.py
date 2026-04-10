class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        """
        Given a string s of length n consisting of lowercase English letters,
        return the smallest index i such that s[i] == s[n - i - 1].

        If no such index exists, return -1.

        Args:
            s (str): The input string.

        Returns:
            int: The smallest index i where s[i] == s[n - i - 1], or -1 if no
            such index exists.

        Example:
            Input: s = "abccba"
            Output: 0  # s[0] == s[5] == 'a'

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] == s[r]:
                return l

            l += 1
            r -= 1

        return -1
