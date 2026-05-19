class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        """
        Processes a string list events and returns the final score and counter.

        The function takes a list of strings `events`, where each element
        represents a scoring event.
        Initially, score = 0 and counter = 0. The possible events are:

            - "0", "1", "2", "3", "4", "6": Add that value to the total score.
            - "W": Increase the counter by 1. No score is added.
            - "WD": Add 1 to the total score.
            - "NB": Add 1 to the total score.

        The list is processed from left to right. Processing stops if either:
            - All elements in `events` have been processed, or
            - The counter (number of wickets) reaches 10.

        Args:
            events (list[str]): The list of events to process.

        Returns:
            list[int]: A list [score, counter] where `score` is the total score
                       and `counter` is the total counter.

        Example:
            Input: ["1", "4", "W", "WD", "2"]
            Output: [8, 1]

        Time Complexity: O(n)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        events_dict = {
            "0": [0, 0],
            "1": [0, 1],
            "2": [0, 2],
            "3": [0, 3],
            "4": [0, 4],
            "6": [0, 6],
            "W": [1, 1],
            "WD": [0, 1],
            "NB": [0, 1],
        }
        res = [0, 0]

        for e in events:
            curr = events_dict.get(e, [0, 0])

            res[curr[0]] += curr[1]

            if res[1] == 10:
                break

        return res
