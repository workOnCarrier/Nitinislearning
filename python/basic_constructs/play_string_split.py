import re, json

input_str = """
For some reason advance deposit EngineMessage[[{"account":33075275,"amount":{"currency":"USD","value":"96.51"},"reason":{"transactionNumber":"207622ea-52b0-4b45-a6ce-f80e4b9a8030","$type":"InstantCard"},"fee":{"currency":"USD","value":"3.49"},"$type":"AdvanceDepositV1"}]] was not successful ( 209706313817 EngineMessage[[{"inResponseTo":209706313817,"created":1707955806570,"raptorLedgerTransactionId":0,"successful":false,"ledgerOperations":[],"message":{"account":33075275,"amount":{"currency":"USD","value":"96.51"},"reason":{"transactionNumber":"207622ea-52b0-4b45-a6ce-f80e4b9a8030","$type":"InstantCard"},"fee":{"currency":"USD","value":"3.49"},"$type":"AdvanceDepositV1"},"$type":"LedgerResponseV1"}]])
"""

re_search_str = "EngineMessage\[\[(.*)\]\].*EngineMessage\[\[(.*)\]\]"

def process_str(input_str) -> ():
    result_arr = re.findall(re_search_str, input_str)
    return result_arr


def sample_run():
    result_arr = process_str(input_str)
    print(type(result_arr), result_arr)
    for i in result_arr:
        json_obj_req = json.loads(i[0])
        json_obj_resp = json.loads(i[1])
        account = json_obj_req["account"]
        event_id = json_obj_resp["inResponseTo"]
        print(f"account : {account}, event_id : {event_id}")

    print(f"\t\t{input_str}")


if __name__ == "__main__":
    sample_run()