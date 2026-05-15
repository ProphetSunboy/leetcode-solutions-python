class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Finds the minimum element in a rotated sorted list of unique elements.

        Suppose a list of length n sorted in ascending order is rotated between
        1 and n times.
        For example, the list nums = [0, 1, 2, 4, 5, 6, 7] might become:
            [4, 5, 6, 7, 0, 1, 2] if rotated 4 times,
            [0, 1, 2, 4, 5, 6, 7] if rotated 7 times.
        Rotating a list [a[0], a[1], ..., a[n-1]] 1 time results in
        [a[n-1], a[0], ..., a[n-2]].

        Args:
            nums (List[int]): The rotated sorted list of unique integers.

        Returns:
            int: The minimum element in the list.

        Example:
            Input: nums = [3, 4, 5, 1, 2]
            Output: 1

        Time Complexity: O(log n)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
