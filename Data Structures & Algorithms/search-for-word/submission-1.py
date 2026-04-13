class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(i,r,c):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False

            # backtracking
            tmp = board[r][c]
            board[r][c] = '#'

            vals = dfs(i+1,r-1,c) or dfs(i+1,r+1,c) or dfs(i+1,r,c-1) or dfs(i+1,r,c+1)
            board[r][c] = tmp
            return vals

        for i in range(rows):
            for j in range(cols):
                if dfs(0,i,j):
                    return True
        return False