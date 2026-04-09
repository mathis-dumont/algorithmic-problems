class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        length = len(nums)

        right_products = [1 for _ in range(length)]
        left_products = [1 for _ in range(length)]
        res = [1 for _ in range(length)]

        for i in range(1,length):
            right_products[i] = right_products[i-1] * nums[i-1]

        for j in range(length-2,-1,-1):
            left_products[j] = left_products[j+1] * nums[j+1]

        for k in range(length):
            res[k] = right_products[k] * left_products[k]
        return res 
