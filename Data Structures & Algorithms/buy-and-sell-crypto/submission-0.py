class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        n = len(prices)
        res = 0
        l = 0
        for r in range(1,n):
            if prices[r]-prices[l]>=0:
                res = max(res, prices[r]-prices[l])
            else:
                l = r
        return res


