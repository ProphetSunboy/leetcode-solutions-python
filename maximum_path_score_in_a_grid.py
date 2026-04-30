class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        """
        Calculate the maximum score obtainable from the top-left to the
        bottom-right of an m x n grid using at most k cost.

        Each cell in the grid contains one of the following values:
            0: adds 0 to the score, costs 0
            1: adds 1 to the score, costs 1
            2: adds 2 to the score, costs 1

        The movement is restricted to only right or down.

        The path is valid only if the total cost does not exceed k upon reaching
        the last cell.

        Args:
            grid (List[List[int]]): 2D grid containing cell values {0, 1, 2}.
            k (int): Maximum allowed total cost for the path.

        Returns:
            int: Maximum achievable score without exceeding total cost k,
                 or -1 if no valid path exists.

        Example:
            Input:
                grid = [[0, 1],[2, 0]]
                k = 1
            Output: 2

        Time Complexity: O(m * n * k)
        Space Complexity: O(m * n * k)
        """
        m = len(grid)
        n = len(grid[0])

        def get_vals(val):
            if val == 0:
                return 0, 0
            if val == 1:
                return 1, 1
            if val == 2:
                return 2, 1
            return 0, 0

        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]

        start_score, start_cost = get_vals(grid[0][0])
        if start_cost <= k:
            dp[0][0][start_cost] = start_score
        else:
            return -1

        for r in range(m):
            for c in range(n):
                cell_score, cell_cost = get_vals(grid[r][c])

                for current_cost in range(k + 1):
                    if dp[r][c][current_cost] == -1:
                        continue

                    current_score = dp[r][c][current_cost]

                    if c + 1 < n:
                        next_score, next_cost = get_vals(grid[r][c + 1])
                        total_cost = current_cost + next_cost
                        if total_cost <= k:
                            dp[r][c + 1][total_cost] = max(
                                dp[r][c + 1][total_cost], current_score + next_score
                            )

                    if r + 1 < m:
                        next_score, next_cost = get_vals(grid[r + 1][c])
                        total_cost = current_cost + next_cost
                        if total_cost <= k:
                            dp[r + 1][c][total_cost] = max(
                                dp[r + 1][c][total_cost], current_score + next_score
                            )

        res = max(dp[m - 1][n - 1])
        return res if res != -1 else -1
