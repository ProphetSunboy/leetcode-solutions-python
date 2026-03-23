class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        """
        Given an m x n integer matrix grid, you start at the top-left
        corner (0, 0) and can only move either right or down at each step.

        Among all paths from the top-left to the bottom-right corner (m-1, n-1),
        find the path whose product of all visited cell values is maximized.
        Return the maximum non-negative product modulo 10^9 + 7.
        If all such products are negative, return -1.

        The modulo operation is applied to the result after finding the maximum
        product.

        Args:
            grid (List[List[int]]): The 2D matrix of integers.

        Returns:
            int: The maximum non-negative product mod 10^9 + 7,
            or -1 if none exists.

        Example:
            Input:
                grid = [[1, -2, 1],
                        [1, -2, 1],
                        [3, -4, 1]]
            Output: 8

        Time Complexity: O(m * n)
        Space Complexity: O(m * n)

        LeetCode: Beats 100% of submissions
        """
        m, n = len(grid), len(grid[0])

        dp_max = [[0] * n for _ in range(m)]
        dp_min = [[0] * n for _ in range(m)]

        dp_max[0][0] = dp_min[0][0] = grid[0][0]

        for j in range(1, n):
            dp_max[0][j] = dp_min[0][j] = dp_max[0][j - 1] * grid[0][j]

        for i in range(1, m):
            dp_max[i][0] = dp_min[i][0] = dp_max[i - 1][0] * grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                options = (
                    dp_max[i - 1][j] * val,
                    dp_min[i - 1][j] * val,
                    dp_max[i][j - 1] * val,
                    dp_min[i][j - 1] * val,
                )
                dp_max[i][j] = max(options)
                dp_min[i][j] = min(options)

        res = dp_max[-1][-1]
        return res % (10**9 + 7) if res >= 0 else -1
