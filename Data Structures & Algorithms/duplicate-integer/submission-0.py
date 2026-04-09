class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)

        if n ==0 or  n ==1:
            return False

        m=max(nums)
        o = min(nums)


        if o<=0:
            o = -o

        if n>=m and n>=o:
            l = [0.5]*(n+1)
        elif m>=o:
            l = [0.5]*(m+1)
        else:
            l=[0.5]*(o+1)
        print(l)
        for elt in nums:
            if l[elt]==0.5:
                l[elt]=1
            else:
                return True
        return False
