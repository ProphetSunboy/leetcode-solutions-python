class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        """
        Given a list of integers nums.

        From any index i, you can jump to another index j under the following
        rules:

            - Jump to index j where j > i is allowed only if nums[j] < nums[i].
            - Jump to index j where j < i is allowed only if nums[j] > nums[i].

        For each index i, find the maximum value in nums that can be reached by
        following any sequence of valid jumps starting at i.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            List[int]: A list ans where ans[i] is the maximum value reachable
                       starting from index i.

        Example:
            Input: nums = [2,3,1]
            Output: [3,3,3]

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n).
        """
        n = len(nums)

        suffixMin = [0] * (n + 1)
        suffixMin[n] = float("inf")
        for i in range(n - 1, -1, -1):
            suffixMin[i] = min(nums[i], suffixMin[i + 1])

        ans = [0] * n
        l = 0

        while l < n:
            r = l
            component_max = nums[l]

            while r + 1 < n and component_max > suffixMin[r + 1]:
                r += 1
                component_max = max(component_max, nums[r])

            for i in range(l, r + 1):
                ans[i] = component_max

            l = r + 1

        return ans
