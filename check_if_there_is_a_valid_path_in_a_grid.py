class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        """
        Determines if there is a valid path in a given m x n grid.

        Each cell in the grid represents a street of a certain type:
            1: Connects left and right cells.
            2: Connects upper and lower cells.
            3: Connects left and lower cells.
            4: Connects right and lower cells.
            5: Connects left and upper cells.
            6: Connects right and upper cells.

        The path must start at the upper-left cell (0, 0) and end at the
        bottom-right cell (m - 1, n - 1), following only the streets as
        described.

        You are not allowed to change any street.

        Args:
            grid (list[list[int]]): The grid representing streets.

        Returns:
            bool: True if there is a valid path, False otherwise.

        Example:
            Input: grid = [[2,4,3],[6,5,2]]
            Output: True

        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        m, n = len(grid), len(grid[0])
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)],
        }

        visited = {(0, 0)}
        queue = [(0, 0)]

        while queue:
            r, c = queue.pop(0)
            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    if (-dr, -dc) in directions[grid[nr][nc]]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        return False
