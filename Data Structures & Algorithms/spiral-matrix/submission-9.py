class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        res = []

    # n = 2 : n//2 = 1 -> i =0
    # n= 3 : n//2 = 1 -> i = 0
    # n = 4: n//2 = 2 -> i = 0,1

        for i in range((min(n,m)+1)//2):
            print("STEP1")
            for j in range(i,m-i):
                res.append(matrix[i][j])
                print(i,j)

            print("STEP2")
            if m-1-i >=0:
                for j in range(i+1,n-1-i):
                    res.append(matrix[j][m-1-i])
                    print(j,m-1-i)
                print("STEP3")

            if i != n-1-i:
                for j in range(m-1-i,i-1,-1):
                    res.append(matrix[n-1-i][j])
                    print(n-1-i,j)
            print("STEP4")
            
            if i != m-1-i and 0 <=i <m:
                for j in range(n-2-i,i,-1):
                    res.append(matrix[j][i])
                    print(j,i)
            

        return res