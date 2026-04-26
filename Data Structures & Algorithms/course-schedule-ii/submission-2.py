class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahn's Algorithm

        g = {i:[] for i in range(numCourses)}
        in_degree = [0] * numCourses
        
        # output : 
        order = [] 

        for a,b in prerequisites:
            in_degree[a] += 1
            g[b].append(a)

        q = collections.deque([i for i in range(numCourses) if in_degree[i] == 0])

        while q:
            course = q.popleft()
            order.append(course)
            for neighbor in g[course]:
                in_degree[neighbor] -=1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        
        return order if len(order) == numCourses else []