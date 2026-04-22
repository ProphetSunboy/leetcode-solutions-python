class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        """
        Given two lists of strings, queries and dictionary, where all words
        consist of lowercase English letters and have the same length.

        In one edit, you can change any single letter in a word from queries to
        any other letter. Find all words from queries that, after at most two
        edits, are equal to some word in dictionary.

        Returns a list of all such words from queries, in the same order as they
        appear in queries.

        Args:
            queries (List[str]): List of query words.
            dictionary (List[str]): List of dictionary words.

        Returns:
            List[str]: Words from queries that can be changed to a dictionary
                word with at most two edits.

        Example:
            Input:
                queries = ["word","note","ants","wood"],
                dictionary = ["wood","joke","moat"]
            Output: ["word","note","wood"]

        Time Complexity: O(m * n * k), where m = len(queries),
            n = len(dictionary), and k = length of each word.
        Space Complexity: O(m), where m is the number of valid query words
            returned.
        """
        res = []

        for q in queries:
            for w in dictionary:
                diff = 0
                for q_ch, w_ch in zip(q, w):
                    if q_ch != w_ch:
                        diff += 1

                if diff <= 2:
                    res.append(q)
                    break

        return res
