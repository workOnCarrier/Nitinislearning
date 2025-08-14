from collections import deque
from collections import defaultdict

problem = '''
Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.
Given a directed graph, find the topological ordering of its vertices. If the graph is cyclic, return an empty array.
'''
class Solution:

  def sort(self, vertices_count, edges):
    result = []

    graph = defaultdict(list)
    for from_node, to_node in edges:
      graph[from_node].append(to_node)
    
    visited = [False]* vertices_count
    stack = []
    
    for vertex in range(vertices_count):
      current_path = [False]* vertices_count
      if visited[vertex] is False:
        if self.topo_sort(graph, vertex, visited, stack, current_path ):
          return []
    result = stack[::-1]
    return result

  def topo_sort(self, graph: defaultdict(list), vertex: int, visited: list, stack: list, current_path: list):
    visited[vertex] = True
    current_path[vertex] = True
    for child in graph[vertex]:
      if not visited[child] :
        if self.topo_sort(graph, child, visited, stack, current_path):
          return True
      elif current_path[child]:
        return True
    stack.append(vertex)


def main():
  sol = Solution()
  print("Topological sort: " +
        str(sol.sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], \
              [3, 0], [3, 1], [3, 2], [4, 1]])))
  print("Topological sort: " +
        str(sol.sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(sol.sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))

main()
