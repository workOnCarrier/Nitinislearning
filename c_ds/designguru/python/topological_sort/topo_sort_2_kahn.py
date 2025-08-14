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
  def isSchedulingPossible(self, tasks, prerequisites):
    print(f"\t\t -- input:{prerequisites}")
    result = []
    to_process = deque()
    in_degree_map = { i:0 for i in range(tasks)}
    graph = defaultdict(list)

    for parent, child in prerequisites:
      graph[parent].append(child)
      in_degree_map[child] += 1
    print(f"\t graph:{graph},\t in_degree_map:{in_degree_map}")

    for task in range(tasks):
      if in_degree_map[task] == 0:
        to_process.append(task)
    
    while to_process:
      print(f"\t to_process:{to_process}")
      task = to_process.popleft()
      result.append(task)
      for child in graph[task]:
        in_degree_map[child] -= 1
        if in_degree_map[child] == 0:
          to_process.append(child)

    print(f"\t result:{result} ---- {tasks} \t can be done:{len(result) == tasks}")
    if len(result) != tasks:
      return False

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
