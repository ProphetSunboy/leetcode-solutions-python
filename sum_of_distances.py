class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        """
        Given a 0-indexed integer list nums, returns a list arr such that
        arr[i] is the sum of |i - j| over all j where nums[j] == nums[i] and
        j != i. If there is no such j, arr[i] is set to 0.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            list[int]: List where each element is the sum of distances for that
                       value.

        Example:
            Input: nums = [1, 3, 1, 1, 2]
            Output: [5, 0, 3, 4, 0]

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(nums)
        res = [0] * n

        nums_indices = defaultdict(list)
        for i, num in enumerate(nums):
            nums_indices[num].append(i)

        for num in nums_indices:
            indices = nums_indices[num]
            m = len(indices)

            total_sum = sum(indices)
            left_sum = 0

            for j, idx in enumerate(indices):
                right_sum = total_sum - left_sum - idx

                res[idx] = (idx * j - left_sum) + (right_sum - idx * (m - 1 - j))

                left_sum += idx

        return res
