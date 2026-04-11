class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        
        res = []
        subset = []

        candidates.sort()

        def dfs(i,total):
            if total == target:
                res.append(subset[:])
                return 

            if total > target or i == len(candidates):
                return
            

            subset.append(candidates[i])
            dfs(i+1,total+candidates[i])

            while i+1 < len(candidates) and candidates[i]== candidates[i+1]:
                i+=1
            subset.pop()
            dfs(i+1,total)

        dfs(0,0)
        return res