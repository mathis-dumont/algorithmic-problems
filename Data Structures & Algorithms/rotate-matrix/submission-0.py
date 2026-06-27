class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 0,0 -> 0,2
        # 1,0 -> 0,1
        # 2,0 -> 0,0
        # 0,1 -> 1,2
        # 1,1 -> 1,1
        # 2,1 -> 1,0
        # 0,2 -> 2,2
        # 1,2 -> 2,1
        # 2,2 -> 2,0
        n = len(matrix)
        matrix2 = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                matrix2[i][j] = matrix[n-1-j][i]

        matrix[:] = matrix2.copy()

        
        