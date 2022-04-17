class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add_item(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            if value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def in_order_visit(self, fun: callable):
        def _in_order_visit(current: Node, func: callable):
            if current.left is not None:
                _in_order_visit(current.left, func)
            fun(current.value)
            if current.right is not None:
                _in_order_visit(current.right, func)

        if self.root == None:
            return
        _in_order_visit(self.root, fun)

    def contains(self, value):
        class ContainedSTate:
            def __init__(self):
                self.contained = False
                self.value = value

            def __call__(self, test_value):
                if self.value == test_value:
                    self.contained = True

        if self.root is None:
            return False
        checker = ContainedSTate()
        self.in_order_visit(checker)
        return checker.contained

    def breadth_first_traversal(self):
        curr_node = self.root
        queue = []
        result = []
        queue.append(curr_node)
        while len(queue) > 0:
            curr_node = queue.pop(0)
            result.append(curr_node.value)
            if curr_node.left is not None:
                queue.append(curr_node.left)
            if curr_node.right is not None:
                queue.append(curr_node.right)
        return result



def test_tree():
    bt = Tree()
    bt.add_item(2)
    bt.add_item(1)
    bt.add_item(3)

    bt.in_order_visit(lambda b: print(b))
    check_value = 4
    print(f'Tree {"contains" if bt.contains(check_value) else "does not contain"} {check_value} ')


if __name__ == '__main__':
    test_tree()
