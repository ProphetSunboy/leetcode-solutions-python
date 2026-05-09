class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        Rotates each layer of an m x n integer matrix `grid` by `k` positions
        in the counter-clockwise direction.

        Each layer is defined as the set of elements that form a closed loop
        around the matrix, starting from the outermost layer and moving inward.
        A single rotation moves each element of a layer to the position of its
        adjacent element in the counter-clockwise direction. All layers are
        rotated independently.

        Args:
            grid (List[List[int]]): An m x n matrix of integers, with both m and
                                    n even.
            k (int): The number of times to cyclically rotate each layer.

        Returns:
            List[List[int]]: The matrix after applying k cyclic rotations to
                             each layer.

        Example:
            Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
                   k = 2
            Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]

        Time Complexity: O(m * n), where m and n are the grid dimensions.
        Space Complexity: O(min(m, n)), for the space used to store layer
                          elements.

        LeetCode: Beats 100% of submissions
        """
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2

        for layer in range(num_layers):
            elements = deque()

            for j in range(layer, n - 1 - layer):
                elements.append(grid[layer][j])
            for i in range(layer, m - 1 - layer):
                elements.append(grid[i][n - 1 - layer])
            for j in range(n - 1 - layer, layer, -1):
                elements.append(grid[m - 1 - layer][j])
            for i in range(m - 1 - layer, layer, -1):
                elements.append(grid[i][layer])

            net_rotation = k % len(elements)
            elements.rotate(-net_rotation)

            for j in range(layer, n - 1 - layer):
                grid[layer][j] = elements.popleft()
            for i in range(layer, m - 1 - layer):
                grid[i][n - 1 - layer] = elements.popleft()
            for j in range(n - 1 - layer, layer, -1):
                grid[m - 1 - layer][j] = elements.popleft()
            for i in range(m - 1 - layer, layer, -1):
                grid[i][layer] = elements.popleft()

        return grid
