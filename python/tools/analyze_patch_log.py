import json


count = 0
def manage_error_message(error_list, search_string, key, map, debug=False):
    for error in error_list:
        if error.find(search_string) != -1:
            if key not in map.keys():
                map[key] = 0
            map[key] += 1
            return True
        else:
            if debug:
                print(f"search_string: {search_string} not found in error: {error}")
    return False

def map_errors(error_reasons, error_reason_map, unclassified_error_reasons, debug=False):
    global count
    matched = manage_error_message(error_reasons, 'errro', 'mising_prior_next_file', error_reason_map, debug)  
    if not matched:
        matched = manage_error_message(error_reasons, 'NoSuchKey', 'NoSuchKey', error_reason_map, debug)  
    if not matched:
        matched = manage_error_message(error_reasons, 'less', 'mismatch', error_reason_map, debug)  
    if not matched:
        matched = manage_error_message(error_reasons, 'NOT', 'wrapped_case', error_reason_map, debug)  
    if not matched:
        count += 1
        unclassified_error_reasons.add(str(error_reasons))

def analyze_json_distribution(json_obj, debug=False):
    global count
    error_reason_map = {}
    unclassified_error_reasons = set()
    for obj in json_obj:
        error_reasons = obj['error_reasons']
        map_errors(error_reasons, error_reason_map, unclassified_error_reasons, debug)
        warning = obj['warning_reasons']
        map_errors(warning , error_reason_map, unclassified_error_reasons, debug)
    print(f"Total number of unclassieds: {count}")   
    return error_reason_map, unclassified_error_reasons


def segregate_by_error(file_path, output_path):
    mapped_errors = {}
    json_obj = json.load(open(file_path))
    for obj in json_obj:
        error_reasons = obj['error_reasons']
        if len(error_reasons) == 0:
            error_reasons = obj['warning_reasons']
        for error in error_reasons:
            for key, filename in error_patter_map.items():
                if error.find(key) != -1:
                    if filename not in mapped_errors.keys():
                        mapped_errors[filename] = []
                    mapped_errors[filename].append(json.dumps(obj))

    for key, value_list in mapped_errors.items():
        with open(f"{output_path}/{key}.json", 'w') as f:
            f.write("[\n")
            for count, value in enumerate(value_list):
                f.write(value)
                if count != len(value_list) - 1:
                    f.write(",")
                f.write("\n")
            f.write("]\n")

def drive_analysis():
    file_path = '/Users/nitin.sharma/work/Missing_trades_20240919/merge_cycle/prod/data_n000000000000000000000000000000000000001-n000000000000000000000000000000000000002_t1730150965204708252-t1730151843573335932_r1720_s2647224_p0.bin'
    json_obj = json.load(open(file_path))
    mapping, unclassified = analyze_json_distribution(json_obj)
    print(unclassified)
    print("--------------------------")
    print(mapping)

error_patter_map = {'no prior / next file': "sandalone_trades",
                        'NoSuchKey': "NoSuchKey",
                        'less': "mismatch",
                        'NOT': "wrapped_case"}
 
def drive_segregation():
    input_file = '/Users/nitin.sharma/work/Missing_trades_20240919/merge_cycle/prod/data_n000000000000000000000000000000000000001-n000000000000000000000000000000000000002_t1730150965204708252-t1730151843573335932_r1720_s2647224_p0.bin'
    output_path = '/Users/nitin.sharma/work/Missing_trades_20240919/merge_cycle/prod/'
    segregate_by_error(input_file, output_path)



def test_analysis():
    json_text = """{ "status" :"failure",
"merge_type" :"perform_merge_at_front",
 "file_to_be_created":[],
 "files_to_copy_across":[],
 "files_to_remove":[],
 "error_reasons":["perform_merge_at_front:: with no prior / next file identified this seems an errro"],
 "warning_reasons":[],
 "replay_merge_requirement": "ReplaySearchHelper:DatasetDataObject: production/ksw/trading.trades/acc_9906210_i_16781430/replay/data_n000000000000007359999672082457572671488-n000000000000007359999672082457572671488_t1726689989950379305-t1726689989950379305_r1_s272_p0.bin:acc_9906210_i_16781430:data_n000000000000007359999672082457572671488-n000000000000007359999672082457572671488_t1726689989950379305-t1726689989950379305_r1_s272_p0.bin:2024-09-18 20:06:29:2024-09-18 20:06:29 prior:DatasetDataObject: :::1970-01-01 00:00:00:1970-01-01 00:00:00 next:DatasetDataObject: :::1970-01-01 00:00:00:1970-01-01 00:00:00 wrapped_objects:0"
}"""
    json_obj = json.loads(json_text)
    mapping, unclassified = analyze_json_distribution([json_obj], True)
    print(unclassified)
    print("\n--------------------------")
    print(mapping)

if __name__ == '__main__':
    # drive_analysis()
    # test_analysis()
    drive_segregation()

