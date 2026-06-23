class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp(i,a) = nb of ways to make amount a with the i first numbers of nums

        # dp(i,a) = dp(i-1,a-nums[i]) + dp(i-1,a+nums[i])
        memo = {}
        def dp(i,goal):
            if i == 0:
                if nums[0] == 0 and goal == 0:
                    return 2
                elif nums[0] == -goal or nums[0] == goal:
                    return 1
                else:
                    return 0
            
            if (i,goal) not in memo:
                memo[(i,goal)] = dp(i-1,goal-nums[i]) + dp(i-1,goal+nums[i])

            return memo[(i,goal)]
        
        return dp(len(nums)-1,target)
