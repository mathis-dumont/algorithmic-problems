class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahn's Algorithm (topological sort)

        in_degree = [0] * numCourses
        g = {i:[] for i in range(numCourses)}
        order= []

        for a,b in prerequisites:
            g[b].append(a)
            in_degree[a] +=1

        q = collections.deque([i for i in range(numCourses) if in_degree[i] == 0])

        while q:
            c = q.popleft()
            order.append(c)

            for neighbor in g[c]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        if len(order) == numCourses:
            return order
        else:
            return []