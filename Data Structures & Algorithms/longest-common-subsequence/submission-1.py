class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}
        def dp(i,j):
            if i == 0 or j == 0:
                return 0
            if (i,j) not in memo:
                if text1[i-1] == text2[j-1]:
                    memo[(i,j)] = dp(i-1,j-1) + 1
                else:
                    memo[(i,j)] = max(dp(i-1,j),dp(i,j-1))
            return memo[(i,j)]
        
        return dp(len(text1),len(text2))
