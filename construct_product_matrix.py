class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Given a 0-indexed 2D integer matrix `grid` of size n x m, returns a 2D
        product matrix `p` of the same size such that each element p[i][j] is
        the product of all elements in `grid` except grid[i][j], modulo 12345.

        Args:
            grid (list[list[int]]): The input 2D matrix.

        Returns:
            list[list[int]]: The product matrix.

        Example:
            Input: grid = [[1, 2], [3, 4]]
            Output: [[24, 12], [8, 6]]

        Time Complexity: O(n * m), where n and m are the dimensions of grid.
        Space Complexity: O(n * m), due to the output matrix.

        LeetCode: Beats 98.01% of submissions
        """
        n, m = len(grid), len(grid[0])
        MOD = 12345
        res = [[1] * m for _ in range(n)]

        current_prod = 1
        for i in range(n):
            for j in range(m):
                res[i][j] = current_prod
                current_prod = (current_prod * grid[i][j]) % MOD

        current_prod = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                res[i][j] = (res[i][j] * current_prod) % MOD
                current_prod = (current_prod * grid[i][j]) % MOD

        return res
