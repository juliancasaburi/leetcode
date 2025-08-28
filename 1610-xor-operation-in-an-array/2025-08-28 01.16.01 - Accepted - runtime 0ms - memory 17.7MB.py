class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xored_nums = 0
        
        for i in range(0, n):
            xored_nums = xored_nums ^ (start + 2 * i)

        return xored_nums

        