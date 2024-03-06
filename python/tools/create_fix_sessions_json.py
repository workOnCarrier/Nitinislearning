import json

meta=""" redundant_instance | partition_type | partition_num | multiplicity_num |  session_name   | target_comp_id  | port | account_id | session_id | session_logger | protocol_logger | sender_comp_id | throttle | obo_mode"""

data='''A|LEDGER|1|0|JSTCORDPRODP002|JSTCORDPRODP002|2108|30177608|2108|f|f|GEMINIORD|0|0
B|LEDGER|1|0|JSTCORDPRODP002|JSTCORDPRODP002|2108|30177608|2108|f|f|GEMINIORD|0|0
A|LEDGER|1|1|AKUNORDPROD001|AKUNORDPROD001|2114|2716929|2114|f|f|GEMINIORD|37|0
B|LEDGER|1|1|AKUNORDPROD001|AKUNORDPROD001|2114|2716929|2114|f|f|GEMINIORD|37|0
A|LEDGER|1|0|JSTCORDPRODP003|JSTCORDPRODP003|2109|30177608|2109|f|f|GEMINIORD|0|0
B|LEDGER|1|0|JSTCORDPRODP003|JSTCORDPRODP003|2109|30177608|2109|f|f|GEMINIORD|0|0
A|LEDGER|1|0|JSTCORDPRODP001|JSTCORDPRODP001|2085|30177608|30177608|f|f|GEMINIORD|125|0
B|LEDGER|1|0|JSTCORDPRODP001|JSTCORDPRODP001|2085|30177608|30177608|f|f|GEMINIORD|125|0
A|LEDGER|2|0|AKUNORDPRODP001|AKUNORDPRODP001|2088|30177821|30177821|f|f|GEMINIORD|225|0
A|LEDGER|1|0|PTRNORDPRODP002|PTRNORDPRODP002|2116|30177646|2116|f|f|GEMINIORD|50|0
B|LEDGER|1|0|PTRNORDPRODP002|PTRNORDPRODP002|2116|30177646|2116|f|f|GEMINIORD|50|0
B|LEDGER|2|0|AKUNORDPRODP001|AKUNORDPRODP001|2088|30177821|30177821|f|f|GEMINIORD|225|0
A|LEDGER|2|0|AKUNORDPRODP002|AKUNORDPRODP002|2103|30177821|2103|f|f|GEMINIORD|225|0
B|LEDGER|2|0|AKUNORDPRODP002|AKUNORDPRODP002|2103|30177821|2103|f|f|GEMINIORD|225|0
B|LEDGER|2|0|AKUNORDPRODP003|AKUNORDPRODP003|2110|30177821|2110|f|f|GEMINIORD|225|0
A|LEDGER|2|0|AKUNORDPRODP003|AKUNORDPRODP003|2110|30177821|2110|f|f|GEMINIORD|225|0
A|LEDGER|1|0|PTRNORDPRODP001|PTRNORDPRODP001|2091|30177646|30177646|f|f|GEMINIORD|225|0
B|LEDGER|1|0|PTRNORDPRODP001|PTRNORDPRODP001|2091|30177646|30177646|f|f|GEMINIORD|225|0
A|LEDGER|1|0|PULSORDPRODP001|PULSORDPRODP001|2094|30177625|30177625|f|f|GEMINIORD|225|0
B|LEDGER|1|0|PULSORDPRODP001|PULSORDPRODP001|2094|30177625|30177625|f|f|GEMINIORD|225|0
A|LEDGER|2|0|TACHORDPRODP001|TACHORDPRODP001|2101|30179845|30179845|f|f|GEMINIORD|225|0
B|LEDGER|2|0|TACHORDPRODP001|TACHORDPRODP001|2101|30179845|30179845|f|f|GEMINIORD|225|0'''

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