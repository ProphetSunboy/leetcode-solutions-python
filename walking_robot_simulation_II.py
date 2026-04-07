class Robot:
    """
    A width x height grid exists on the XY-plane with the bottom-left cell at
    (0, 0) and the top-right cell at (width - 1, height - 1).
    The grid is aligned to the four cardinal directions: "North", "East",
    "South", and "West".
    The robot starts at (0, 0) facing "East".

    The robot can be instructed to move a specific number of steps.
    On each step:
        - Attempts to move forward one cell in its current facing direction.
        - If the next cell is out of bounds, turns 90 degrees counterclockwise
          and retries the move.

    When all requested steps have been completed, the robot waits for new
    instructions.

    Methods
    -------
    __init__(width, height):
        Initializes the width x height grid and places the robot at (0, 0)
        facing "East".

    step(num):
        Moves the robot forward by num steps.

    getPos():
        Returns the current position of the robot as a list [x, y].

    getDir():
        Returns the current facing direction of the robot: one of
        "North", "East", "South", or "West".

    LeetCode: Beats 92.31% of submissions
    """

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.perimeter = 2 * (width + height - 4) + 4
        self.pos = 0
        self.is_moved = False

    def step(self, num: int) -> None:
        self.is_moved = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> list[int]:
        p = self.pos
        if p < self.w:
            return [p, 0]
        p -= self.w - 1
        if p < self.h:
            return [self.w - 1, p]
        p -= self.h - 1
        if p < self.w:
            return [self.w - 1 - p, self.h - 1]
        p -= self.w - 1
        return [0, self.h - 1 - p]

    def getDir(self) -> str:
        if self.pos == 0 and self.is_moved:
            return "South"

        p = self.pos
        if 0 < p < self.w:
            return "East"
        p -= self.w - 1
        if 0 < p < self.h:
            return "North"
        p -= self.h - 1
        if 0 < p < self.w:
            return "West"
        return "South" if self.is_moved else "East"
