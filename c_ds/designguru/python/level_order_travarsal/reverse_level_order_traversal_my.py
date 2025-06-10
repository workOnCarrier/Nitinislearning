from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

class Solution:
  def traverse(self, root):
    result = deque()
    if root is None:
      return []

    crop = deque()
    crop.append(root)
    while crop:
      current_list = []
      length = len(crop)
      for _ in range(length):
        cur_node = crop.popleft()
        current_list.append(cur_node.val)
        if cur_node.left:
          crop.append(cur_node.left)
        if cur_node.right:
          crop.append(cur_node.right)
      result.appendleft(current_list)
    result = [list(sublist) for sublist in result]
    return result

def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(sol.traverse(root)))


main()
