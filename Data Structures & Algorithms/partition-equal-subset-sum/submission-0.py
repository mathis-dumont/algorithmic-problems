class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # dp(i, goal) = True s'il existe un sous-ensemble des i premiers éléments de nums dont la somme vaut exactement goal.

        if sum(nums)%2 != 0:
            return False

        target = sum(nums) // 2

        memo = {}
        def dp(i,goal):
            if i==0:
                return goal==0
            if goal<0:
                return False
            
            if (i,goal) not in memo:
                memo[(i,goal)] = dp(i-1,goal-nums[i-1]) or dp(i-1,goal)
            return memo[(i,goal)]

        return dp(len(nums),target)
        