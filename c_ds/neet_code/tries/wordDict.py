class Trie:
    def __init__(self):
        self.children = {}
        self.isLast = False

class WordDictionary:
    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        print(f"\t adding {word}")
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.isLast = True

    def skipsearch(self, index, word, node) -> bool:
        if index == len(word):
            return node.isLast
        if word[index] == '.':
            for c in node.children.keys():
                print(f"\t checking for {c} in '.' case")
                if self.skipsearch(index + 1, word, node.children[c]):
                    return True
        else:
            if word[index] not in node.children:
                return False
            print(f"\t checking for {word[index]} in non '.' case")
            return self.skipsearch( index + 1, word, node.children[ word[index] ] )
        return False


    def search(self, word: str) -> bool:
        print(f"\t start for {word}")
        return self.skipsearch(0, word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
# [[ .             ,["at"]   , ["and"] ,["an"]   ,["add"]  ,["a"]   ,[".at"] ,["bat"]  ,[".at"] ,["an."] ,["a.d."],["b."]  , ["a.d"],["."]]
def test():
    obj = WordDictionary()
    obj.addWord('at')
    obj.addWord('and')
    obj.addWord('an')
    obj.addWord('add')
    print(f"{obj.search('a')}")
    print(f"{obj.search('.at')}")
    obj.addWord('bat')
    print(f"{obj.search('.at')}")
    print(f"{obj.search('.an')}")

if __name__ == "__main__":
    test()