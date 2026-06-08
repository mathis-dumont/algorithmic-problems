class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n ==1:
            return nums[0]
        if n ==2:
            return max(nums[0],nums[1])
        cache = []
        cache.append(nums[0])
        cache.append(max(nums[0],nums[1]))

        for i in range(3,n+1):
            cache.append(max(cache[-1], cache[-2] + nums[i-1]))

        return cache[-1]