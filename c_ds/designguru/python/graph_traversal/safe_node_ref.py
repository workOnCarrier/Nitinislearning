class Solution:
    def eventualSafeNodes(self, graph):
        def dfs(node):
            if visited[node] == -1: # If node is marked as safe
                return True
            if visited[node] == 1: # If node is part of a cycle
                return False

            visited[node] = 1 # Mark the node as visiting
            for next_node in graph[node]:
                if not dfs(next_node):
                    return False # If any adjacent node is not safe

            visited[node] = -1 # Mark the node as safe
            return True

        n = len(graph)
        visited = [0] * n # 0: unvisited, 1: visiting, -1: safe
        result = []

        for i in range(n):
            if dfs(i):
                result.append(i)

        return sorted(result) # Sorting the result

if __name__ == "__main__":
    sol = Solution()
    print(sol.eventualSafeNodes([[1,2],[2,3],[2],[],[5],[6],[]]))
    print(sol.eventualSafeNodes([[1,2],[2,3],[5],[0],[],[],[4]]))
    print(sol.eventualSafeNodes([[1,2,3],[2,3],[3],[],[0,1,2]]))


