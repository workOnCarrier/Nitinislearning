import re, json
import logging

count = 0

logging.basicConfig(filename="run_log.log",
                    level=logging.INFO,
                    format="%(asctime)s: %(message)s ", datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger(__name__)

# input_file = "/Users/nitin.sharma/tmp/extract-2024-03-08T04_17_01.925Z.csv"
input_file = "extract-2024-03-08T04_17_01.925Z.csv"
# input_file = "tmp.rough.txt"
output_file_path_intermediate = "isolated_msg_payload.txt"
output_file_final = "final_csv.csv"

re_search_str = "EngineMessage\[\[(.*)\]\].*EngineMessage\[\[(.*)\]\]"


def get_line_from_file(file_name):
    for line in open(file_name, "r"):
        yield line

def get_message_from_line(line):
    if len(line) <= 0:
        return ""
    # logger.info(f"\t\t\t {line}")
    split_array = line.split("\"\"\"")
    mesage_orig = split_array[6]
    removed_part = mesage_orig[2:].strip() # remove starting ,"
    tmp_message_part = removed_part[:-1] # remove ending "
    # logger.info(f"\t\t\t after removing ending \" -{tmp_message_part}")
    with_back_slash = tmp_message_part.replace('""', '"') # replace "" with "
    message_part = with_back_slash 
    logger.info(f"\t\t -- {len(split_array)}__{message_part}")
    return message_part 

def get_parts_from_message(message):
    json_obj = json.loads(message)
    msg_of_interest = json_obj["message"]
    return msg_of_interest

def get_msg_part_of_interest():
    input_file_path = input_file
    logger.info(f"opening file {input_file_path}")
    lines = get_line_from_file(input_file_path)
    logger.info(f"type of lines:{type(lines)}")
    first_line = True
    global count
    with open(output_file_path_intermediate, "w") as output_file :
        for line in lines:
            if len(line) == 0 or first_line :
                first_line = False
                continue
            msg = get_message_from_line(line)
            msg_of_interest = get_parts_from_message(msg)
            print(f"msg of interest processed:{count}:", end="..")
            output_file.writelines(f"{msg_of_interest}\n")
            count = count+1
            yield msg_of_interest

def add_pattern_to_dict(result_dict, msg_to_process):
    pattern_matching = re.findall(re_search_str, msg_to_process)
    for each_match in pattern_matching:
        req = each_match[0]
        resp = each_match[1]
        json_req = json.loads(req)
        json_resp = json.loads(resp)
        account = json_req["account"]
        event_id = json_resp["inResponseTo"]
        key = (account, event_id)
        value = (req, resp)
        if key in result_dict.keys():
            if result_dict[key] != value:
                logger.info(f"mismatch in new {value} <--> existing {result_dict[key]}")
        else:
            result_dict[key] = value
            logger.info(f"adding {key} {value}")
        


def process_full():
    interting_msgs =  get_msg_part_of_interest()
    logger.info(f"type of interesting_msgs:{type(interting_msgs)}")
    result_dict = {}
    for imsg in interting_msgs:
        add_pattern_to_dict(result_dict, imsg)
    with open(output_file_final, "w") as final_output:
        for key, value in result_dict.items():
            final_output.writelines(f"{key[0]}, {key[1]}, {value[0]}, {value[1]}\n")
            logger.info(f"\t\t processing {key}")


if __name__ == "__main__":
    process_full()
    print(f"done {count}")

