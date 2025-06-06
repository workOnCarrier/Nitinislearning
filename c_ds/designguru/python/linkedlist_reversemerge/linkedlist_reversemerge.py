import time
class Node:
  def __init__(self, value, next=None):
    self.val = value
    self.next = next

def print_list(head, comment):
  print(f"\n---{comment}\t")
  current = head
  while current is not None:
    print(f"{current.val}", end=", ")
    current = current.next
    time.sleep(0.10)


def reverse(head):
  prev = None
  while head is not None:
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev

# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# 1 -> 2 -> 3 
# 6 -> 5 -> 4 
# 1 -> 6 -> 2 -> 5 -> 3 -> 4
def merge(left, right):
  head = None 
  if left is None or right is None:
    return left if left is not None else right
  head = left                 # 1 -> 6 -> 2 -> 5 -> 3
  left_current = left # 1
  left_next = left.next # 2
  right_current = right # 6
  right_next = right.next # 5
  while left_current is not None and right_current is not None:
    left_current.next = right_current    # 3 -> 4
    right_current = right_next       # None
    left_current = left_current.next  # None
    if left_current is None:
      break
    left_current.next = left_next      # 5 -> 3
    left_current = left_current.next   # 3
    if left_next is None or right_next is None:
      break
    left_next = left_next.next         # None
    right_next = right_next.next       # None
  return head

def test_merge():
  left_head = Node(1)
  left_head.next = Node(2)
  left_head.next.next = Node(3)
  left_head.next.next.next = Node(7)
  right_head = Node(6)
  right_head.next = Node(5)
  right_head.next.next = Node(4)
  print_list(left_head, "left")
  print_list(right_head, "right")
  final = merge(left_head, right_head)
  print_list(final, "final")

def split(head):
  fast, slow = head, head
  count = 1
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
    count += 2
  if fast is None:
    count -= 1
  slow = head
  for _ in range( (int)((count-1)/2) ):
    slow = slow.next
  right_half = slow.next
  slow.next = None
  print(f"\t ---  element count:{count}")
  return head, right_half

def test_split():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(8)
  print_list(head, "origin")
  left, right = split(head)
  print_list(left, "left")
  print_list(right, "right")
  print(f"\n{'-'*10}")
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(8)
  head.next.next.next.next.next = Node(9)
  print_list(head, "origin")
  left, right = split(head)
  print_list(left, "left")
  print_list(right, "right")
 

class Solution:
  def reorder(self, head):
    left, right = split(head)
    inverted_right = reverse(right)
    final = merge(left, inverted_right)
    return final

def main():
  sol = Solution()
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  print_list(head, "original")
  value = sol.reorder(head)
  print_list(value, "value")

def test_reverse():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(8)

  print_list(head, "before")
  reverted = reverse(head)
  print_list(reverted, "after")



if __name__ == "__main__":
  main()
  # test_reverse()
  # test_merge()
  # test_split()
 