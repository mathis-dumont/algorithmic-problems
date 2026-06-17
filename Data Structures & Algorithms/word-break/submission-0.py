class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp(i) : s[:i] can be segmented into a space-separated sequence of dictionary words
        # dp(i) = 
        memo = {}
        def dp(i):
            if i == 0:
                return True
            if i not in memo:
                stop = 0
                for j in range(i+1): 
                    if s[i-j:i] in wordDict and dp(i-j):
                        memo[i] = True
                        stop = 1
                if stop ==0:
                    memo[i] = False

            return memo[i]
        return dp(len(s)+1)
            