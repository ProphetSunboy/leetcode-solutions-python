class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        """
        Given an n x n matrix lcp, returns the lexicographically smallest
        string word of n lowercase English letters such that:

            lcp[i][j] == length of the longest common prefix between word[i:n]
            and word[j:n]

        If no such string exists, returns an empty string.

        A string a is lexicographically smaller than string b (of the same
        length) if at the first position where they differ, a has a letter that
        comes earlier in the alphabet than b.
        For example, "aabd" is smaller than "aaca".

        Args:
            lcp (List[List[int]]): n x n matrix describing longest common
            prefixes.

        Returns:
            str: The lexicographically smallest string satisfying lcp,
            or an empty string.

        Example:
            Input: lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
            Output: "abab"

        Time Complexity: O(n^2), where n is the length of lcp.
        Space Complexity: O(n).
        """
        n = len(lcp)
        res = [None] * n
        char_idx = 0

        for i in range(n):
            if res[i] is not None:
                continue
            if char_idx >= 26:
                return ""

            char = chr(ord("a") + char_idx)
            for j in range(i, n):
                if lcp[i][j] > 0:
                    res[j] = char
            char_idx += 1

        if None in res:
            return ""
        word = "".join(res)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                expected = 0
                if word[i] == word[j]:
                    if i == n - 1 or j == n - 1:
                        expected = 1
                    else:
                        expected = 1 + lcp[i + 1][j + 1]

                if lcp[i][j] != expected:
                    return ""

        return word
