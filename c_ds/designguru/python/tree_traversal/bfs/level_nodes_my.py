from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None
  def __str__(self):
      return f"{self.val}"
  def __repr__(self):
      return self.__str__()

class Solution:
  def traverse(self, root):
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append([root])
    while (queue):
      current_level = []
      node_list = queue.popleft()
      print(f"node list:{str(node_list)}")
      result.append(node_list)
      for node in node_list:
        if node.left is not None:
          current_level.append(node.left)
        if node.right is not None:
          current_level.append(node.right)
      if len(current_level) > 0:
        queue.append(current_level)
    return result

def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(sol.traverse(root)))


if __name__ == "__main__":
  main()
