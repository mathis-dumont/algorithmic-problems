class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dp(i,j):
            if i == 0:
                return j
            if j == 0:
                return i
            if (i,j) not in memo:
                if word1[i-1] == word2[j-1]:   
                    memo[(i,j)] = dp(i-1,j-1)
                else:
                    tmp = min(dp(i,j-1),dp(i-1,j))
                    memo[(i,j)] = min(dp(i-1,j-1),tmp) + 1
            return memo[(i,j)]
        return dp(len(word1),len(word2))