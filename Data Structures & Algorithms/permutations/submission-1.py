class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        visited = set()

        def dfs(i):
            if i == len(nums):
                res.append(perm[:])
                return

            for k in range(len(nums)):
                if k not in visited:
                    visited.add(k)
                    perm.append(nums[k])
                    dfs(i+1)
                    visited.remove(k)
                    perm.pop()
        dfs(0)
        return res

