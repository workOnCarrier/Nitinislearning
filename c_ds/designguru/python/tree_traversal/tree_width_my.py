from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Method to find the maximum width of the binary tree
    def widthOfBinaryTree(self, root):
        if root is None:
            return 0
        max_width = 0
        to_process = deque()
        to_process.append([(root, 1)])
        def navigate(to_process):
            nonlocal max_width
            while to_process:
                curr_level_list = []
                node_index_list = to_process.popleft()
                print(node_index_list)
                first_index = node_index_list[0][1]
                last_index = node_index_list[-1][1]
                max_width = max(max_width, last_index - first_index + 1 )
                for node, level in node_index_list:
                    if node.left:
                        curr_level_list.append((node.left, level*2))
                    if node.right:
                        curr_level_list.append((node.right, level*2 +1))
                if curr_level_list:
                    to_process.append(curr_level_list)
        navigate(to_process)
        return max_width;

if __name__ == "__main__":
    sol = Solution()

    # Create the first example tree
    example1 = TreeNode(1)
    example1.left = TreeNode(2)
    example1.right = TreeNode(3)
    example1.left.left = TreeNode(4)
    example1.right.right = TreeNode(5)

    # Create the second example tree
    example2 = TreeNode(1)
    example2.left = TreeNode(2)
    example2.right = TreeNode(3)
    example2.left.left = TreeNode(4)
    example2.left.left.right = TreeNode(7)
    example2.right.left = TreeNode(5)
    example2.right.right = TreeNode(6)

    # Create the third example tree
    example3 = TreeNode(1)
    example3.left = TreeNode(2)
    example3.left.left = TreeNode(3)
    example3.left.right = TreeNode(4)
    example3.left.right.left = TreeNode(5)

    # Test the widthOfBinaryTree method with the example trees
    print(sol.widthOfBinaryTree(example1))  # Output: 4
    print(sol.widthOfBinaryTree(example2))  # Output: 4
    print(sol.widthOfBinaryTree(example3))  # Output: 2

