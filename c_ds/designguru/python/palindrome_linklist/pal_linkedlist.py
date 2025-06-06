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



class Solution:
  def isPalindrome(self, head):
    # TODO: Write your code here
    # find the middle -- lower end biased
    if head is None or head.next is None:
      return True
    slow, fast = head, head
    print_list(head, "before changes")
    while (fast is not None and fast.next is not None):
      slow = slow.next
      fast = fast.next.next
      print(f"fast:{fast.val if fast is not None else None}")
    
    # reverse the linked list from the middle onwards
    old_slow = slow
    mid = reverse(slow)
    to_restore = mid
    print_list(head, "existing")
    print_list(mid, "reversed")
    current = head
    # compare head with the middle onwards till the end of the list
    while (mid is not None and current is not None):
      if mid.val == current.val:
        mid = mid.next
        current = current.next
      else:
        break

    palstatus = False
    if mid is None or current is None:
      palstatus = True

    # restore the linklist to old setup
    mid = reverse(to_restore)
    print_list(mid, "again reversed")
    # old_slow.next = mid
    print_list(head, "restored")
    return palstatus

def main():
  sol = Solution()
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)
  #head.next.next.next.next.next = Node(2)

  print("Is palindrome: " + str(sol.isPalindrome(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(sol.isPalindrome(head)))

def test_reverse():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    print_list(head, "original")
    reversed = reverse(head)
    print_list(reversed, "reversed")


if __name__ == "__main__":
  main()
  # test_reverse()
