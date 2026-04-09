class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        l, r = 0, n-1

        while l<r:
            amount = min(heights[l],heights[r])*(r-l)
            res = max(res,amount)

            if heights[l] > heights[r]:
                r-=1
            elif heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return res
            