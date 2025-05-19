class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count_with_even_digits = 0

        for number in nums:
            digits = 0
            while number != 0:
                digits += 1
                number = number // 10

            if digits % 2 == 0:
                count_with_even_digits += 1

        return count_with_even_digits
