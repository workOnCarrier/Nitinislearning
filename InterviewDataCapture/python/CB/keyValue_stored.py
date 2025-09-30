from collections import defaultdict

class KeyValueStore:
    def __init__(self):
        self.store = defaultdict(dict)
        self.purged_store = defaultdict(dict)

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
            self.purged_store[key][field] = data[field]
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
            self.purged_store[key][field] = data[field]
            del data[key]
            return True
        return False

    def compare_and_set(self, timestamp, key, field, expected_value, new_value, ttl = None):
        data = self.store.get(key, None)
        if not data:
            return False
        self.remove_ttl_expired(timestamp, key)
        if field in data.keys():
            existing = data[field][0]
            if existing == expected_value:
                data[field] = (new_value, timestamp, ttl)
                return True
        return False

    def search(self, timestamp, key, field):
        result = []
        data = self.store.get(key, None)
        if not data:
            return result
        self.remove_ttl_expired(timestamp, key)
        if key in data.keys():
            result  = [f"{k}({v})" for k, v in sorted(data.items())]
        return result
 
    def prefix_search(self, timestamp, key, field, prefix):
        result = []
        data = self.store.get(key, None)
        if not data:
            return result
        self.remove_ttl_expired(timestamp, key)
        if field in data.keys():
            result  = [f"{k}({v})" for k, v in sorted(data.items()) if k.startswith(prefix)]
        return result
    
    def set_with_ttl(self, timestamp, key, field, value, ttl):
        self.set(timestamp, key, field, value, ttl)

    def compare_and_set_with_ttl(self, timestamp, key, field, expected_value, new_value, ttl ):
        self.compare_and_set(timestamp, key, field, expected_value, new_value, ttl)
    
    def search_historical_at_timestamp(self, timestamp, key, field, historical_ts):
        result = []
        historical_data = self.purged_store.get(key, None)
        if historical_data:
            result  = [f"{k}({v})" for k, v in sorted(historical_data.items()) if v[1] <= historical_ts]

        data = self.store.get(key, None)
        if field in data.keys():
            result  += [f"{k}({v})" for k, v in sorted(data.items()) if v[1] <= historical_ts]

        return result
 
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
    print(f"{'-'*10}")

def test_historical():
    db = KeyValueStore()
    db.set(100, 'foo', 'bar', 1)
    db.set_with_ttl(102, 'foo', 'bar_', 5, 10)
    db.set_with_ttl(103, 'foo', 'bar', 6, 10)
    get_val = db.get(104, 'foo', 'bar' )
    if get_val != 1:
        print(f" expected:{1} got:{get_val}")
    search_before_ttl_expiry = db.search(111, 'foo', 'bar')
    print(f" before ttl expiry:{search_before_ttl_expiry}")
    search_after_ttl_expiry = db.search(112, 'foo', 'bar')
    db.set(113, 'foo', '_bar_', 1)
    print(f" after ttl expiry:{search_after_ttl_expiry}")
    search_history = db.search_historical_at_timestamp(115, 'foo', 'bar', 110)
    print(f" history ttl expiry:{search_history}")


if __name__ == "__main__":
    test()
    test_historical()