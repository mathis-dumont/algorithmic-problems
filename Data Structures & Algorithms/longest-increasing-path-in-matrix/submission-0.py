class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])

        res = [[1 for _ in range(cols)] for _ in range(rows)]

        def dfs(r,c):
            if res[r][c] > 1:
                return res[r][c]
            directions = [(-1,0),(1,0),(0,-1),(0,1)]

            for dr,dc in directions:
                nr, nc = r + dr, c + dc
                if 0<=nr<rows and 0<=nc<cols and matrix[nr][nc] > matrix[r][c]:
                    res[r][c] = max(res[r][c],1 + dfs(nr,nc))

            return res[r][c]

        output = 0
        for i in range(rows):
            for j in range(cols):
                output = max(dfs(i,j), output)

        return output