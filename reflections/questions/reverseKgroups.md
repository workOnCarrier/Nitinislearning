Below is a **clean, structured revision quiz** based on the logic and concepts behind your `reverseKGroup` implementation.
At the end, you’ll get the **answer key**, followed by the **final question that repeats the entire code**, as you requested.

---

# ✅ **QUIZ: Reverse Nodes in k-Group — Concept & Code Revision**

## **Section A — Conceptual Understanding**

### **1. What problem does `reverseKGroup` solve?**

A. Reverse the entire linked list
B. Reverse linked list every *k* nodes
C. Rotate the list
D. Remove nodes based on value

---

### **2. What is the purpose of the helper function `getKth`?**

A. To count total nodes
B. To return the k-th node starting from `node`
C. To reverse k nodes
D. To find the midpoint

---

### **3. What happens if `getKth` returns `None`?**

A. Continue reversing
B. Stop processing and return current list
C. Throw an error
D. Skip only one node

---

### **4. Why do we use a dummy node?**

A. Required by Python
B. Easier handling of edge cases involving the head
C. To track node count
D. For recursion

---

### **5. What does `gp` represent?**

A. The last node of the current group
B. The node before the current k-group
C. The first node of the current k-group
D. The k-th node

---

### **6. What does `gn = kth.next` represent?**

A. The next group's first node
B. A random pointer
C. The dummy node
D. The node before k-group

---

### **7. During reversal, what does this loop do?**

```python
while cur != gn:
    tmp = cur.next
    cur.next = prev
    prev = cur
    cur = tmp
```

A. Swaps nodes
B. Reverses k nodes
C. Counts nodes
D. Finds kth node

---

### **8. After reversing a group, why do we do this?**

```python
tmp = gp.next
gp.next = kth
gp = tmp
```

A. Connect reversed block and move gp forward
B. Delete the group
C. Rotate the list
D. Shift values instead of nodes

---

### **9. What is the time complexity of `reverseKGroup`?**

A. O(n²)
B. O(log n)
C. O(n)
D. O(k·n)

---

### **10. Why is the reversal done using pointers instead of values?**

A. Linked lists support random access
B. It preserves memory ordering
C. Value swaps break the problem constraints
D. Pointer manipulation is required to keep the list valid

---

---

# **Section B — Code-Focused Questions**

### **11. In the reversal loop, what is the role of `prev` initially set to `gn`?**

A. Prevents cycles by ending the reversed segment
B. Stores old head
C. Tracks group positions
D. Counts nodes

---

### **12. Which variable marks the beginning of the next group BEFORE reversal?**

A. `gp`
B. `cur`
C. `tmp`
D. `gn`

---

### **13. Which pointer becomes the new head of the reversed group?**

A. `gp`
B. `tmp`
C. `kth`
D. `cur`

---

### **14. What ensures that groups smaller than k are not reversed?**

A. The dummy node
B. The reversal loop
C. The break when `kth` is None
D. A length pre-check

---

### **15. After reversing a group, what does `gp = tmp` achieve?**

A. Moves gp to the end of the reversed group
B. Moves gp to the next group's head
C. Sets gp to None
D. Moves to the k-th node

---

---

# **Section C — Simulation Questions**

### **16. For list 1 → 2 → 3 → 4 → 5 and k = 2, what is the output?**

A. 2 → 1 → 4 → 3 → 5
B. 1 → 3 → 2 → 5 → 4
C. 2 → 1 → 3 → 4 → 5
D. 5 → 4 → 3 → 2 → 1

---

### **17. For list 1 → 2 → 3 → 4 → 5 and k = 3, what is the output?**

A. 3 → 2 → 1 → 4 → 5
B. 3 → 2 → 1 → 6 → 5
C. 3 → 1 → 2 → 4 → 5
D. 1 → 2 → 3 → 4 → 5

---

### **18. If k = 1, what happens?**

A. Reverse entire list
B. Reverse in pairs
C. Reverse in triples
D. List remains unchanged

---

### **19. If k > length of list, what happens?**

A. Full reversal
B. Program crashes
C. Entire list reversed
D. No reversal occurs

---

### **20. True or False?

The `reverseKGroup` algorithm can be implemented using recursion.**

---

---

# ✅ **ANSWER KEY**

1. B
2. B
3. B
4. B
5. B
6. A
7. B
8. A
9. C
10. C
11. A
12. D
13. C
14. C
15. A
16. A
17. A
18. D
19. D
20. True

---

# 📌 **Final question (your request): repeat the code as the last question**

### **21. Rewrite or explain the following code’s logic in your own words:**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKth(self, node, k):
        if not node:
            return None
        n = 1
        cur = node
        while cur and n < k:
            cur  = cur.next
            n += 1
        return cur

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        gp = dummy
        while True:
            kth = self.getKth(gp.next, k)
            if not kth:
                break
            gn = kth.next
    
            prev, cur = gn, gp.next
            while cur != gn:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = gp.next
            gp.next = kth
            gp = tmp
        return dummy.next
```

---

If you'd like, I can also generate:
✅ flashcards
✅ spaced-repetition version
✅ memory-hooks version
✅ diagram/visual explanation

Just tell me!
