class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        n=len(nums)
        output = []

        for integer in nums:
            if integer not in count:
                count[integer]=1
            else:
                count[integer]+=1
        print(count)
        for i in range(k):
            c=0
            k2=int()
            for key,value in count.items():

                if c-value <0:
                    c = value
                    k2=key

            output.append(k2)
            count[k2]=0

        return output


        
        