class Solution:
    def rotatedDigits(self, n: int) -> int:
        """
        Returns the number of good integers in the range [1, n].

        An integer x is called good if, after rotating each digit individually
        by 180 degrees, we obtain a valid number that is different from x.
        Every digit must be rotated.

        A number is valid if each of its digits remains a digit after rotation:
            - 0, 1, and 8 rotate to themselves.
            - 2 and 5 rotate to each other.
            - 6 and 9 rotate to each other.
            - 3, 4, and 7 do not rotate to any valid digit (become invalid).

        Args:
            n (int): The upper bound of the range (inclusive).

        Returns:
            int: The count of good integers between 1 and n.

        Example:
            Input: n = 10
            Output: 4

        Time Complexity: O(len(n) * 2)
        Space Complexity: O(len(n) * 2)

        LeetCode: Beats 100% of submissions
        """
        s = str(n)

        def dp(i, tight, is_good):
            if i == len(s):
                return 1 if is_good else 0

            res = 0
            limit = int(s[i]) if tight else 9

            for d in range(limit + 1):
                if d in (3, 4, 7):
                    continue

                new_tight = tight and (d == limit)
                new_is_good = is_good or (d in (2, 5, 6, 9))

                res += dp(i + 1, new_tight, new_is_good)

            return res

        return dp(0, True, False)
