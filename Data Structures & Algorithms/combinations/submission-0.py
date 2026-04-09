class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        nums = [_ for _ in range(1,n+1)]
        
        res = []
        subset = []
        def dfs(i):
            if len(subset) == k:
                res.append(subset[:])
                return 
            if i == len(nums):
                return 

            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
        