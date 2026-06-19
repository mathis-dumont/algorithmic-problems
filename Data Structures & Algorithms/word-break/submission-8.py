class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        res = (len(s)+1) * [False]
        
        res[0] = True

        for i in range(1,len(s)+1):
            for j in range(1,i+1):
                    if s[i-j:i] in wordDict and res[i-j]:
                        res[i] = True
                        break

        return res[-1]


