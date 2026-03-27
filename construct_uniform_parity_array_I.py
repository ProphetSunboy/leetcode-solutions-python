class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        """
        Given a list nums1 of n distinct integers.

        You want to construct another list nums2 of length n such that the
        elements in nums2 are either all odd or all even.

        For each index i, you must choose exactly one of the following
        (in any order):
            nums2[i] = nums1[i]
            nums2[i] = nums1[i] - nums1[j], for an index j != i

        Return True if it is possible to construct such a list, otherwise,
        return False.

        Args:
            nums1 (list[int]): The list of distinct integers.

        Returns:
            bool: True if a uniform parity list can be constructed,
            False otherwise.

        Example:
            Input: nums1 = [1, 2, 3, 4]
            Output: True

        Time Complexity: O(1).
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        return True
