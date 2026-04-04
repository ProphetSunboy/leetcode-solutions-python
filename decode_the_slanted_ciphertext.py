class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        """
        Decodes a string that was encoded using a slanted transposition cipher.

        A string originalText is encoded by placing its characters in a matrix
        with a given number of rows, filling cells from top-left to bottom-right
        diagonally. After placing all characters, any remaining empty cells are
        filled with spaces. The number of columns is such that the rightmost
        column is not empty.

        The encodedText is constructed by reading the filled matrix row-wise.

        Given the encoded string and the number of rows, this function recovers
        and returns the original text (with no trailing spaces).

        Args:
            encodedText (str): The encoded string.
            rows (int): The number of rows used to encode the originalText.

        Returns:
            str: The decoded originalText.

        Example:
            Input: encodedText = "ch   ie   pr", rows = 3
            Output: "cipher"

        Time Complexity: O(n), where n is the length of encodedText.
        Space Complexity: O(n).
        """
        if rows == 1:
            return encodedText.rstrip()

        n = len(encodedText)
        cols = n // rows
        step = cols + 1

        res = [encodedText[i] for start in range(cols) for i in range(start, n, step)]

        return "".join(res).rstrip()
