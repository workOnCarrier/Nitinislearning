import json


data=''''''

sample_json = '''{
        "module_type_id": "FIX_OE",
        "partition_type": "LEDGER",
        "partition_num": "<partition_num>",
        "redundancy_instance": "<redundant_instance>",
        "multiplicity": "30",
        "command": "FIXAddOrderSessionRequest",
        "name": "<comp_id>",
        "target_comp_id": "<comp_id>",
        "port": "<port>",
        "account": "<account_id>",
        "sessionId": "<session_id>",
        "session_logger": "FALSE",
        "protocol_logger": "FALSE",
        "sender_comp_id": "GEMINIORD",
        "throttle": "<throttle>",
	"obo_mode": "None"
    }'''

def convert_to_json(field_list: list) -> json:
    json_sample = json.loads(sample_json)
    json_sample["partition_num"] = field_list[2]
    json_sample["redundancy_instance"] = field_list[0]
    json_sample["name"] = field_list[4]
    json_sample["target_comp_id"] = field_list[5]
    json_sample["port"] = field_list[6]
    json_sample["account"] = field_list[7]
    json_sample["sessionId"] = field_list[8]
    json_sample["throttle"] = field_list[12]
    yield json_sample

def get_single_data(data_list :str) -> str:
    for row in data.split('\n'):
        yield row

def get_json_entry(data_item: str) -> str:
    for cols in data_item:
        yield from convert_to_json(cols.split('|'))

def generate_json_file():
    with open("oe_sessions.json", "w+") as file:
        file.write("[\n")
        all_json = get_json_entry(get_single_data(data))
        line_count = 0
        for json_data in all_json:
            if line_count > 0:
                file.write(",\n")
            file.write(json.dumps(json_data))
            line_count += 1
        file.write("\n]")
    pass


if __name__ == "__main__":
    generate_json_file()