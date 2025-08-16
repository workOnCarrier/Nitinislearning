from collections import deque

class Solution:
  def __init__(self):
    self.orders = []

  # this is a backtracking / permutatinal + topological solution
  def topo(self, path, seen):
    
    print(f"\t seen:{seen}, \t path:{path}")
    # base case
    if len(path) == len(self.graph):
      self.orders.append(path[:])
      return

    # instead of using queue to procee the next 0 node we recurse and loop to find the 0 node
    for node in self.graph:
      if self.indegree[node] == 0 and not seen.get(node):

        seen[node] = True
        path.append(node)

        for nex_node in self.graph[node]:
          self.indegree[nex_node] -= 1

        self.topo(path, seen)

        # undo the change as the values gets used when one path completes 
        for nex_node in self.graph[node]:
            self.indegree[nex_node] += 1

        del seen[node]
        path.pop()
        

  def printOrders(self, tasks, prerequisites):
    self.orders = []
    # edge cases 
    if tasks == 0:
      return self.orders
    elif tasks == 1:
      self.orders.append([0])
      return self.orders

    # build graph and indegree
    self.graph = {}
    self.indegree = {}

    for i in range(tasks):
      self.graph[i] = []
      self.indegree[i] = 0

    for before, after in prerequisites:
      self.graph[before].append(after)
      self.indegree[after] += 1

    self.topo([], {})

    return self.orders

def main():
  sol = Solution()
  print("Task Orders: ")
  result1 = sol.printOrders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])
  for order in result1:
    print(order)

  print("Task Orders: ")
  result2 = sol.printOrders(3, [[0, 1], [1, 2]])
  for order in result2:
    print(order)

  print("Task Orders: ")
  result3 = sol.printOrders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
  for order in result3:
    print(order)

if __name__ == "__main__":
  main()
