class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        """
        Given an integer list nums of even length n and an integer limit,
        in one move, you can replace any integer from nums with another
        integer between 1 and limit, inclusive.

        The list nums is complementary if for all indices i (0-indexed),
        nums[i] + nums[n - 1 - i] equals the same number. For example,
        the list [1, 2, 3, 4] is complementary because for all indices i,
        nums[i] + nums[n - 1 - i] = 5.

        Returns the minimum number of moves required to make nums complementary.

        Args:
            nums (List[int]): List of integers of even length.
            limit (int): The upper bound (inclusive) of allowed replacements.

        Returns:
            int: The minimum number of moves required.

        Example:
            Input: nums = [1, 2, 4, 3], limit = 4
            Output: 1

        Time Complexity: O(n + limit).
        Space Complexity: O(limit).

        LeetCode: Beats 93.85% of submissions
        """
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            A = min(nums[i], nums[n - 1 - i])
            B = max(nums[i], nums[n - 1 - i])

            diff[A + 1] -= 1
            diff[B + limit + 1] += 1

            diff[A + B] -= 1
            diff[A + B + 1] += 1

        min_moves = n
        current_moves = n

        for target_sum in range(2, 2 * limit + 1):
            current_moves += diff[target_sum]
            if current_moves < min_moves:
                min_moves = current_moves

        return min_moves
