class Solution:
    def trafficSignal(self, timer: int) -> str:
        """
        Return the current state of a traffic signal based on the remaining
        timer.

        The signal operates as follows:
            - If timer == 0, the signal is "Green".
            - If timer == 30, the signal is "Orange".
            - If 30 < timer <= 90, the signal is "Red".
            - Otherwise, returns "Invalid".

        Args:
            timer (int): The remaining time (in seconds) on the traffic signal.

        Returns:
            str: The current state of the signal ("Green", "Orange", "Red",
            or "Invalid").

        Example:
            Input: timer = 60
            Output: "Red"

        Time Complexity: O(1).
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        if timer == 0:
            return "Green"
        elif timer == 30:
            return "Orange"
        elif 30 < timer <= 90:
            return "Red"

        return "Invalid"
