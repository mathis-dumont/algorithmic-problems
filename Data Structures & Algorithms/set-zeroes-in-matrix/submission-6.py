class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        n, m = len(matrix), len(matrix[0])

        visited = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0 and (i,j) not in visited:
                    visited.add((i,j))
                    for _ in range(n):
                        if matrix[_][j] != 0:
                            visited.add((_,j))
                            matrix[_][j] = 0

                    for _ in range(m):
                        if matrix[i][_] != 0:
                            visited.add((i,_))
                            matrix[i][_] = 0
                