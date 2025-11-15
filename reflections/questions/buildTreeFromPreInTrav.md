Below is a **clean revision-oriented quiz** for the classic problem **Construct Binary Tree From Preorder and Inorder Traversal** using your provided code.
It includes:

1. **Concept-focused MCQs & short-answer questions**
2. **Answer key**
3. **Final quiz question that includes the full code listing**

---

# ✅ **Quiz: Construct Binary Tree From Preorder & Inorder**

## **Section A — Conceptual Understanding**

### **Q1. (MCQ)**

In preorder traversal, the order of nodes is:

A. Left → Root → Right
B. Root → Left → Right
C. Left → Right → Root
D. Root → Right → Left

---

### **Q2. (Short Answer)**

Why do we use an **index map (imap)** for the inorder array in this reconstruction algorithm?

---

### **Q3. (MCQ)**

In the algorithm, which traversal determines the **root node** at each recursive step?

A. Inorder
B. Postorder
C. Preorder
D. Level order

---

### **Q4. (Short Answer)**

Given:

```
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]
```

What is the **root value** of the entire tree?

---

### **Q5. (MCQ)**

What does `start > end` signify in the recursive helper?

A. We found a leaf node
B. We must build a right subtree
C. No subtree exists in this range
D. The current segment is invalid and should return the root

---

### **Q6. (Short Answer)**

What is the purpose of `self.index` in the algorithm?

---

### **Q7. (MCQ)**

`mid = imap[rv]` gives:

A. The preorder index of rv
B. The inorder index of rv
C. The postorder index of rv
D. None of the above

---

### **Q8. (Short Answer)**

After finding `mid`, which range of inorder corresponds to the left subtree?

---

### **Q9. (Short Answer)**

What ensures that preorder traversal is consumed **only once** throughout the entire reconstruction?

---

### **Q10. (MCQ)**

The time complexity of this algorithm is:

A. O(n log n)
B. O(n²)
C. O(n)
D. O(log n)

---

---

# 🔍 **Section B — Code-Reasoning Quiz**

### **Q11. (Short Answer)**

Why is preorder consumed in the order `self.index += 1` rather than popping from the front of the list?

---

### **Q12. (Short Answer)**

If inorder traversal contains duplicate values, why does this algorithm break?

---

---

# 🧪 **Section C — Full Code Listing Question**

### **Q13. (Code Listing Question)**

Read the following code carefully and explain **how recursion divides the inorder array** into left and right subtrees. Your explanation should refer to `mid = imap[rv]`, `helper(start, mid-1)`, and `helper(mid+1, end)`.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        imap = {val:i for i, val in enumerate(inorder)}
        self.index = 0
        def helper(start, end):
            if start > end:
                return None
            rv = preorder[self.index]
            self.index += 1
            root = TreeNode(rv)
            mid = imap[rv]
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            return root
        return helper(0, len(inorder) - 1)
```

---

# ✅ **Answer Key**

### **A1.** B — Root → Left → Right

### **A2.**

To find the index of a value in the inorder array in O(1) time rather than O(n), enabling linear-time reconstruction.

### **A3.** C — Preorder

### **A4.** 3

### **A5.** C — No subtree exists in this range

### **A6.**

It tracks the current root position in the preorder list so we always pick the next root correctly.

### **A7.** B — The inorder index of rv

### **A8.**

`start` to `mid-1`

### **A9.**

Using a single global pointer `self.index` ensures each element is used exactly once and in order.

### **A10.** C — O(n)

### **A11.**

Because popping from the front of a Python list is O(n); using an index is O(1).

### **A12.**

Because the inorder index map relies on unique values. Duplicates make the split ambiguous.

### **A13.**

(Your explanation will vary, but must mention that `mid` partitions inorder into left and right segments corresponding to left and right subtrees, and recursion reconstructs each side using preorder order.)

---

If you'd like, I can also generate:
✅ A spaced-repetition version of the quiz
✅ Flashcards
✅ A version tailored to C++ or Java
Just tell me!
