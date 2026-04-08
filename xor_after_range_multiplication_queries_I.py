class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        Given an integer list nums of length n and a 2D integer list queries of
        size q, where queries[i] = [li, ri, ki, vi], apply the following for
        each query:
            - Set idx = li.
            - While idx <= ri:
                - Update: nums[idx] = (nums[idx] * vi) % (10**9 + 7)
                - Set idx += ki.

        After processing all queries, return the bitwise XOR of all elements in
        nums.

        Args:
            nums (List[int]): The list of integers to be processed.
            queries (List[List[int]]): Each query contains [li, ri, ki, vi],
                representing the start index, end index (inclusive), step size,
                and multiplier value.

        Returns:
            int: The bitwise XOR of all elements in nums after processing all
            queries.

        Example:
            Input: nums = [1,1,1], queries = [[0,2,1,4]]
            Output: 4

        Time Complexity: O(q * n), where n is the number of elements affected
            by the queries.
        Space Complexity: O(1), in-place modification.
        """
        MOD = 10**9 + 7

        for l, r, k, v in queries:
            i = l

            while i <= r:
                nums[i] = (nums[i] * v) % MOD
                i += k

        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]

        return res
