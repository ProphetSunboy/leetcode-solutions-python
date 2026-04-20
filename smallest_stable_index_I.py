class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        """
        Given an integer list nums of length n and an integer k,
        for each index i, define its instability score as:
            max(nums[0..i]) - min(nums[i..n-1])

        Where:
            - max(nums[0..i]) is the largest value among elements from 
              index 0 to i.
            - min(nums[i..n-1]) is the smallest value among elements from 
              index i to n-1.

        An index i is called stable if its instability score is less than or 
        equal to k.

        Returns the smallest stable index. 
        If no such index exists, returns -1.

        Args:
            nums (list[int]): The input integer list.
            k (int): The instability threshold.

        Returns:
            int: The smallest stable index, or -1 if none exists.

        Example:
            Input: nums = [5,0,1,4], k = 3
            Output: 3

        Time Complexity: O(n log n)
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        curr_max = 0
        r = SortedList(nums)

        for i in range(len(nums)):
            curr_max = max(curr_max, nums[i])

            if curr_max - r[0] <= k:
                return i

            r.remove(nums[i])

        return -1