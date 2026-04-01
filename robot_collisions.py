class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        """
        Determines the health of robots that survive a series of collisions.

        There are n 1-indexed robots, each with a position on a line, health,
        and movement direction.
        Robots are given by the lists:
            positions (List[int]): The unique initial positions of the robots.
            healths (List[int]): The initial health values of the robots.
            directions (str): The movement directions of the robots
            ('L' for left, 'R' for right).

        All robots move simultaneously at the same speed.
        When two robots occupy the same position:
            - The robot with smaller health is removed, and the survivor's
            health decreases by one.
            - If both have the same health, both are removed.
            - The surviving robot continues in its direction.

        Returns the health of the robots that survive all collisions,
        in their original order.

        Args:
            positions (List[int]): The positions of the robots.
            healths (List[int]): The health values of the robots.
            directions (str): Movement directions ('L' or 'R') for each robot.

        Returns:
            List[int]: Health values of surviving robots in the input order.
                       Returns an empty list if no robots survive.

        Example:
            Input: positions = [3,5,2,6],
                   healths = [10,10,15,12],
                   directions = "RLRL"
            Output: [14]

        Time Complexity: O(n), where n is the number of robots.
        Space Complexity: O(n), for auxiliary data structures.

        LeetCode: Beats 97.02% of submissions
        """
        n = len(positions)
        robots = sorted(range(n), key=lambda i: positions[i])
        stack = []

        for i in robots:
            if directions[i] == "R":
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    top = stack[-1]
                    if healths[top] < healths[i]:
                        healths[top] = 0
                        healths[i] -= 1
                        stack.pop()
                    elif healths[top] > healths[i]:
                        healths[i] = 0
                        healths[top] -= 1
                    else:
                        healths[i] = 0
                        healths[top] = 0
                        stack.pop()

        return [h for h in healths if h > 0]
