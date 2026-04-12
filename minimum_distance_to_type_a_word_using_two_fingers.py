from functools import lru_cache


class Solution:
    def minimumDistance(self, word: str) -> int:
        """
        Given a keyboard layout where each uppercase English letter occupies a
        coordinate, return the minimum total distance to type the given word
        using only two fingers.

        Each letter 'A'-'Z' is at an (x, y) coordinate, e.g.:
            'A' -> (0, 0)
            'B' -> (0, 1)
            'P' -> (2, 3)
            'Z' -> (4, 1)

        The distance between two coordinates (x1, y1) and (x2, y2) is defined as:
            |x1 - x2| + |y1 - y2|

        The initial positions of your two fingers may be anywhere without cost.
        The fingers do not need to start at the first letter or at the first
        two letters.

        Args:
            word (str): The input string consisting of uppercase English letters.

        Returns:
            int: The minimum total distance required to type the string using
            two fingers.

        Example:
            Input: word = "CAKE"
            Output: 3

        Time Complexity: O(n), where n is the length of word.
        Space Complexity: O(n^2), due to memoization.
        """

        @lru_cache(None)
        def get_coords(char):
            if char is None:
                return None
            idx = ord(char) - ord("A")
            return divmod(idx, 6)

        def dist(c1, c2):
            if c1 is None or c2 is None:
                return 0
            p1, p2 = get_coords(c1), get_coords(c2)
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        @lru_cache(None)
        def solve(idx, other_pos):
            if idx == len(word):
                return 0

            curr_char = word[idx]
            prev_char = word[idx - 1] if idx > 0 else None

            res1 = dist(prev_char, curr_char) + solve(idx + 1, other_pos)

            res2 = dist(other_pos, curr_char) + solve(idx + 1, prev_char)

            return min(res1, res2)

        return solve(0, None)
