class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        """
        Given a square on the Cartesian plane with edge length `side` and
        corners at (0, 0), (0, side), (side, 0), and (side, side), and a list of
        integer points lying on the boundary, select `k` points such that the
        minimum Manhattan distance between any two selected points is maximized.

        The Manhattan distance between points (xi, yi) and (xj, yj) is
        |xi - xj| + |yi - yj|.

        Args:
            side (int): The length of the edge of the square.
            points (List[List[int]]): 2D list where points[i] = [xi, yi] is a
                                      point on the boundary.
            k (int): Number of points to select.

        Returns:
            int: The maximum possible minimum Manhattan distance between any two
                 of the selected `k` points.

        Example:
            Input: side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4
            Output: 2

        Time Complexity: O(nlog(n) * log(Perimeter)).
        Space Complexity: O(n).
        """
        positions = []
        for x, y in points:
            if y == 0:
                d = x
            elif x == side:
                d = side + y
            elif y == side:
                d = 3 * side - x
            else:
                d = 4 * side - y
            positions.append(d)

        positions.sort()
        n = len(positions)
        perimeter = 4 * side

        def check(mid):
            for i in range(n):
                count = 1
                last_pos = positions[i]
                first_pos = positions[i]

                curr = i
                for _ in range(k - 1):
                    target = last_pos + mid

                    idx = bisect.bisect_left(positions, target, lo=curr + 1)

                    if idx < n:
                        last_pos = positions[idx]
                        curr = idx
                    else:
                        target_wrapped = target % perimeter
                        return False

                if perimeter - (last_pos - first_pos) >= mid:
                    return True
            return False

        def can_place(mid):
            for i in range(n):
                if i > 0 and positions[i] - positions[0] >= mid:
                    break

                count = 1
                curr_idx = i
                last_val = positions[i]
                for _ in range(k - 1):
                    target = last_val + mid
                    next_idx = bisect_left(positions, target)
                    if next_idx == n:
                        count = -1
                        break
                    last_val = positions[next_idx]
                    curr_idx = next_idx

                if count != -1 and (positions[i] + perimeter - last_val) >= mid:
                    return True
            return False

        from bisect import bisect_left

        low = 1
        high = perimeter // k
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if can_place(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
