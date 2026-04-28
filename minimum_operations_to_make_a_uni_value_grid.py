class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        """
        Given a 2D integer grid of size m x n and an integer x, in one
        operation, you can add or subtract x from any element in the grid.

        A uni-value grid is a grid where all the elements are equal.

        Returns the minimum number of operations to make the grid uni-value.
        If it is not possible, returns -1.

        Args:
            grid (List[List[int]]): The input 2D grid.
            x (int): The increment/decrement value for each operation.

        Returns:
            int: The minimum number of operations to make all grid elements
                equal, or -1 if impossible.

        Example:
            Input: grid = [[2,4],[6,8]], x = 2
            Output: 4

        Time Complexity: O(m*n log(m*n)).
        Space Complexity: O(m*n).

        LeetCode: Beats 93.84% of submissions
        """
        nums = []
        for row in grid:
            nums.extend(row)

        remainder = nums[0] % x
        for n in nums:
            if n % x != remainder:
                return -1

        nums.sort()
        median = nums[len(nums) // 2]

        operations = 0
        for n in nums:
            operations += abs(n - median) // x

        return operations
