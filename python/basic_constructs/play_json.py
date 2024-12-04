import json


try_json = """
"""

def test_json():
    json_obj = json.loads(try_json)
    print(json.dumps(json_obj))

def hw():
    print("hw")

try_json = """
{
    "name": "John",
    "age": 30,
    "city": "New York"
}
"""

def test_json():
    # Load the JSON string into a dictionary
    json_obj = json.loads(try_json)
    
    # Create a new dictionary
    new_dict = {
        "name": "Alice",
        "age": 25,
        "city": "Los Angeles"
    }
    
    # Dump the dictionary as a JSON string
    json_str = json.dumps(new_dict, indent=4)
    
    # Print the JSON string
    print(json_str)

def hw():
    print("hw")

if __name__ == "__main__":
    # hw()
    test_json()