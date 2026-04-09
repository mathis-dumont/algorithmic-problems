class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        distinct = set(nums)

        longest = 0
        

        for n in distinct:
            if n-1 not in distinct:
                k = n
                current = 1
                while k+1 in distinct:
                    current +=1
                    k+=1
                longest = max(current,longest)

        return longest

        