class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        """
        Given an integer list nums, return a list of all valid elements in the
        same order as they appear in nums.

        An element nums[i] is considered valid if it satisfies at least one of
        the following:
            - It is strictly greater than every element to its left.
            - It is strictly greater than every element to its right.
            - The first and last elements are always valid.

        Args:
            nums (list[int]): The list of integers.

        Returns:
            list[int]: A list of valid elements from nums.

        Example:
            Input: nums = [1,2,4,2,3,2]
            Output: [1,2,4,3,2]

        Time Complexity: O(n)
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        valid = [False] * len(nums)
        l = 0

        for i, num in enumerate(nums):
            if num > l:
                valid[i] = True
            l = max(l, num)

        r = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > r:
                valid[i] = True
            r = max(r, nums[i])

        return [nums[i] for i in range(len(valid)) if valid[i]]
