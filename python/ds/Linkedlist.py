class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


def print_linked_list(llist: LinkedList):
    node = llist.head
    print(f'size of linked list:{llist.length}')
    while node is not None:
        print(f'data:{node.value}')
        node = node.next


def test_linked_list():
    llist = LinkedList()
    llist.append(4)
    print_linked_list(llist)


if __name__ == '__main__':
    test_linked_list()
