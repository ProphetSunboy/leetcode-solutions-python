class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        """
        Given a list of tasks where tasks[i] = [actual_i, minimum_i]:
            - actual_i: The actual amount of energy required to finish the i-th
                        task.
            - minimum_i: The minimum amount of energy required to begin the i-th
                         task.

        For example, if a task is [10, 12] and your current energy is 11, you
        cannot start this task.
        If your current energy is 13, you can finish it, and your energy will be
        3 afterwards.

        Tasks may be completed in any order.

        Args:
            tasks (List[List[int]]): A list of tasks, where each task is
                represented as [actual, minimum].

        Returns:
            int: The minimum initial amount of energy required to finish all
                 tasks.

        Example:
            Input: tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
            Output: 32

        Time Complexity: O(n log n), due to sorting the task list.
        Space Complexity: O(1).
        """
        initial = 0
        curr_spent = 0
        tasks.sort(key=lambda item: item[1] - item[0], reverse=True)

        for actual, minimum in tasks:
            if minimum > initial - curr_spent:
                initial += minimum - (initial - curr_spent)
            curr_spent += actual

        return initial
