class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        """
        Calculate the maximum number of unique walls that can be destroyed
        by robots on an infinite straight line, given their positions,
        bullet distances, and the positions of walls.

        Each robot can shoot one bullet either left or right up to its
        respective distance. Bullets destroy all walls in their path
        within range, but stop immediately if they hit another robot.

        A wall and a robot may occupy the same position. In this case,
        the wall can still be destroyed by the robot at that position.
        Robots are not destroyed by bullets.

        Args:
            robots (list[int]): The positions of the robots.
            distance (list[int]): The maximum bullet distance for each robot.
            walls (list[int]): The positions of the walls.

        Returns:
            int: The maximum number of unique walls that can be destroyed.

        Example:
            Input: robots = [4], distance = [3], walls = [1,10]
            Output: 1 # The robot can destroy the wall at position 10.

        Time Complexity: O(n log n), where n is the length of the input lists.
        Space Complexity: O(n), where n is the length of the input lists.
        """
        walls.sort()
        robot_data = sorted(zip(robots, distance))
        n = len(robot_data)

        def count_walls(low, high):
            if low > high:
                return 0
            return bisect_right(walls, high) - bisect_left(walls, low)

        dp = [[0, 0] for _ in range(n)]

        for i in range(n):
            curr_pos, curr_dist = robot_data[i]

            limit_l = max(
                curr_pos - curr_dist,
                robot_data[i - 1][0] + 1 if i > 0 else float("-inf"),
            )
            walls_left = count_walls(limit_l, curr_pos)

            if i == 0:
                dp[i][0] = walls_left
            else:
                prev_pos, prev_dist = robot_data[i - 1]
                limit_prev_r = min(prev_pos + prev_dist, curr_pos - 1)

                overlap = count_walls(
                    max(limit_l, prev_pos), min(curr_pos, limit_prev_r)
                )

                dp[i][0] = max(
                    dp[i - 1][0] + walls_left, dp[i - 1][1] + walls_left - overlap
                )

            limit_r = min(
                curr_pos + curr_dist,
                robot_data[i + 1][0] - 1 if i < n - 1 else float("inf"),
            )
            walls_right = count_walls(curr_pos + 1, limit_r)

            if i == 0:
                dp[i][1] = count_walls(curr_pos, limit_r)
            else:
                prev_pos, prev_dist = robot_data[i - 1]
                limit_prev_r = min(prev_pos + prev_dist, curr_pos - 1)

                at_robot_covered = (
                    1
                    if (
                        limit_prev_r >= curr_pos and count_walls(curr_pos, curr_pos) > 0
                    )
                    else 0
                )

                walls_right_with_self = count_walls(curr_pos, limit_r)

                dp[i][1] = max(
                    dp[i - 1][0] + walls_right_with_self,
                    dp[i - 1][1] + walls_right_with_self - at_robot_covered,
                )

        return max(dp[-1])
