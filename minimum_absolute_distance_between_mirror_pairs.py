class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        """
        Given an integer list `nums`, finds the minimum absolute distance
        between the indices of any mirror pair.

        A mirror pair is defined as a pair of indices (i, j) such that:
            - 0 <= i < j < len(nums)
            - reverse(nums[i]) == nums[j], where reverse(x) is the integer
              formed by reversing the digits of x. Leading zeros are omitted
              after reversing. For example, reverse(120) == 21.

        The absolute distance between indices i and j is abs(i - j).

        If no mirror pair exists, returns -1.

        Args:
            nums (list[int]): The list of integers.

        Returns:
            int: The minimum absolute distance between mirror pairs, or -1 if
            none exist.

        Example:
            Input: nums = [12,21,45,33,54]
            Output: 1

        Time Complexity: O(n * k), where k is the number of digits in an integer.
        Space Complexity: O(n).
        """
        n = len(nums)
        min_dist = float("inf")
        nums_indices = defaultdict(list)

        for idx, num in enumerate(nums):
            nums_indices[num].append(idx)

        for i, num in enumerate(nums):
            target = int(str(num)[::-1])

            if target in nums_indices:
                indices = nums_indices[target]
                idx_in_list = bisect_right(indices, i)

                if idx_in_list < len(indices):
                    j = indices[idx_in_list]
                    min_dist = min(min_dist, j - i)

        return min_dist if min_dist != float("inf") else -1
