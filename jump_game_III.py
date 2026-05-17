class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """
        Determines if it's possible to reach any index with value 0 in the
        given list.

        You are initially positioned at the given start index of the list.
        At each step, you can jump to either i + arr[i] or i - arr[i],
        where i is your current position. You cannot jump outside of the list.

        Args:
            arr (List[int]): List of non-negative integers.
            start (int): Starting index.

        Returns:
            bool: True if it is possible to reach any index with value 0,
                  False otherwise.

        Example:
            Input: arr = [4, 2, 3, 0, 3, 1, 2], start = 5
            Output: True

        Time Complexity: O(n)
        Space Complexity: O(n)

        LeetCode: Beats 97.28% of submissions
        """
        can_reach = [start]
        seen = set()

        while can_reach:
            curr = can_reach.pop()
            seen.add(curr)
            if arr[curr] == 0:
                return True

            l, r = curr - arr[curr], curr + arr[curr]
            if l >= 0 and l not in seen:
                can_reach.append(l)
            if r < len(arr) and r not in seen:
                can_reach.append(r)

        return False
