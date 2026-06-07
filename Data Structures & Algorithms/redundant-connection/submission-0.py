class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [0] * (len(edges) + 1)

        parent = [i for i in range(len(edges) + 1)]

        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return x

        def union(x,y):
            root_x, root_y = find(x), find(y)

            if root_x == root_y:
                return False

            if rank[x] < rank[y]:
                root_x, root_y = root_y, root_x
            
            parent[root_y] = root_x

            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1
            
            return True
        
        for a,b in edges:
            if not union(a,b):
                return [a,b]
