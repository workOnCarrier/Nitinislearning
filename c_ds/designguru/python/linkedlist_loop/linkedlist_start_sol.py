class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Function to find the start of the cycle in a linked list
    def findCycleStart(self, head):
        if head is None:
            return None

        slow = head
        fast = head

        # Step 1: Detect cycle using two pointers
        while fast is not None and fast.next is not None:
            slow = slow.next          # Move slow pointer by 1
            fast = fast.next.next     # Move fast pointer by 2

            if slow == fast:          # Cycle detected
                break

        # If no cycle is found
        if fast is None or fast.next is None:
            return None

        # Step 2: Find the start of the cycle
        slow = head                   # Reset slow to head
        while slow != fast:
            slow = slow.next          # Move slow by 1
            fast = fast.next          # Move fast by 1

        # Both pointers meet at the start of the cycle
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