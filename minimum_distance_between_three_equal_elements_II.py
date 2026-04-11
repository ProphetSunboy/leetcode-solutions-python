class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        """
        Given an integer list nums, finds the minimum possible distance of a
        good tuple.

        A tuple (i, j, k) of 3 distinct indices is good if
        nums[i] == nums[j] == nums[k].

        The distance of a good tuple is defined as:
            abs(i - j) + abs(j - k) + abs(k - i),
        where abs(x) denotes the absolute value of x.

        Returns the minimum possible distance of a good tuple.
        If no good tuples exist, returns -1.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The minimum possible distance of a good tuple, or -1 if no
            such tuple exists.

        Example:
            Input: nums = [1, 2, 1, 1, 3]
            Output: 6

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n).
        """
        elems = {}
        min_dist = float("infinity")

        def get_distance(curr_list):
            curr_dist = (
                abs(curr_list[0] - curr_list[1])
                + abs(curr_list[1] - curr_list[2])
                + abs(curr_list[2] - curr_list[0])
            )

            return curr_dist

        for i, num in enumerate(nums):
            if elems.get(num, 0) == 0:
                elems[num] = [i]
            else:
                if len(elems[num]) < 3:
                    elems[num].append(i)
                else:
                    elems[num].pop(0)
                    elems[num].append(i)

                if len(elems[num]) == 3:
                    min_dist = min(get_distance(elems[num]), min_dist)

        if min_dist == float("infinity"):
            min_dist = -1

        return min_dist
