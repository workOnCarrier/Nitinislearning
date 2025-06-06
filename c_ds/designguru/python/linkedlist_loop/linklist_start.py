
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return f"\t\t value:{self.val}"
    def __repr__(self):
       return self.__str__

class Solution:
  def findCycleStart(self, head):
    if head is None:
        return head
    # get the slow pointer to meet the faster pointer
    slow = head
    fast = head
    while fast != None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        print(f"\t\t slow:{slow} fast:{fast}")
        if fast == slow:
           break
     
    print(f"meeting point:{slow}")
    
    # circle the slow pointer to find the lenght of the circle
    nodecount = 1
    slow = slow.next
    while slow != fast :
      slow = slow.next
      nodecount += 1
    
    print(f"\t circle node count:{nodecount}")

    # move fast from head to length of the circle
    slow = head
    fast = head
    for offset in range (nodecount):
      fast = fast.next

    # move both slow and fast till they meet, this will be start of the circle
    while slow != fast:
      slow = slow.next
      fast = fast.next
    
    print(f"\t circle head:{slow}")

    return slow

def main():
  sol = Solution()
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  # Create a cycle by connecting nodes
  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(sol.findCycleStart(head).val))

  # Create a different cycle
  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(sol.findCycleStart(head).val))

  # Create a cycle that points back to the head
  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(sol.findCycleStart(head).val))

main()