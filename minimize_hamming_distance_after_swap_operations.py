class Solution:
    def minimumHammingDistance(
        self, source: list[int], target: list[int], allowedSwaps: list[list[int]]
    ) -> int:
        """
        Given two integer lists, source and target, both of length n, and a list
        of allowed swaps, where each allowedSwaps[i] = [ai, bi] indicates you
        can swap source[ai] and source[bi] any number of times and in any order.

        The Hamming distance between source and target is the number of
        positions with different values.

        This function returns the minimum Hamming distance between source and
        target after performing any amount of swap operations on source.

        Args:
            source (list[int]): The source list.
            target (list[int]): The target list.
            allowedSwaps (list[list[int]]): Allowed index swaps for source.

        Returns:
            int: The minimum possible Hamming distance after swaps.

        Example:
            Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
            Output: 1

        Time Complexity: O(n).
        Space Complexity: O(n).
        """
        n = len(source)
        parent = list(range(n))

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        for a, b in allowedSwaps:
            union(a, b)

        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        distance = 0

        for indices in groups.values():
            source_counts = Counter(source[i] for i in indices)
            target_counts = Counter(target[i] for i in indices)

            matches = 0
            for val, count in source_counts.items():
                if val in target_counts:
                    matches += min(count, target_counts[val])

            distance += len(indices) - matches

        return distance
