class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def helper(i, j, carry):
            if i < 0 and j < 0 and carry == 0:
                return ""

            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            total = bit_a + bit_b + carry
            carry = total // 2
            bit = str(total % 2)

            return helper(i - 1, j - 1, carry) + bit

        return helper(len(a) - 1, len(b) - 1, 0)
