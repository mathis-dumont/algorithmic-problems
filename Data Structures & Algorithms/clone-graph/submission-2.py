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
    
        # [[2],[1,3],[2]] : example

        # hashmap, keys : original nodes, values : deep copy nodes
        visited = {}
        visited[node] = Node(node.val)

        def dfs():
            stack = [node]
            while stack:
                n = stack.pop()
                for neighbor in n.neighbors:
                    if not neighbor in visited:
                        visited[neighbor] = Node(neighbor.val)
                        stack.append(neighbor)

                    # Update the hashmap, by adding 
                    # the neighbors to the deepcopy
                    visited[n].neighbors.append(visited[neighbor]) 

        
        dfs()
        return visited[node]

 