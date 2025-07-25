from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


class Solution:
  def traverse(self, root):
    result = deque()
    if root is None:
      return result

    queue = deque()
    queue.append(root)
    while queue:
      levelSize = len(queue)
      currentLevel = []
      for _ in range(levelSize):
        currentNode = queue.popleft()
        # add the node to the current level
        currentLevel.append(currentNode.val)
        # insert the children of current node in the queue
        if currentNode.left:
          queue.append(currentNode.left)
        if currentNode.right:
          queue.append(currentNode.right)

      result.appendleft(currentLevel)

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
