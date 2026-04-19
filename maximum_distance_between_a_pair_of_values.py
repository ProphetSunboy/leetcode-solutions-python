class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Given two non-increasing integer lists nums1 and nums2 (0-indexed),
        find the maximum distance of any valid pair (i, j) such that:
            - 0 <= i < len(nums1)
            - 0 <= j < len(nums2)
            - i <= j
            - nums1[i] <= nums2[j]

        The "distance" of the pair is defined as j - i.

        If there are no valid pairs, return 0.

        Args:
            nums1 (List[int]): First non-increasing list of integers.
            nums2 (List[int]): Second non-increasing list of integers.

        Returns:
            int: The maximum distance of any valid (i, j) pair, or 0 if none
            exist.

        Example:
            Input: nums1 = [55, 30, 5, 4, 2], nums2 = [100, 20, 10, 10, 5]
            Output: 2

        Time Complexity: O(n * log n)
        Space Complexity: O(1)
        """
        max_dist = 0
        nums2_asc = nums2[::-1]
        n2 = len(nums2)

        for i, val in enumerate(nums1):
            idx_in_asc = bisect.bisect_left(nums2_asc, val)

            j = n2 - 1 - idx_in_asc

            if j >= i:
                max_dist = max(max_dist, j - i)

        return max_dist
