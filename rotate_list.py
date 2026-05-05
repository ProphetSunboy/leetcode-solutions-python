# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Rotate a singly linked list to the right by k places.

        Args:
            head (Optional[ListNode]): The head of the singly linked list.
            k (int): Number of positions to rotate the list.

        Returns:
            Optional[ListNode]: The new head of the rotated linked list.

        Example:
            Input: head = [1, 2, 3, 4, 5], k = 2
            Output: [4, 5, 1, 2, 3]

        Time Complexity: O(n), where n is the length of the linked list.
        Space Complexity: O(n), due to the use of an auxiliary list.

        LeetCode: Beats 100% of submissions
        """
        if not head:
            return head

        values = []
        curr = head

        while curr.next:
            values.append(curr.val)
            curr = curr.next

        values.append(curr.val)
        rotations = k % len(values)

        values = values[-rotations:] + values[:-rotations]
        rotated_head = ListNode()
        dummy = rotated_head

        for i in range(len(values) - 1):
            dummy.val = values[i]
            dummy.next = ListNode()
            dummy = dummy.next

        dummy.val = values[-1]

        return rotated_head
