class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        """
        Given a 0-indexed list of n integers `arr`, compute the sum of absolute
        interval distances between each element and every other element with the
        same value.

        The interval between two elements in `arr` is the absolute difference
        between their indices. For each index `i`, the output at `intervals[i]`
        is the sum of |i - j| for all j such that `arr[j] == arr[i]` and
        `j != i`.

        Args:
            arr (List[int]): The list of integers for which interval distances
                             are calculated.

        Returns:
            List[int]: A list where each element corresponds to the sum of
                       intervals for `arr[i]`.

        Example:
            Input: arr = [2,1,3,1,2,3,3]
            Output: [4,2,7,2,4,4,5]

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(arr)
        res = [0] * n

        nums_indices = defaultdict(list)
        for i, num in enumerate(arr):
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
