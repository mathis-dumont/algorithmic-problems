class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # transposition : 
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 

        # inversion of each row
        for row in matrix:
            left, right = 0, n-1
            while left < right :
                row[right], row[left] = row[left], row[right]
                right -=1
                left +=1
