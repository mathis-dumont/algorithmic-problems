class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # state a : fewest nb of coins to make a

        # transition a :
        # dp(a) = for coin in coins:
                # min(1+dp(a-coin))

        # base: dp(0) = 0 
        # if i < 0:
            # return float("-inf")

        memo = {}
        def dp(a):
            if a == 0:
                return 0
            if a < 0:
                return float('inf')

            if a not in memo:
                res = float('inf')

                for coin in coins:
                    res = min(res, 1 + dp(a-coin))
                memo[a] = res
            
            return memo[a]
        
        return dp(amount) if dp(amount) != float('inf') else -1


        

            
