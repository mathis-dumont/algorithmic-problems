class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        if n ==0 or n ==1:
            return None
        for i in range(n):
            for j in range(i+1,n):
                add = nums[i]+nums[j]
                if add == target :
                    return [i,j]
                