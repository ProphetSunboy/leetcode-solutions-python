class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        """
        Given an m x n grid, where each cell coins[i][j] contains:
            - A non-negative value: robot gains coins.
            - A negative value: robot encounters a robber and loses
              abs(coins[i][j]) coins.

        The robot starts at the top-left (0, 0) and wants to reach the
        bottom-right (m-1, n-1), moving only right or down.
        The robot can neutralize robbers in at most 2 cells so that no coins
        are lost in those cells.

        The robot's total coins may be negative.

        Args:
            coins (list[list[int]]): The grid of coins.

        Returns:
            int: The maximum amount of money the robot can earn.

        Example:
            Input: coins = [
                [0,1,-1],
                [1,-2,3],
                [2,-3,4]
            ]
            Output: 8

        Time Complexity: O(m * n * 3), where m and n are the grid's dimensions.
        Space Complexity: O(m * n * 3)
        """
        m, n = len(coins), len(coins[0])
        dp = [[[-float("inf")] * 3 for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0

        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if dp[i][j][k] == -float("inf"):
                        continue

                    for ni, nj in [(i + 1, j), (i, j + 1)]:
                        if ni < m and nj < n:
                            val = coins[ni][nj]

                            dp[ni][nj][k] = max(dp[ni][nj][k], dp[i][j][k] + val)

                            if k < 2 and val < 0:
                                dp[ni][nj][k + 1] = max(dp[ni][nj][k + 1], dp[i][j][k])

        return max(dp[m - 1][n - 1])
