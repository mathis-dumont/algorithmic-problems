class Solution:
    def rob(self, nums: List[int]) -> int:
        def linrob(arr):
            memo = {}

            n = len(arr)

            def dp(i):
                if i ==1: return arr[0]
                if i ==2: return max(arr[0],arr[1])

                if i not in memo:
                    memo[i] = max(dp(i-1), dp(i-2) + arr[i-1])
                return memo[i]

            return dp(n)

        if len(nums) == 1:
            return nums[0]

        return max(linrob(nums[1:]), linrob(nums[:-1])) 