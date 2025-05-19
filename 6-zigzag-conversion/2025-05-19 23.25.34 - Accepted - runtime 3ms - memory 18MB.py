class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Handle edge cases
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        currentRow = 0
        increasing = False

        for char in s:
            rows[currentRow] += char

            if currentRow == (numRows - 1) or currentRow == 0:
                increasing = not increasing

            if increasing:
                currentRow += 1
            else:
                currentRow -= 1

        return "".join(rows)
