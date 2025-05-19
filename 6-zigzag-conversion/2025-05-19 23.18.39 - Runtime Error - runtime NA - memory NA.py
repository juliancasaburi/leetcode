class Solution:
    def convert(self, s: str, numRows: int) -> str:
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
