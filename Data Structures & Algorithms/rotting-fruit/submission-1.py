class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        witness = 0
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while q:
            len_q = len(q)
            for _ in range(len_q):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        witness = 1
                        grid[nr][nc]=2
                        q.append((nr,nc))
            if witness ==1:
                res +=1
            witness =0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return res


