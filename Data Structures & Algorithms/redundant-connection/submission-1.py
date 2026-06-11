class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [0] * (len(edges)+1)

        parent = [i for i in range(len(edges)+1)]

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        def union(a,b):
            ra, rb = find(a), find(b)

            if rank[ra]<rank[rb]:
                rb, ra = ra, rb
            parent[rb] = ra

            if rank[ra] == rank[rb]:
                rank[ra] += 1

        for a,b in edges:
            if find(a) == find(b):
                return [a,b]
            union(a,b)



