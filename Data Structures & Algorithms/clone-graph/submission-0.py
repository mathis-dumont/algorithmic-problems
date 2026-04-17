"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}
        visited[node] = Node(node.val, [])
        frontier = collections.deque([node])

        while frontier:
            curr = frontier.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    frontier.append(neighbor)
                    visited[neighbor] = Node(neighbor.val, [])
                visited[curr].neighbors.append(visited[neighbor]) 
            
        return visited[node]
