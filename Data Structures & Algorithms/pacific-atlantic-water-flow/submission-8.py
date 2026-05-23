class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl, pac = set(), set()

        if not heights:
            return [[]]

        rows, cols = len(heights), len(heights[0])

        def dfs(r,c,ocean, prev):
            if (r,c) in ocean:
                return
            if 0<=r<rows and 0<=c<cols and heights[r][c] >= prev:
                ocean.add((r,c))
            else:
                return
            dfs(r-1,c,ocean,heights[r][c])
            dfs(r+1,c,ocean,heights[r][c])
            dfs(r,c-1,ocean,heights[r][c])
            dfs(r,c+1,ocean,heights[r][c])
            return

        for i in range(rows):
            dfs(i,cols-1,atl,0)

            dfs(i,0,pac,0)

        for j in range(cols):
            dfs(rows-1,j,atl,0)
            dfs(0,j,pac,0)



        
        return [[i,j] for i,j in atl & pac]



