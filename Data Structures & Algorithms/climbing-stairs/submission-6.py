class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1]=1
        memo[2]=2
        if n==1 or n==2:
            return memo[n]
        for i in range(3,n+1):
            memo[i] = memo[i-1]+memo[i-2]
        return memo[n]

