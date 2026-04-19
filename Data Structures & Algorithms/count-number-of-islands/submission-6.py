class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        n_islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def bfs(i,j):
            q = collections.deque([(i,j)])
            while q:
                r,c = q.popleft()
                if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or grid[r][c] == '0':
                    continue
                    
                visited[r][c] = True
                q.append((r-1,c))
                q.append((r+1,c))
                q.append((r,c+1))
                q.append((r,c-1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    n_islands += 1
                    bfs(i,j)
        return n_islands