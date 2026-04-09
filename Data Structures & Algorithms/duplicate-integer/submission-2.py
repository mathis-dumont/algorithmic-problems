class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:


        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)

        if n==0 or n ==1:
            return False
        
        max_val = max(nums)
        min_val = min(nums)

        if min_val < 0 :
            offset = -min_val + 1
        else:
            offset = 0

        total = max_val + offset + 1

        l = total*[False]

        for num in nums:
            if l[num+offset] == False:
                print(num)
                l[num+offset]=True
            
            else:
                return True

        return False