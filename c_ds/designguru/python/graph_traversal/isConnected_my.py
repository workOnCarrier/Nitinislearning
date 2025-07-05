from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: [[int]], start: int, end: int) -> bool:
        graph = defaultdict(list)
        visited = set()

        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)

        def dfs(node):
            if node == end:
                return True
            visited.add(node)
            isconnected = False
            for child in graph[node]:
                if child not in visited:
                    isconnected = dfs(child)
                if isconnected:
                    break
            return isconnected
        return dfs(start)

    

# Test
sol = Solution()
print(sol.validPath(4, [[0,1],[1,2],[2,3]], 0, 3))  # true
print(sol.validPath(4, [[0,1],[2,3]], 0, 3))      # false
print(sol.validPath(5, [[0,1],[3,4]], 0, 4))      # false
print(sol.validPath(3, [[0,1],[1,2]], 0, 2))      # True

