class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        memo = {}
        def dp(i,j):

            if (i,j) not in memo:
                if (i,j) == (0,0):
                    memo[(i,j)] = grid[0][0]
                elif i == 0:
                    memo[(i,j)] = grid[0][j] + dp(0,j-1)
                elif j == 0:
                    memo[(i,j)] = grid[i][j] + dp(i-1,0)
                else:
                    memo[(i,j)] =  grid[i][j] + min(dp(i-1,j),dp(i,j-1))
            return memo[(i,j)]
        return dp(rows-1,cols-1)

                

