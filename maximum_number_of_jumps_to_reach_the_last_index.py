class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        """
        Given a 0-indexed list `nums` of n integers and an integer `target`,
        you start at index 0. In one step, you can jump from index `i` to any
        index `j` such that:
            0 <= i < j < n
            -target <= nums[j] - nums[i] <= target

        Returns the maximum number of jumps needed to reach index n - 1.
        If it is not possible to reach index n - 1, returns -1.

        Args:
            nums (List[int]): The input list of integers.
            target (int): The maximum allowed absolute difference for a valid
                          jump.

        Returns:
            int: The maximum number of jumps to reach the last index, or -1 if
                 unreachable.

        Example:
            Input: nums = [1,3,6,4,1,2], target = 2
            Output: 3

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0

        for j in range(1, n):
            for i in range(j):
                if dp[i] != -1 and -target <= nums[j] - nums[i] <= target:
                    dp[j] = max(dp[j], dp[i] + 1)

        return dp[n - 1]
