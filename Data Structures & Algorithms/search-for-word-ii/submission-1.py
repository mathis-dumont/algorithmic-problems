class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        for word in words:
            if self.exist(board,word):
                res.append(word)
        return res



    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        # Early exit: check character frequency
        board_count = Counter(c for row in board for c in row)
        word_count = Counter(word)
        if any(word_count[c] > board_count[c] for c in word_count):
            return False
        
        # Optimize: start from the rarer end of the word
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]
        
        word_len = len(word)
        
        def dfs(i: int, r: int, c: int) -> bool:
            if i == word_len:
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False
            
            board[r][c] = '#'
            found = (
                dfs(i + 1, r - 1, c) or
                dfs(i + 1, r + 1, c) or
                dfs(i + 1, r, c - 1) or
                dfs(i + 1, r, c + 1)
            )
            board[r][c] = word[i]  # restore without tmp variable
            return found
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(0, r, c):
                    return True
        return False