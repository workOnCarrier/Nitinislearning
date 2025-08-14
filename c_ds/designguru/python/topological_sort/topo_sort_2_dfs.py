from collections import deque
from collections import defaultdict

problem_statement = '''
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled.

Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

Examples
Example 1:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: true
Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5] 
Example 2:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish before '2' can be scheduled. One possible scheduling of tasks is: [0, 1, 2] 
Example 3:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: false
Explanation: The tasks have a cyclic dependency, therefore they cannot be scheduled.
'''

class Solution:
  def isSchedulingPossible(self, task_count, prerequisites):
    if not prerequisites:
      return True
    print(f"\t\t task_count:{task_count} -- input:{prerequisites}")
    result = []
    graph = defaultdict(list)
    visited = [False] * task_count

    for parent, child in prerequisites:
      graph[child].append(parent)
    print(f"\t graph:{graph}")
    
    for task in range(task_count):
      current_path = set()
      if not visited[task]:
        if not self.topo_navigate(task, graph, visited, current_path, result):
          print(f"\t task failed:{task}")
          return False
    
    print(f" result:{result}  -- validation: {len(result) == task_count}")
    if len(result) == task_count:
      return True
    return False

  def topo_navigate(self, task, graph: defaultdict(list), visited: list, current_path: set, result: list):
    print(f"\t entering task navigagte for task:{task},\t visited:{visited},\t current_path:{current_path},\t result:{result}")
    if task in current_path:
      return False
    current_path.add(task)
    for child_task in graph[task]:
      if visited[child_task] :
        continue
      if not self.topo_navigate(child_task, graph, visited, current_path, result):
        return False
    result.append(task)
    visited[task] = True
    print(f"\t\t exiting task navigagte for task:{task},\t visited:{visited},\t current_path:{current_path},\t result:{result}")
    return True


def main():
  sol = Solution()
  print("Is scheduling possible: " +
        str(sol.isSchedulingPossible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))
  print("Is scheduling possible: " +
        str(sol.isSchedulingPossible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(sol.isSchedulingPossible(3, [[0, 1], [1, 2], [2, 0]])))


main()

