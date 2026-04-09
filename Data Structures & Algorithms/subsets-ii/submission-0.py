class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        subset = []
        nums.sort()
        def backtrack(i):
            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            backtrack(i+1)

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            subset.pop()
            backtrack(i+1)
        
        backtrack(0)
        return res