class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]

        def linearrob(arr):
            prev1, prev2 = 0, 0
            for x in arr:
                prev1, prev2 = max(prev2 + x,prev1), prev1 
            return prev1
        return max(linearrob(nums[1:]),linearrob(nums[:-1]))

        

