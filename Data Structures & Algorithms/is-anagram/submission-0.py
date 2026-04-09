class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if set(s)!=set(t):
            return False
        
        dic_s = {i:0 for i in set(s)}
        dic_t = {i:0 for i in set(t)}
        

        for letter in s:
            dic_s[letter]+=1

        for letter in t:
            dic_t[letter]+=1

        for letter in s:
            if dic_s[letter]!=dic_t[letter]:
                return False
        return True

