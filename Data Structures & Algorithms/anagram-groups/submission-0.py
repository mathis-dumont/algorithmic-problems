class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if n == 0 or n ==1:
            return [strs]
        
        def is_anagram(word1,word2):
            seen = {}
            if len(word1)!=len(word2):
                return False
            for letter in word1:
                if letter in seen:
                    seen[letter]+=1
                else:
                    seen[letter]=1
            
            for letter in word2:
                if letter not in seen :
                    return False
                seen[letter]-=1
                if seen[letter]<0:
                    return False
            return True

        output=[[strs[0]]]


        for i in range(1,n):
            c=0
            for j in range(len(output)):
                if is_anagram(strs[i],output[j][0]):
                    output[j].append(strs[i])
                    c=1
            if c==0:        
                output.append([strs[i]])
        return output

            
                

