class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        if t =="":
            return ""

        freq_t = {}
        freq_s={}

        for letter in t:
            freq_t[letter]= freq_t.get(letter,0)+1

        def countains_dic2(dic1,dic2):
            for letter,count_needed in dic2.items():
                if letter not in dic1:
                    return False
                if dic1[letter] < count_needed:
                    return False
            return True

        res = [0,0]     
        len_res = float('inf')
        l,r = 0,0
        while r < n :
            char = s[r]
            freq_s[char] = freq_s.get(char,0) + 1
            while countains_dic2(freq_s,freq_t):
                if r-l+1 < len_res:
                    len_res= r-l+1
                    res=[l,r]
                freq_s[s[l]] -=1
                l+=1
            r+=1

        if len_res == float('inf'):
            return ""
        else:
            l,r = res
            return s[l:r+1]



