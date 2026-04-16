class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        Given a circular list nums and a list of queries, for each query
        index i, find the minimum distance between the element at index
        queries[i] and any other index j in the circular list such that
        nums[j] == nums[queries[i]].
        If no such index exists, return -1 for that query.

        Args:
            nums (List[int]): The circular list of integers.
            queries (List[int]): List of query indices.

        Returns:
            List[int]: A list where each element is the result for the
            corresponding query. Each result is the minimum circular distance
            to another occurrence of nums[queries[i]], or -1 if none exists.

        Example:
            Input: nums = [1,3,1,4,1,3,2], queries = [0,3,5]
            Output: [2,-1,3]

        Time Complexity: O(Q * log N), where Q is the number of queries and N is
        the length of nums.
        Space Complexity: O(N).
        """
        n = len(nums)
        nums_indices = defaultdict(list)

        for i, num in enumerate(nums):
            nums_indices[num].append(i)

        answer = []
        for q in queries:
            target_val = nums[q]
            indices = nums_indices[target_val]

            if len(indices) <= 1:
                answer.append(-1)
                continue

            idx_in_list = bisect.bisect_left(indices, q)

            left_neighbor = indices[idx_in_list - 1]
            right_neighbor = indices[(idx_in_list + 1) % len(indices)]

            dist_left = abs(q - left_neighbor)
            dist_left = min(dist_left, n - dist_left)

            dist_right = abs(q - right_neighbor)
            dist_right = min(dist_right, n - dist_right)

            answer.append(min(dist_left, dist_right))

        return answer
