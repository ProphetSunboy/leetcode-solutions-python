class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        """
        Given an m x n matrix of characters `boxGrid` representing a side-view
        of a box, where each cell is one of the following:
            - A stone: '#'
            - A stationary obstacle: '*'
            - Empty: '.'

        The box is rotated 90 degrees clockwise. After rotation, stones may fall
        downward due to gravity until they hit an obstacle, another stone, or
        the bottom of the box. Obstacles remain in the same position, and the
        change in orientation does not affect the stones' horizontal positions.

        It is guaranteed that each stone in `boxGrid` rests on an obstacle,
        another stone, or the bottom of the box.

        Args:
            boxGrid (List[List[str]]): The m x n matrix of characters
                                       representing the box.

        Returns:
            List[List[str]]: The n x m matrix representing the box after
                             rotation and gravity.

        Example:
            Input: boxGrid = [["#",".","#"]]
            Output: [["."],
                    ["#"],
                    ["#"]]

        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        m, n = len(boxGrid), len(boxGrid[0])

        for row in boxGrid:
            empty_pos = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == "*":
                    empty_pos = j - 1
                elif row[j] == "#":
                    row[j], row[empty_pos] = ".", "#"
                    empty_pos -= 1

        res = [["" for _ in range(m)] for _ in range(n)]
        for r in range(m):
            for c in range(n):
                res[c][m - 1 - r] = boxGrid[r][c]

        return res
