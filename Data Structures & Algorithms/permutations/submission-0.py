class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset=[]
        n = len(nums)
        def dfs(i):
            if i == len(nums):
                res.append(subset[:])
                return 

            for k in range(0,n):
                if nums[k] not in subset:
                    subset.append(nums[k])
                    dfs(i+1)
                    subset.pop()
        
        dfs(0)
        return res