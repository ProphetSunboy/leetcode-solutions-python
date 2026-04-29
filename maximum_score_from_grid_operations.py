class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        """
        Given a 2D matrix `grid` of size n x n, initially all cells are colored
        white. In one operation, you can select any cell at indices (i, j) and
        color black all the cells in the j-th column from the top row down to
        the i-th row.

        The grid score is the sum of all grid[i][j] such that cell (i, j) is
        white and it has a horizontally adjacent black cell.

        Returns the maximum score that can be achieved after some number of
        operations.

        Args:
            grid (List[List[int]]): The input 2D matrix.

        Returns:
            int: The maximum score obtainable.

        Example:
            Input: grid = [[0,0,0,0,0],
                           [0,0,3,0,0],
                           [0,1,0,0,0],
                           [5,0,0,3,0],
                           [0,0,0,0,2]]
            Output: 11

        Time Complexity: O(N^3)
        Space Complexity: O(N)
        """
        n = len(grid)
        NEG_INF = float("-inf")

        pre = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                pre[j][i + 1] = pre[j][i] + grid[i][j]

        def gain(j: int, lo: int, hi: int) -> int:
            if j < 0 or j >= n or hi <= lo:
                return 0
            return pre[j][hi] - pre[j][lo]

        A = [NEG_INF] * (n + 1)
        B = [NEG_INF] * (n + 1)
        C = [NEG_INF] * (n + 1)

        A[0] = 0
        B[0] = 0

        for col in range(n):
            nA = [NEG_INF] * (n + 1)
            nB = [NEG_INF] * (n + 1)
            nC = [NEG_INF] * (n + 1)

            for h0 in range(n + 1):
                for h1 in range(n + 1):
                    s_base = gain(col, h0, h1)

                    if h0 >= h1 and B[h1] != NEG_INF:
                        opt1 = B[h1] + (pre[col - 1][h0] if col > 0 else 0) + s_base
                    else:
                        opt1 = NEG_INF

                    opt2 = A[h1] + s_base if A[h1] != NEG_INF else NEG_INF

                    right3 = gain(col - 1, h1, h0) if col > 0 else 0
                    opt3 = C[h1] + right3 + s_base if C[h1] != NEG_INF else NEG_INF

                    val = max(opt1, opt2, opt3)
                    if val == NEG_INF:
                        continue

                    if h1 >= h0:
                        if val > nA[h0]:
                            nA[h0] = val
                        bv = val - pre[col][h1]
                        if bv > nB[h0]:
                            nB[h0] = bv
                    else:
                        if val > nC[h0]:
                            nC[h0] = val

            A, B, C = nA, nB, nC

        return max(
            max(
                A[h] if A[h] != NEG_INF else NEG_INF,
                C[h] if C[h] != NEG_INF else NEG_INF,
            )
            for h in range(n + 1)
        )
