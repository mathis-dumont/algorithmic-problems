class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()

        def bfs(i,j):
            q = collections.deque([(i,j)])
            distance = 0

            while q:
                distance +=1
                for _ in range(len(q)):
                    r, c = q.popleft()
                    directions = [(-1,0),(1,0),(0,-1),(0,1)]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]!=0 and grid[nr][nc]>distance:
                            grid[nr][nc]=distance
                            q.append((nr,nc))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    bfs(i,j)
        

                    

