class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] != '.' and board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        seen = {(i,j): set() for i in range(3) for j in range(3)}
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in seen[(i//3,j//3)]:
                    return False
                seen[(i//3,j//3)].add(board[i][j])
        
        return True
                


            

                

        