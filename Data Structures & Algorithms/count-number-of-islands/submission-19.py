class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = set()
        def bfs(node):
            visited.add(node)
            r,c = node
            queue = deque([node])
            while queue:
                for _ in range(len(queue)):
                    r,c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc]=='1':
                            visited.add((nr,nc))
                            queue.append((nr,nc))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs((i,j))
                    count +=1
        
        return count
                    