
class Node:
  def __init__(self, value, next=None):
    self.val = value
    self.next = next

class Solution:
  def reverse(self, head, p, q):
    if p == q:
      return head
    previous, current, last = None, head, head
    last = head
    orig_prev = None
    last_next = None
    for _ in range(1, p):
      orig_prev = current
      current = current.next
    for _ in range(1, q):
      last = last.next
      if last is None:
        break
    if last is not None:
      last_next = last.next  # can be None
    #    orig_prev    current/new_last                  last          last_next
    #     v           v                                  v             v
    # .. [] --------> [] -------> [] ------> [] ------> [] -----------> [] -------->[] ...
    new_last = current
    while current is not last:
      local = current
      current = current.next
      local.next = previous
      previous = local
    current.next = previous
    #    orig_prev    new_last                         last/current   last_next
    #     v           v                                  v             v
    # .. [] --------> [] <------- [] <------ [] <------ []            [] -------->[] ...
    if orig_prev is None:
      head = current
    else:
      orig_prev.next = current
    new_last.next = last_next
    
    return head

def print_list(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next
    print()

def main():
    sol = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    print_list(head)
    result = sol.reverse(head, 1, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    print_list(result)

if __name__ == "__main__":
    main()
