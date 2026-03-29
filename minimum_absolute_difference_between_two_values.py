class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        """
        Given an integer list nums consisting only of 0, 1, and 2,
        finds the minimum absolute difference between indices i and j
        among all valid pairs (i, j) such that nums[i] == 1 and nums[j] == 2.

        If no valid pair exists, returns -1.

        The absolute difference is defined as abs(i - j).

        Args:
            nums (list[int]): List of integers containing only 0, 1, and 2.

        Returns:
            int: The minimum absolute difference between the index of
            a 1 and a 2, or -1 if no valid pair exists.

        Example:
            Input: nums = [1,0,0,2,0,1]
            Output: 2

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        min_dif = float("inf")
        prev_one, prev_two = -1, -1

        for i, num in enumerate(nums):
            if num == 1:
                prev_one = i

                if prev_two > -1:
                    min_dif = min(min_dif, i - prev_two)
            elif num == 2:
                prev_two = i

                if prev_one > -1:
                    min_dif = min(min_dif, i - prev_one)

        return min_dif if min_dif < float("inf") else -1
