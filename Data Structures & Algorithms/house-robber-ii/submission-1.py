class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])

        case1 = [nums[i] for i in range(1,n)]
        case2 = [nums[i] for i in range(n-1)]
        
        def dp(i,l,memo):
            if i==1:
                return l[0]
            if i==2:
                return max(l[0],l[1])
            if i not in memo:
                memo[i] = max(dp(i-2,l,memo)+l[i-1], dp(i-1,l,memo))
            return memo[i]
        
        return max(dp(n-1,case1,{}),dp(n-1,case2,{}))

        

