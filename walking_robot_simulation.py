class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        Simulates a robot on an infinite XY-plane given movement commands and
        obstacles.

        The robot starts at (0, 0) facing north. Commands are:
            - -2: Turn left 90 degrees.
            - -1: Turn right 90 degrees.
            - 1 <= k <= 9: Move forward k units, one unit at a time.

        If a move would take the robot into an obstacle, it stops before the
        obstacle and continues with the next command.

        The function returns the maximum squared Euclidean distance from the
        origin attained at any point in the robot's path.

        Notes:
            - Obstacles can appear at (0, 0); the robot ignores obstacles at the
              origin until it moves off.
            - North: +Y direction
            - East: +X direction
            - South: -Y direction
            - West: -X direction

        Args:
            commands (List[int]): The sequence of movement and turn commands.
            obstacles (List[List[int]]): List of obstacle coordinates.

        Returns:
            int: The maximum squared Euclidean distance from the origin.

        Example:
            Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
            Output: 65

        Time Complexity: O(n + m), where n is the number of commands and m is
                         the number of obstacles.
        Space Complexity: O(m), where m is the number of obstacles.

        LeetCode: Beats 96.52% of submissions
        """
        obstacle_set = {tuple(o) for o in obstacles}

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir = 0
        x, y = 0, 0
        max_sqr_dist = 0

        for cmd in commands:
            if cmd == -1:
                curr_dir = (curr_dir + 1) % 4
            elif cmd == -2:
                curr_dir = (curr_dir - 1) % 4
            else:
                dx, dy = directions[curr_dir]
                for _ in range(cmd):
                    if (x + dx, y + dy) in obstacle_set:
                        break
                    x += dx
                    y += dy

                max_sqr_dist = max(max_sqr_dist, x * x + y * y)

        return max_sqr_dist
