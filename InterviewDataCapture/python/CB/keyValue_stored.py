from collections import defaultdict

class KeyValueStore:
    def __init__(self):
        self.store = defaultdict(dict)

    def set(self, timestamp, key, field, value, ttl = None):
        data = self.store[key]
        data[field] = (value, timestamp, ttl)
    
    def remove_ttl_expired(self, timestamp, key):
        data = self.store.get(key, None)
        if not data:
            return
        keys_to_remove = []
        for field, value_tuple in data.items():
            if value_tuple[2] is not None and timestamp >= value_tuple[1] + value_tuple[2]:
                keys_to_remove.append(field)
        for field in keys_to_remove:
            del data[field]

    def get(self, timestamp, key, field):
        data = self.store.get(key, None)
        if not data:
            return None
        self.remove_ttl_expired(timestamp, key)
        if field in data.keys():
            return data[field][0]
        return None

    def delete(self, timestamp, key, field):
        data = self.store.get(key, None)
        if not data:
            return False
        self.remove_ttl_expired(timestamp, key)
        if key in data.keys():
            del data[key]
            return True
        return False

    def compare_and_set(self, timestamp, key, field, expected_value, new_value, ttl = None):
        data = self.store.get(key, None)
        if not data:
            print(f"\t key:{key} not found")
            return False
        self.remove_ttl_expired(timestamp, key)
        if field in data.keys():
            existing = data[field][0]
            if existing == expected_value:
                data[field] = (new_value, timestamp, ttl)
                return True
        return False

    def prefix_search(self, timestamp, key, field, prefix):
        """Return a list of (key, value) pairs where the key starts with the prefix."""
        result = []
        data = self.store.get(key, None)
        if not data:
            return result
        self.remove_ttl_expired(timestamp, key)
        if key in data.keys():
            result  = [f"{k}({v})" for k, v in self.data.items() if k.startswith(prefix)]
        return result
    
    def set_with_ttl(self, timestamp, key, field, value, ttl):
        self.set(timestamp, key, field, value, ttl)

    def compare_and_set_with_ttl(self, timestamp, key, field, expected_value, new_value, ttl ):
        self.compare_and_set(timestamp, key, field, expected_value, new_value, ttl)
    

# Example usage:
def test():
    db = KeyValueStore()
    db.set(100, 'foo', 'bar', 1)
    get_val = db.get(101, 'foo', 'bar' )
    if get_val != 1:
        print(f" expected:{1} got:{get_val}")
    db.set_with_ttl(998, 'foo', 'bar', 1, 30)
    set_success = db.compare_and_set_with_ttl(1000, 'foo', 'bar', 1, 4, 10)
    if set_success == False:
        print(f" expected compare and set to succeed")
    else:
        print(" success ")
    expecting_None = db.get(1010, 'foo', 'bar')
    if expecting_None is None:
        print(f" expected get to fetch None")
    else:
        print(f" {expecting_None} ")



if __name__ == "__main__":
    test()