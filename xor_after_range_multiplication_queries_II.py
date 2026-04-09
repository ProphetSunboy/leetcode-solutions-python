import numpy as np


class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        """
        Processes a list of queries on the input list, updating segments with
        multiplication, and returns the bitwise XOR of the resulting list.

        Each query is of the form [li, ri, ki, vi]:
            - For each index idx from li to ri (inclusive), stepping by ki:
                nums[idx] = (nums[idx] * vi) % (10**9 + 7)

        The function uses a numpy array named 'nums' as an intermediate variable
        to store the current state of the input list during the process.

        Args:
            nums (list[int]): The input list of integers.
            queries (list[list[int]]): Each query is a list [li, ri, ki, vi].

        Returns:
            int: The bitwise XOR of all elements in the list after processing
                 all queries.

        Example:
            Input: nums = [1,1,1], queries = [[0,2,1,4]]
            Output: 4

        Time Complexity: O(n + q), depending on query step sizes.
        Space Complexity: O(n), due to input list and intermediate storage.
        """
        MOD = 1_000_000_007
        N = len(nums)
        arr = np.array(nums, dtype=np.int64)

        BLOCK_SIZE = 120

        small_k = [[] for _ in range(BLOCK_SIZE)]

        for l, r, k, v in queries:
            if v == 1:
                continue
            if k >= BLOCK_SIZE:
                view = arr[l : r + 1 : k]
                np.multiply(view, v, out=view)
                np.remainder(view, MOD, out=view)
            else:
                small_k[k].append((l, r, v))

        for k in range(1, BLOCK_SIZE):
            if not small_k[k]:
                continue

            diff = np.ones(N + k + 1, dtype=np.int64)
            for l, r, v in small_k[k]:
                diff[l] = (diff[l] * v) % MOD
                last_idx = l + ((r - l) // k) * k
                r_next = last_idx + k
                if r_next < len(diff):
                    diff[r_next] = (diff[r_next] * pow(v, MOD - 2, MOD)) % MOD

            for i in range(k, N):
                diff[i] = (diff[i] * diff[i - k]) % MOD

            arr = (arr * diff[:N]) % MOD

        return int(np.bitwise_xor.reduce(arr))
