class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n ==1:
            return nums[0]
        if n ==2:
            return max(nums[0],nums[1])
        memo = {}
        memo[1] = nums[0]
        memo[2] = max(nums[0],nums[1])

        for i in range(3,n+1):
            memo[i] = max(memo[i-1], memo[i-2] + nums[i-1])

        return memo[n]