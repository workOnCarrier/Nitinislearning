from typing import Optional
from time import sleep
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        list_len = 0
        cur_pos = head
        while cur_pos is not None:
            cur_pos = cur_pos.next
            list_len += 1
        rotate_count = k % list_len
        cur_pos = head

        for _ in range(rotate_count):
            cur_pos = cur_pos.next
        prev = head
        while cur_pos.next is not None:
            prev = prev.next
            cur_pos = cur_pos.next
        nhead = prev.next 
        if nhead is None:
            return head
        prev.next = None
        cur_pos.next = head
        head = nhead
        return head

def display(head: Optional[ListNode], qualifier = ""):
    cp = head
    print(f"\t {qualifier} list:")
    while cp is not None:
        print(f"{cp.val},")
        sleep(1)
        cp = cp.next

        
def test():
    s = Solution()
    input = ListNode(1)
    display(input, "input")
    output = s.rotateRight(input, 0)
    display(output, "output")
    
if __name__ == "__main__":
    test()