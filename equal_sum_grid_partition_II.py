class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        """
        Determines if an m x n grid of positive integers can be partitioned
        with a single horizontal or vertical cut into two non-empty sections
        such that:

        - The sum of elements in both sections is equal, or can be made equal by
          discounting at most one single cell in total (from either section).
        - If a cell is discounted, the rest of the section must remain
          connected.

        A section is connected if every cell in it can be reached from any other
        cell by moving up, down, left, or right through other cells in the
        section.

        Args:
            grid (List[List[int]]): The m x n matrix of positive integers.

        Returns:
            bool: True if such a partition exists, False otherwise.

        Example:
            Input: grid = [[1,2],[3,4]]
            Output: True

        Time Complexity: O(m * n).
        Space Complexity: O(m * n).

        LeetCode: Beats 97.22% of submissions
        """
        m, n = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)

        def check_orientation(matrix, R, C):
            row_sums = [sum(r) for r in matrix]

            prefix_sum = 0
            seen_prefix = set()

            for i in range(R - 1):
                prefix_sum += row_sums[i]
                for val in matrix[i]:
                    seen_prefix.add(val)

                other_sum = total_sum - prefix_sum

                if prefix_sum == other_sum:
                    return True

                x = prefix_sum - other_sum
                if x > 0:
                    if (i + 1) > 1 and C > 1:
                        if x in seen_prefix:
                            return True
                    else:
                        if (i + 1) == 1:
                            if matrix[0][0] == x or matrix[0][C - 1] == x:
                                return True
                        else:
                            if matrix[0][0] == x or matrix[i][0] == x:
                                return True

            suffix_sum = 0
            seen_suffix = set()
            for i in range(R - 1, 0, -1):
                suffix_sum += row_sums[i]
                for val in matrix[i]:
                    seen_suffix.add(val)

                other_sum = total_sum - suffix_sum
                x = suffix_sum - other_sum
                if x > 0:
                    if (R - i) > 1 and C > 1:
                        if x in seen_suffix:
                            return True
                    else:
                        if (R - i) == 1:
                            if matrix[R - 1][0] == x or matrix[R - 1][C - 1] == x:
                                return True
                        else:
                            if matrix[i][0] == x or matrix[R - 1][0] == x:
                                return True
            return False

        if check_orientation(grid, m, n):
            return True

        transposed = [list(row) for row in zip(*grid)]
        if check_orientation(transposed, n, m):
            return True

        return False
