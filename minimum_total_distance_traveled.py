class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        """
        Calculates the minimum total distance traveled by all robots to reach
        and be repaired at factories along the X-axis.

        There are robots and factories on the X-axis.
        Each robot's position is given in the integer list `robot`.
        Each factory is described as [position, limit] in the `factory` list,
        where `position` is the location of the factory and `limit`
        is the maximum number of robots it can repair.

        - The positions of each robot and each factory are unique.
        - Robots may start at the same position as a factory.
        - All robots start broken and move in one direction (either positive or
        negative).
        - Robots may be directed in any initial direction.
        - When a robot reaches a factory that can repair it, it is repaired and
        stops moving.
        - Robots pass by factories at their repair limit, ignoring them.
        - Robots do not collide; if they cross paths, they continue as normal.

        The goal is to minimize the total distance traveled by all robots.

        Args:
            robot (list[int]): Positions of the robots on the X-axis.
            factory (list[list[int]]): Each factory described as
                [position, limit], where 'position' is the location of the
                factory and 'limit' is the maximum number of robots it can
                repair.

        Returns:
            int: The minimum total distance traveled by all robots.

        Example:
            Input: robot = [0,4,6], factory = [[2,2],[6,2]]
            Output: 4

        Time Complexity: O(n * m), where n is a number of robots, m is a total
        factory repair slots.
        Space Complexity: O(n), due to the DP list.
        """
        robot.sort()
        factory.sort()

        factories_expanded = []
        for pos, limit in factory:
            factories_expanded.extend([pos] * limit)

        n, m = len(robot), len(factories_expanded)

        dp = [0] + [float("inf")] * n

        for f_pos in factories_expanded:
            for i in range(n, 0, -1):
                if dp[i - 1] != float("inf"):
                    dist = abs(robot[i - 1] - f_pos)
                    dp[i] = min(dp[i], dp[i - 1] + dist)

        return dp[n]
