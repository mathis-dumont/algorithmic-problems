class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_islands = 0

        rows, cols = len(grid), len(grid[0])


        def bfs(i,j):
            q = collections.deque([(i,j)])
            while q:
                r,c = q.popleft()
                grid[r][c]='0'
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr, nc = r + dr, c + dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1':
                        q.append((nr,nc))




        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    n_islands+=1
                    bfs(i,j)
        
        return n_islands