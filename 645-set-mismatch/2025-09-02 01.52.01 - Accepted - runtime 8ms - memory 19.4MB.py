class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        dup = -1
        for num in nums:
            if num in seen:
                dup = num
            seen.add(num)

        n = len(nums)
        for i in range(1, n + 1):
            if i not in seen:
                return [dup, i]
