class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        solution = []
        partial = []
        nums.sort()

        def backtrack(start):
            solution.append(partial[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                partial.append(nums[i])
                backtrack(i + 1)
                partial.pop()

        backtrack(0)
        return solution
