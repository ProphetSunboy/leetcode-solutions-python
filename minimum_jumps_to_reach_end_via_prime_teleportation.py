class Solution:
    def minJumps(self, nums: List[int]) -> int:
        """
        Given an integer list `nums` of length n, starting at index 0, the goal
        is to reach index n - 1 using the minimum number of jumps.

        At each move from index i, you may:
            - Take an adjacent step to index i + 1 or i - 1, if in bounds.
            - Use prime teleportation:
                If nums[i] is a prime p, instantly jump to any index j (j != i)
                such that nums[j] % p == 0.

        Returns:
            int: The minimum number of jumps required to reach index n - 1.

        Example:
            Input: nums = [1,2,4,6]
            Output: 2

        Time Complexity: O(N * log(log(max_num))).
        Space Complexity: O(N + max_num).
        """
        n = len(nums)
        if n <= 1:
            return 0

        max_num = max(nums)
        min_prime = [0] * (max_num + 1)
        for i in range(2, int(max_num**0.5) + 1):
            if min_prime[i] == 0:
                for j in range(i * i, max_num + 1, i):
                    if min_prime[j] == 0:
                        min_prime[j] = i
        for i in range(2, max_num + 1):
            if min_prime[i] == 0:
                min_prime[i] = i

        def get_prime_factors(num):
            factors = set()
            while num > 1:
                p = min_prime[num]
                factors.add(p)
                while num % p == 0:
                    num //= p
            return factors

        prime_to_indices = defaultdict(list)
        for i, val in enumerate(nums):
            for p in get_prime_factors(val):
                prime_to_indices[p].append(i)

        queue = deque([(0, 0)])
        visited_indices = {0}
        visited_primes = set()

        while queue:
            curr_idx, dist = queue.popleft()

            if curr_idx == n - 1:
                return dist

            for neighbor in [curr_idx - 1, curr_idx + 1]:
                if 0 <= neighbor < n and neighbor not in visited_indices:
                    visited_indices.add(neighbor)
                    queue.append((neighbor, dist + 1))

            val = nums[curr_idx]
            if min_prime[val] == val:
                p = val
                if p not in visited_primes:
                    for next_idx in prime_to_indices[p]:
                        if next_idx not in visited_indices:
                            visited_indices.add(next_idx)
                            queue.append((next_idx, dist + 1))
                    visited_primes.add(p)

        return -1
