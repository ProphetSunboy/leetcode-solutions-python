class Solution:
    def spiralMatrix(
        self, m: int, n: int, head: Optional[ListNode]
    ) -> List[List[List[int]]]:
        """
        Generates an m x n matrix filled with the values from a linked list in
        spiral order.

        The matrix is filled in a clockwise spiral pattern, starting from the
        top-left cell.
        If the linked list does not have enough values to fill the matrix,
        remaining cells are filled with -1.

        Args:
            m (int): Number of rows.
            n (int): Number of columns.
            head (Optional[ListNode]): The head node of the singly linked list
                containing integer values to fill the matrix.

        Returns:
            List[List[int]]: The generated m x n matrix filled in spiral order.

        Example:
            Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
            Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]

        Time Complexity: O(m * n), as every cell is visited once.
        Space Complexity: O(m * n), the space required for the resulting matrix.

        LeetCode: Beats 97.02% of submissions
        """
        res = [[-1] * n for _ in range(m)]

        top, bottom = 0, m - 1
        left, right = 0, n - 1

        curr = head
        while curr and top <= bottom and left <= right:
            for j in range(left, right + 1):
                if not curr:
                    return res
                res[top][j] = curr.val
                curr = curr.next
            top += 1

            for i in range(top, bottom + 1):
                if not curr:
                    return res
                res[i][right] = curr.val
                curr = curr.next
            right -= 1

            for j in range(right, left - 1, -1):
                if not curr:
                    return res
                res[bottom][j] = curr.val
                curr = curr.next
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                if not curr:
                    return res
                res[i][left] = curr.val
                curr = curr.next
            left += 1

        return res
