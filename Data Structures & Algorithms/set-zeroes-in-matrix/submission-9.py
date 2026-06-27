class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        n, m = len(matrix), len(matrix[0])

        first_row_zeros, first_col_zeros = False, False

        if any(matrix[0][j] == 0 for j in range(m)):
            first_row_zeros = True

        if any(matrix[i][0] == 0 for i in range(n)):
            first_col_zeros = True

        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_zeros == True:
            for j in range(m):
                matrix[0][j] = 0

        if first_col_zeros == True:
            for i in range(n):
                matrix[i][0] = 0
        
            