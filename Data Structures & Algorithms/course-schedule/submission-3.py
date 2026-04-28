class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = {i:[] for i in range(numCourses)}

        for a,b in prerequisites:
            g[a].append(b)

        UNVISITED, VISITING, VISITED = 0, 1, 2

        states = [UNVISITED] * numCourses

        def dfs(node):
            if states[node] == VISITING: return False
            if states[node] == VISITED: return True

            states[node] = VISITING

            for neighbor in g[node]:
                if not dfs(neighbor): return False
            
            states[node] = VISITED
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True