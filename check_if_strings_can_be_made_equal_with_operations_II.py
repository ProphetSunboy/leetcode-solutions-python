class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        """
        Determines if two strings s1 and s2 can be made equal by applying a
        specific operation any number of times. The allowed operation is to
        swap characters at two indices i and j (with i < j and (j - i) even)
        in either string.

        Args:
            s1 (str): The first input string.
            s2 (str): The second input string.

        Returns:
            bool: True if s1 can be made equal to s2, False otherwise.

        Example:
            Input: s1 = "abcd", s2 = "cdab"
            Output: True

        Time Complexity: O(n), where n is the length of the strings.
        Space Complexity: O(n), for the use of counters.

        LeetCode: Beats 93.28% of submissions
        """
        return Counter(s1[0::2]) == Counter(s2[0::2]) and Counter(s1[1::2]) == Counter(
            s2[1::2]
        )
