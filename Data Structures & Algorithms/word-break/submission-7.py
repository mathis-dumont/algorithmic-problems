class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordDict = set(wordDict)
        def dp(i):
            if i == 0:
                return True
            if i not in memo:
                memo[i] = False
                for j in range(1,i+1):
                    if s[i-j:i] in wordDict and dp(i-j):
                        memo[i] = True
                        break
            return memo[i]
        
        return dp(len(s)+1)


