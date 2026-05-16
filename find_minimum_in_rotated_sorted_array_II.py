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

        Given the sorted rotated list nums that may contain duplicates, returns
        the minimum element of this list.

        Args:
            nums (List[int]): Rotated sorted list which may contain duplicate
                              integers.

        Returns:
            int: The minimum element in the list.

        Example:
            Input: nums = [2,2,2,0,1]
            Output: 0

        Time Complexity: O(log n) in the best case, O(n) in the worst case due
                         to possible duplicates
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]
