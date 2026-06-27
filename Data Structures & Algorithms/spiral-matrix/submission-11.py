class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        res = []
        while bottom >= top and left <= right:
            for c in range(left,right+1):
                print(top,c)
                res.append(matrix[top][c])
            top += 1

            for r in range(top, bottom+1):
                print(r,right)
                res.append(matrix[r][right])
            right -= 1

            if bottom >= top:
                for c in range(right,left-1,-1):
                    print(bottom,c)
                    res.append(matrix[bottom][c])
                bottom -= 1    

            if left <= right:
                for r in range(bottom,top-1,-1):
                    print(r,left)
                    res.append(matrix[r][left])
                left += 1

        return res 

            
