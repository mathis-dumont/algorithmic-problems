class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # state a : fewest nb of coins to make a

        # transition a :
        # dp(a) = for coin in coins:
                # min(dp(a-coin))

        # base: dp(0) = 0 
        # if i < 0:
            # return float("-inf")

        memo = {}
        def dp(i):
            if i < 0:
                return float('inf')

            if i ==0:
                return 0

            res = float('inf')

            if i not in memo:
                
                for coin in coins:
                    res = min(res,1 + dp(i-coin))
                memo[i] = res
            return memo[i]

        r = dp(amount)
        return -1 if r == float('inf') else r
            
