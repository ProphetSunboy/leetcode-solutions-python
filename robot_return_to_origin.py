# First solution
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        Return True if the robot returns to the origin after it finishes all of
        its moves, or False otherwise.

        There is a robot starting at the position (0, 0), the origin, on a 2D
        plane. Given a sequence of its moves, judge if this robot ends up at
        (0, 0) after it completes its moves.

        You are given a string moves that represents the move sequence of the
        robot where moves[i] represents its ith move. Valid moves are
        'R' (right), 'L' (left), 'U' (up), and 'D' (down).

        Note: The way that the robot is "facing" is irrelevant. 'R' will always
        make the robot move to the right once, 'L' will always make it move
        left, etc. Also, assume that the magnitude of the robot's movement is
        the same for each move.


        :param str moves: robot movement sequence
        :returns bool returns_to_origin: does the robot returns to origin

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 96.53%
        """
        c = collections.Counter(moves)

        return c["U"] == c["D"] and c["L"] == c["R"]


# Second solution
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        Determines if a robot returns to the origin after completing a sequence
        of moves.

        The robot starts at position (0, 0) on a 2D plane. Each character in the
        string `moves` represents a movement:
            'R' - move right
            'L' - move left
            'U' - move up
            'D' - move down

        The orientation of the robot does not matter; each character corresponds
        to a unit movement in the respective direction.

        Args:
            moves (str): The move sequence for the robot.

        Returns:
            bool: True if the robot returns to the origin (0, 0), False otherwise.

        Example:
            Input: moves = "UD"
            Output: true

        Time Complexity: O(n), where n is the length of moves.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        return moves.count("L") == moves.count("R") and moves.count("U") == moves.count(
            "D"
        )
