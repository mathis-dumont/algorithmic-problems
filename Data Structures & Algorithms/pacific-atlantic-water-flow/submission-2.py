class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return [[]]

        rows, cols = len(heights), len(heights[0])

        res = []

        def dfs(r,c,visited):
            atl = (r == rows-1) or (c == cols-1)
            pac = (r == 0) or (c == 0)

            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] <= heights[r][c] and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    atl_, pac_ = dfs(nr,nc,visited)

                    atl = atl or atl_
                    pac = pac or pac_
            return atl,pac

        for i in range(rows):
            for j in range(cols):
                atl, pac = dfs(i,j, {(i,j)})
                if pac and atl:
                    res.append([i,j])
        
        return res