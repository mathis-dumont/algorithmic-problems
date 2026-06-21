class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = {}
        def dp(i):
            if i == 0:
                return 1
            if i not in memo:
                memo[i] = 1 + max([dp(j) for j in range(i) if nums[j] < nums[i]]+[0])
            return memo[i]
        return max(dp(i) for i in range(len(nums)))

        # dp[i] = length of the lgst stcly incr subseq that finish at nums[i]
        # dp[0] = 1
        # dp[i] = 1 + max([dp[j] for j in range(i) if nums[j] < nums[i]])
        # if nums[i-1] == nums[i-2]:
            # dp[i] = dp[i-1]
        # if nums[i-1] < nums[i-2]:
            # dp[i] = dp[i-2]    



