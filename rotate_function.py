class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        Given an integer list nums of length n, calculates the maximum value of
        the rotate function F.

        The rotate function F is defined as:
            F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1]
        where arrk is nums rotated clockwise by k positions.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The maximum value of F(0), F(1), ..., F(n-1).

        Example:
            Input: nums = [4, 3, 2, 6]
            Output: 26

        Time Complexity: O(n)
        Space Complexity: O(1)

        LeetCode: Beats 94.97% of submissions
        """
        n = len(nums)
        s = sum(nums)

        f = sum(i * v for i, v in enumerate(nums))
        max_val = f

        for i in range(1, n):
            f = f + s - n * nums[n - i]
            if f > max_val:
                max_val = f

        return max_val
