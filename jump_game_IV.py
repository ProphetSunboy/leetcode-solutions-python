class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """
        Given a list of integers arr, you are initially positioned at the first
        index of the list.

        In one step you can jump from index i to index:
            - i + 1 where i + 1 < len(arr)
            - i - 1 where i - 1 >= 0
            - j where arr[i] == arr[j] and i != j

        Return the minimum number of steps to reach the last index of the list.
        You cannot jump outside of the list at any time.

        Args:
            arr (List[int]): The list of integers.

        Returns:
            int: The minimum number of steps to reach the last index.

        Example:
            Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
            Output: 3

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(arr)
        if n <= 1:
            return 0

        indices = defaultdict(list)
        for i, num in enumerate(arr):
            indices[num].append(i)

        queue = deque([(0, 0)])

        visited = {0}

        while queue:
            curr, steps = queue.popleft()

            if curr == n - 1:
                return steps

            if arr[curr] in indices:
                for next_idx in indices[arr[curr]]:
                    if next_idx not in visited:
                        visited.add(next_idx)
                        queue.append((next_idx, steps + 1))
                del indices[arr[curr]]

            if curr + 1 < n and (curr + 1) not in visited:
                visited.add(curr + 1)
                queue.append((curr + 1, steps + 1))

            if curr - 1 >= 0 and (curr - 1) not in visited:
                visited.add(curr - 1)
                queue.append((curr - 1, steps + 1))

        return 0
