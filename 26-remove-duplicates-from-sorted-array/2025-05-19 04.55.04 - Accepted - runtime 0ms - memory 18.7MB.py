class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        k = 0

        for number in nums:
            if number != prev:
                nums[k] = number
                k += 1
                prev = number

        return k
