class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl, pac = set(), set()

        rows, cols = len(heights), len(heights[0])
        def dfs(r,c,ocean):

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in ocean and heights[nr][nc] >= heights[r][c]:
                    ocean.add((nr,nc))
                    dfs(nr,nc,ocean)

            return

        for i in range(rows):
            atl.add((i,cols-1))
            dfs(i,cols-1,atl)

            pac.add((i,0))
            dfs(i,0,pac)

        for j in range(cols):
            atl.add((rows-1,j))
            dfs(rows-1,j,atl)

            pac.add((0,j))
            dfs(0,j,pac)


        

        return [[i,j] for i,j in pac & atl]