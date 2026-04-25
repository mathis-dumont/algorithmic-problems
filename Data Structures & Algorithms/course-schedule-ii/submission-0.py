class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        UNVISITED, VISITING, VISITED = 0, 1, 2
        g = {i:[] for i in range(numCourses)}
        states = [UNVISITED]*numCourses

        for a,b in prerequisites:
            g[a].append(b)
        
        def dfs(node):
            if states[node] == VISITING: return False
            if states[node] == VISITED: return True
            states[node] = VISITING
            for neighbor in g[node]:
                if not dfs(neighbor): return False
            states[node] = VISITED
            order.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return [] 
        
        return order