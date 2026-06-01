class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = {i:[] for i in range(numCourses)}
        in_degrees = [0]*numCourses
        order = []

        for a,b in prerequisites:
            g[b].append(a)
            in_degrees[a]+=1

        q = collections.deque([i for i in range(numCourses) if in_degrees[i]==0])

        while q:
            curr = q.popleft()
            order.append(curr)

            for nei in g[curr]:
                in_degrees[nei] -=1
                if in_degrees[nei] == 0:
                    q.append(nei)
        
        return order if len(order)==numCourses else []
