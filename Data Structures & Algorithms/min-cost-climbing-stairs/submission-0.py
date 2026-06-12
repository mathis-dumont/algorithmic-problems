class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def dp(i):
            if i == 1:
                return cost[0]
            if i ==2:
                return cost[1]

            if i not in memo:
                memo[i] = cost[i-1] + min(dp(i-1),dp(i-2))

            return memo[i]

        return min(dp(n-1),dp(n))