class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None
        self.is_end_of_word = False

class TrieKeyValueStore:
    def __init__(self):
        self.root = TrieNode()
    
    def set(self, key, value):
        """Insert or update the key-value pair in the trie."""
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.value = value
    
    def get(self, key):
        """Get value by key, return None if not found."""
        node = self.root
        for char in key:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.value if node.is_end_of_word else None
    
    def delete(self, key):
        """Delete key-value pair from trie if exists."""
        def _delete(node, key, depth):
            if not node:
                return False
            if depth == len(key):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                node.value = None
                return len(node.children) == 0
            char = key[depth]
            if char in node.children:
                should_delete_child = _delete(node.children[char], key, depth + 1)
                if should_delete_child:
                    del node.children[char]
                    return not node.is_end_of_word and len(node.children) == 0
            return False
        
        _delete(self.root, key, 0)

    def update(self, key, value):
        """Update the value of an existing key."""
        node = self.root
        for char in key:
            if char not in node.children:
                raise KeyError(f"Key '{key}' not found to update.")
            node = node.children[char]
        if not node.is_end_of_word:
            raise KeyError(f"Key '{key}' not found to update.")
        node.value = value

    def prefix_search(self, prefix):
        """Return list of (key, value) starting with prefix."""
        results = []
        node = self.root
        for char in prefix:
            if char not in node.children:
                return results
            node = node.children[char]

        def dfs(current_node, path):
            if current_node.is_end_of_word:
                results.append(("".join(path), current_node.value))
            for c, child_node in current_node.children.items():
                dfs(child_node, path + [c])

        dfs(node, list(prefix))
        return results

    def contains_search(self, substring):
        """Return list of (key,value) pairs with keys containing substring."""
        results = []
        
        def dfs(node, path):
            if node.is_end_of_word:
                key_str = "".join(path)
                if substring in key_str:
                    results.append((key_str, node.value))
            for c, child_node in node.children.items():
                dfs(child_node, path + [c])
        
        dfs(self.root, [])
        return results

# Example usage:
if __name__ == "__main__":
    kv = TrieKeyValueStore()
    kv.set("apple", 10)
    kv.set("appetizer", 20)
    kv.set("banana", 30)

    print(kv.get("apple"))  # 10
    kv.update("apple", 15)
    print(kv.get("apple"))  # 15
    print(kv.prefix_search("app"))  # [('apple', 15), ('appetizer', 20)]
    print(kv.contains_search("ana"))  # [('banana', 30)]
    kv.delete("banana")
    print(kv.get("banana"))  # None
