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

        visited[node] = Node(node.val)
        q = collections.deque([node])

        while q:
            node_copy = q.popleft()
            for neighbor in node_copy.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                visited[node_copy].neighbors.append(visited[neighbor])
        
        return visited[node]
