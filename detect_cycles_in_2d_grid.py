class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        """
        Determines if a 2D grid contains a cycle of the same value.

        A cycle is defined as a path of length 4 or more that starts and ends
        at the same cell. From any given cell, you can move to an adjacent
        cell (up, down, left, or right) if it has the same value.
        You cannot immediately return to the cell you just came from.

        Args:
            grid (List[List[str]]): 2D list of characters representing the grid.

        Returns:
            bool: True if any cycle of the same value exists in the grid,
                  otherwise False.

        Example:
            Input: grid = [
                ['a', 'a', 'a', 'a'],
                ['a', 'b', 'b', 'a'],
                ['a', 'b', 'b', 'a'],
                ['a', 'a', 'a', 'a']
            ]
            Output: True

        Time Complexity: O(m * n), where m and n are the number of rows and
                         columns in the grid.
        Space Complexity: O(m * n), for the visited set.
        """
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c, pr, pc, char):
            visited.add((r, c))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == char:
                    if (nr, nc) in visited and (nr, nc) != (pr, pc):
                        return True
                    if (nr, nc) not in visited:
                        if dfs(nr, nc, r, c, char):
                            return True
            return False

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    if dfs(r, c, -1, -1, grid[r][c]):
                        return True
        return False
