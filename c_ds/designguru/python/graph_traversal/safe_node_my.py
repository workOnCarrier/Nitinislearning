class Solution:
    # graph == adjacency list
    def eventualSafeNodes(self, graph):
        result = []
        status = [0]* len(graph)
        def dfs(node):
          if status[node] != 0:
            return status[node] == 1
          status[node] = -1
          for child in graph[node]:
            if child == node:
              status[node] = -1
              return False
            child_status = dfs(child)
            if not child_status:
              break;
          else:
            status[node] = 1
            result.append(node)
            return True
          return False
        for n in range(len(graph)):
          dfs(n)
        return sorted(result) # Sorting the result


if __name__ == "__main__":
    sol = Solution()
    print(sol.eventualSafeNodes([[1,2],[2,3],[2],[],[5],[6],[]]))
    print(sol.eventualSafeNodes([[1,2],[2,3],[5],[0],[],[],[4]]))
    print(sol.eventualSafeNodes([[1,2,3],[2,3],[3],[],[0,1,2]]))


