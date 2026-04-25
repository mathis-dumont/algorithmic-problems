class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = prerequisites
        g = {i:[] for i in range(numCourses)}
        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED]*numCourses

        for a,b in courses:
            g[a].append(b)

        def dfs(node):
            if states[node] == VISITING: return False
            if states[node] == VISITED: return True
            states[node] = VISITING
            for neighbor in g[node]:
                if not dfs(neighbor): return False
            states[node] = VISITED
            return True
            
        for i in range(numCourses):
            if not dfs(i): 
                # if we detect a cycle 
                return False
        # no cycle detected
        return True
        
        
        