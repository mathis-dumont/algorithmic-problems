class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return [[]]

        rows, cols = len(heights), len(heights[0])

        atl, pac = set(), set()
        # pac = (r == 0) or (c == 0)

        def dfs(r,c,visited):
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr,nc = r + dr, c + dc
                if ( 0<=nr<rows and 0<=nc<cols and 
                (nr,nc) not in visited and 
                heights[nr][nc]>=heights[r][c] ):
                    visited.add((nr,nc))
                    dfs(nr,nc,visited)



        for i in range(rows):
            pac.add((i,0))
            dfs(i,0,pac)

            atl.add((i,cols-1))
            dfs(i,cols-1,atl)

        for j in range(cols):
            pac.add((0,j))
            dfs(0,j,pac)

            atl.add((rows-1,j))
            dfs(rows-1,j,atl)

        res = [[i,j] for i,j in atl & pac]
        return res
        
