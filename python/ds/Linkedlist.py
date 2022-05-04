import io

from python.ds.graph_to_puml import start_uml, end_uml


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

def write_linked_list(llist: LinkedList):
    puml_file_name = "linked_list.puml"
    string_stream = io.StringIO()
    index = 1;
    node = llist.head
    while node is not None:
        target = "None" if node.next is None else node.next.value
        string_stream.write(f'\nRel_Access({node.value}, {target}, {index})')
        index += 1
        node = node.next
    with open(puml_file_name, 'w+') as file_writer:
        file_writer.write(start_uml)
        file_writer.write('\n')
        file_writer.write(string_stream.getvalue())
        file_writer.write('\n')
        file_writer.write(end_uml)
    string_stream.close()


def test_linked_list():
    llist = LinkedList()
    llist.append(4)
    llist.append(5)
    llist.append(6)
    llist.append(7)
    print_linked_list(llist)
    write_linked_list(llist)


if __name__ == '__main__':

    test_linked_list()
