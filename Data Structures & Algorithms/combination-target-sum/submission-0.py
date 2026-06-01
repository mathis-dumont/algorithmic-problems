class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if sum(subset)==target :
                if subset[:] not in res:
                    res.append(subset[:])
                return
            if i ==len(nums) or sum(subset)>target: 
                return 

            subset.append(nums[i])
            dfs(i)
            dfs(i+1)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res



