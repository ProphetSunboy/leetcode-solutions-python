class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        """
        Given an n x n adjacency matrix representing an undirected graph with
        n vertices labeled from 0 to n - 1, compute the degree of each vertex.

        Each matrix[i][j] == 1 indicates an edge between vertices i and j.
        Each matrix[i][j] == 0 indicates no edge.

        The degree of a vertex is the number of edges connected to it.

        Args:
            matrix (list[list[int]]): Adjacency matrix of the undirected graph.

        Returns:
            list[int]: A list where the i-th element is the degree of vertex i.

        Example:
            Input: matrix = [[0, 1], [1, 0]]
            Output: [1, 1]

        Time Complexity: O(n^2)
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        return [sum(vertex) for vertex in matrix]
