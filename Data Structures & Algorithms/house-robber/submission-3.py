class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n ==1:
            return nums[0]
        if n ==2:
            return max(nums[0],nums[1])
        memo = {}
        def dp(i):
            if i ==1:
                return nums[0]
            if i ==2:
                return max(nums[0],nums[1])
            if i not in memo:
                memo[i] = max(dp(i-1), dp(i-2) + nums[i-1])
            return memo[i]
        
        return dp(n)