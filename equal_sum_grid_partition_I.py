class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        """
        Determines if a horizontal or vertical cut can be made in the grid
        such that:
            - Each resulting section is non-empty.
            - The sum of elements in both sections is equal.

        Args:
            grid (List[List[int]]): An m x n matrix of positive integers.

        Returns:
            bool: True if such a partition exists, False otherwise.

        Example:
            Input: grid = [[1,4],[2,3]]
            Output: True

        Time Complexity: O(m + n), where m is the number of rows and n is the
        number of columns.
        Space Complexity: O(m + n), due to storing row and column sums.

        LeetCode: Beats 91.78% of submissions
        """
        m, n = len(grid), len(grid[0])
        rows_s = [sum(grid[i]) for i in range(m)]
        cols_s = [0] * n

        for j in range(n):
            curr = 0
            for i in range(m):
                curr += grid[i][j]

            cols_s[j] = curr

        l, r = 0, sum(rows_s)
        for row_s in rows_s:
            l += row_s
            r -= row_s

            if l == r:
                return True
            elif l > r:
                break

        l, r = 0, sum(cols_s)
        for col_s in cols_s:
            l += col_s
            r -= col_s

            if l == r:
                return True
            elif l > r:
                break

        return False
