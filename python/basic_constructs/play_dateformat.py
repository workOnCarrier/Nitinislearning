import datetime
import json


def sample():
    timestamp = 1696509105.133
    print(f"checking for {timestamp}")
    date = datetime.datetime.utcfromtimestamp(timestamp)
    # date = datetime.datetime.fromtimestamp(timestamp)
    print(date)


input = """
{"@timestamp": 1707142424164, "ddtags": { "team": "tradingsys" }, "status": "info", "message": "KafkaConsumer[FIX_DC.L1.1] re-balance event triggered[ASSIGN_PARTITIONS], cooperative[disabled], topic-partitions[trading.command.topic-0]" }
{"@timestamp": 1707142424165, "ddtags": { "team": "tradingsys" }, "status": "info", "message": "Starting as Standby - awaiting leader election" }
{"@timestamp": 1707142424165, "ddtags": { "team": "tradingsys" }, "status": "info", "message": "Application State Change: module_id=FIX_DC.L1.1-A key=LeaderElection value=STARTED" }
{"@timestamp": 1707142424165, "ddtags": { "team": "tradingsys" }, "status": "info", "message": "Application State Change: module_id=FIX_DC.L1.1-A key=LeaderElection value=STANDBY" }
{"@timestamp": 1707143231476, "ddtags": { "team": "tradingsys" }, "status": "warning", "message": "KafkaConsumer[FIX_DC.L1.1] COMMITFAIL | [thrd:main]: Offset commit (manual) failed for 1/1 partition(s) in join-state steady: Broker: Not coordinator: trading.command.topic[0]@26690047(Broker: Not coordinator)" }
{"@timestamp": 1707143231476, "ddtags": { "team": "tradingsys" }, "status": "warning", "message": "KafkaConsumer[FIX_DC.L1.1] COMMITFAIL | [thrd:main]: Offset commit (manual) failed for 1/1 partition(s) in join-state steady: Local: Broker transport failure: trading.command.topic[0]@26690048(Local: Broker transport failure)" }
{"@timestamp": 1707143305670, "ddtags": { "team": "tradingsys" }, "status": "info", "message": "Elected fault tolerance leader: transitioning from Standby -> Primary" }
{"@timestamp": 1707143305725, "ddtags": { "team": "tradingsys" }, "status": "info", "message": "QUERY: SELECT redundant_instance, partition_type, partition_num, multiplicity_num, session_name, target_comp_id, port, account_id, session_id, session_logger, protocol_logger, sender_comp_id, throttle FROM fix_drop_copy_sessions WHERE redundant_instance='A' AND partition_type='LEDGER' AND partition_num=1 AND multiplicity_num=1" }
{"@timestamp": 1707143305804, "ddtags": { "team": "tradingsys" }, "status": "info", "message": "GRPCFixRecoveryEngine::asyncRecover - enqueueing request: [FixRecoveryRequest [request_type=IN_OUT_SEQ_NUMBERS, inner_request=InAndOutSeqNumbersRequest [requests=FixSeqNumberRequest [probe_id=1707143305804405485, session_id=3009]]]]" }
{"@timestamp": 1707143421929, "ddtags": { "team": "tradingsys" }, "status": "info", "message": "GRPCFixRecoveryEngine::asyncRecover - enqueueing request: [FixRecoveryRequest [request_type=IN_OUT_SEQ_NUMBERS_BY_DURATION, inner_request=InAndOutSeqNumbersByDurationRequest [session_id=3009, lookback_in_ms=5000]]]" }
{"@timestamp": 1707143517864, "ddtags": { "team": "tradingsys" }, "status": "info", "message": "InAndOutSeqNumbersByDurationResponse [session_id=3009 incoming_size=0 outgoing_size=1]" }
{"@timestamp": 1707143526716, "ddtags": { "team": "tradingsys" }, "status": "info", "message": "KafkaConsumer[FIX_DC.L1.1] re-balance event triggered[ASSIGN_PARTITIONS], cooperative[disabled], topic-partitions[trading.command.topic-0]" }
{"@timestamp": 1707143526716, "ddtags": { "team": "tradingsys" }, "status": "error", "message": "Halting on Exception: Broker: Coordinator load in progress" }
{"@timestamp": 1707143526719, "ddtags": { "team": "tradingsys" }, "status": "info", "message": "KafkaFixDropCopyApp::run() - KafkaFixDropCopyApp::keepRunning returned exiting" }
{"@timestamp": 1707143526720, "ddtags": { "team": "tradingsys" }, "status": "info", "message": "Closed Socket[fd=45]" }
"""

def dump_log():
    for line in input.split("\n"):
        if len(line) > 10:
            timestampfield = line.split(",")[0]
            timestamp = timestampfield.split(":")[1].strip()
            float_val = float(timestamp)/1000
            hr_time = datetime.datetime.fromtimestamp(float_val, tz=datetime.timezone.utc)
            message = line.split(",")[3:]
            # print(timestamp, float_val, hr_time, message)
            print(hr_time, message)
        else:
            continue



if __name__ == "__main__":
    # sample()
    dump_log()