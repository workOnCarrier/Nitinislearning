

from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: [[int]], start: int, end: int) -> bool:
        graph = defaultdict(list)
        
        # Create graph from edges
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # Undirected graph
        
        visited = set()

        def dfs(node):
            if node == end:  # Found the path
                return True
            visited.add(node)
            
            # Traverse neighbors
            for neighbor in graph[node]:
                if neighbor not in visited and dfs(neighbor):
                    return True
            return False  # Path not found

        return dfs(start)

# Test
sol = Solution()
print(sol.validPath(4, [[0,1],[1,2],[2,3]], 0, 3))  # true
print(sol.validPath(4, [[0,1],[2,3]], 0, 3))      # false
print(sol.validPath(5, [[0,1],[3,4]], 0, 4))      # false

