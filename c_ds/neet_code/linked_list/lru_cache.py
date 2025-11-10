class LinkNode:
    def __init__(self, key, val, prv = None, nxt = None):
        self.key, self.val = key, val
        self.prv, self.nxt = prv, nxt
class LRUCache:

    def __init__(self, capacity: int):
        self.head, self.tail = None, None
        self.size, self.capacity = 0, capacity
        self.datamap = {}
    
    def display(method):
        def wrapper(self, *args, **kwargs):
            args_str = ', '.join(repr(a) for a in args)
            print(f"\t entering {method.__name__} with {args_str}", end= "")
            result = method(self, *args, **kwargs)
            c = self.head
            hax = lambda x : hex(id(x))[-5:] if x is not None else "None"
            while c:
                print(f"\t {hax(c.prv)}_{c.key}:{c.val}_{hax(c.nxt)}", end="")
                c = c.nxt
            # for key, val in self.datamap.items():
            #     print(f"\t {val.key}:{val.val}", end=", ")
            print(f"\t exiting {method.__name__} h {id(self.head)} t {id(self.tail)} returns : {result}")
            return result
        return wrapper

    @display    
    def get(self, key: int) -> int:
        if key in self.datamap:
            node = self.datamap[key]
            if node.prv == None and node.nxt == None:
                # node is head and tail
                return node.val
            else:
                if node.nxt == None:
                    # already the last node
                    return node.val
                if node.prv == None:
                    self.head = node.nxt
                    node.nxt.prv = None
                else:
                    node.prv.nxt = node.nxt
                    node.nxt.prv = node.prv
                self.tail.nxt = node
                node.prv = self.tail
                self.tail = node
                node.nxt = None
            return node.val
        else:
            return -1
    @display    
    def put(self, key: int, value: int) -> None:
        if key in self.datamap:
            self.datamap[key].val = value
            self.get(key)
            return
        self.size += 1
        if self.size == 1:
            self.head = self.tail = LinkNode(key, value)
        else:
            self.tail.nxt = LinkNode(key, value, self.tail)
            self.tail = self.tail.nxt
        self.datamap[key] = self.tail
        if self.size > self.capacity:
            print(f"\t h {self.head.val} t {self.tail.val}, s: {self.size}")
            to_del = self.head
            self.head = self.head.nxt
            self.head.prv = None
            self.size -= 1
            del self.datamap[to_del.key]
        

        

def test():
    # ["LRUCache", [2], "put", [1, 1], "put", [2, 2], "get", [1], "put", [3, 3], "get", [2], "put", [4, 4], "get", [1], "get", [3], "get", [4]]
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    lRUCache.get(1)
    lRUCache.put(3, 3)
    lRUCache.get(2)
    lRUCache.put(4, 4)
    lRUCache.get(1)
    lRUCache.get(3)
    lRUCache.get(4)

def test2():
    # ["LRUCache", [3], "put", [1, 1], "put", [2, 2], "put", [3, 3], "get", [1], "get", [2], "get", [3], "get", [4], "put", [4, 4], "get", [1], "get", [2], "get", [3], "get", [4]]
    lRUCache = LRUCache(3)
    lRUCache.put(1,1)
    lRUCache.put(2,2)
    lRUCache.put(3,3)
    lRUCache.get(1)
    lRUCache.get(2)
    lRUCache.get(3)
    lRUCache.get(4)
    lRUCache.put(4,4)
    lRUCache.get(1)
    lRUCache.get(2)
    lRUCache.get(3)
    lRUCache.get(4)

def test3():
    lRUCache = LRUCache(4) # ["LRUCache", [4],
    lRUCache.put(1, 1) # "put", [1, 1],
    lRUCache.put(2, 2) # "put", [2, 2], 
    lRUCache.put(3, 3) # "put", [3, 3],
    lRUCache.get(1)    # "get", [1],
    lRUCache.get(2)    # "get", [2],
    lRUCache.get(4)    #  "get", [4],
    lRUCache.put(4, 4) #  "put", [4, 4], 
    lRUCache.get(1)    # "get", [1],
    lRUCache.get(2)    # "get", [2], 
    lRUCache.get(3)    # "get", [3], 
    lRUCache.get(4)    # "get", [4], 
    lRUCache.get(2)    # "get", [2], 
    lRUCache.put(5, 5) # "put", [5, 5], 
    lRUCache.get(1)    # "get", [1],
    lRUCache.get(2)    # "get", [2],
    lRUCache.get(3)    # "get", [3],
    lRUCache.get(4)    # "get", [4],
    lRUCache.get(5)    # "get", [5],
    lRUCache.get(2)    # "get", [2],
    lRUCache.get(3)    # "get", [3],
    lRUCache.get(4)    # "get", [4],
    lRUCache.put(6, 6) # "put", [6,6],
    lRUCache.get(1)    # "get", [1],
    lRUCache.get(2)    # "get", [2],
    lRUCache.get(3)    # "get", [3],
    lRUCache.get(4)    # "get", [4],
    lRUCache.get(5)    # "get", [5],
    lRUCache.get(6)    # "get", [6]]
    # expected [null,null,null,null,1,2,-1,null,1,2,3,4,2,null,-1,2,3,4,5,2,3,4,null,-1,2,3,4,-1,6]

if __name__ == "__main__":
    test3()