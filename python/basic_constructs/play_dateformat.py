import datetime
import json


def sample():
    timestamp = 1696509105.133
    print(f"checking for {timestamp}")
    date = datetime.datetime.utcfromtimestamp(timestamp)
    # date = datetime.datetime.fromtimestamp(timestamp)
    print(date)


input = """
{"@timestamp": 1696509105132, "ddtags": { "team": "tradingsys" }, "status": "error", "message": "Halting on Exception: 2023-10-05 12:31:45.132818: Broker: Not coordinator [16] (external/com_github_morganstanley_modern_cpp_kafka/include/kafka/KafkaConsumer.h:763)" }
{"@timestamp": 1696509105133, "ddtags": { "team": "tradingsys" }, "status": "info", "message": "Closed Socket[fd=45]" }
{"@timestamp": 1696509105133, "ddtags": { "team": "tradingsys" }, "status": "info", "message": "KafkaFixDropCopyApp::run() - KafkaFixDropCopyApp::keepRunning returned exiting" }
{"@timestamp": 1696509106177, "ddtags": { "team": "tradingsys" }, "status": "warning", "message": "KafkaConsumer[FIX_DC.L1.1] COMMITFAIL | [thrd:main]: Offset commit (manual) failed for 1/1 partition(s) in join-state steady: Broker: Not coordinator: trading.command.topic[0]@16045507(Broker: Not coordinator)" }
{"@timestamp": 1696511141262, "ddtags": { "team": "tradingsys" }, "status": "info", "message": "KafkaConsumer[FIX_DC.L1.1] FAIL | [thrd:ssl://b-3.raptor-msk-production.jysd8s.c9.kafka.us-east-1.amazo]: ssl://b-3.raptor-msk-production.jysd8s.c9.kafka.us-east-1.amazonaws.com:9094/3: Disconnected (after 15856869ms in state UP)" }
{"@timestamp": 1696511141265, "ddtags": { "team": "tradingsys" }, "status": "error", "message": "KafkaConsumer[FIX_DC.L1.1] FAIL | [thrd:ssl://b-3.raptor-msk-production.jysd8s.c9.kafka.us-east-1.amazo]: ssl://b-3.raptor-msk-production.jysd8s.c9.kafka.us-east-1.amazonaws.com:9094/3: Connect to ipv4#10.128.158.69:9094 failed: Connection refused (after 2ms in state CONNECT)" }
{"@timestamp": 1696511141417, "ddtags": { "team": "tradingsys" }, "status": "error", "message": "KafkaConsumer[FIX_DC.L1.1] FAIL | [thrd:ssl://b-3.raptor-msk-production.jysd8s.c9.kafka.us-east-1.amazo]: ssl://b-3.raptor-msk-production.jysd8s.c9.kafka.us-east-1.amazonaws.com:9094/3: Connect to ipv4#10.128.158.69:9094 failed: Connection refused (after 0ms in state CONNECT, 1 identical error(s) suppressed)" }
{"@timestamp": 1696518572725, "ddtags": { "team": "tradingsys" }, "status": "info", "message": "Handling SIGTERM" }}
"""
def dump_log():
    for line in input.split("\n"):
        if len(line) > 10:
            timestampfield = line.split(",")[0]
            timestamp = timestampfield.split(":")[1].strip()
            float_val = float(timestamp)/1000
            hr_time = datetime.datetime.fromtimestamp(float_val)
            message = line.split(",")[3:]
            # print(timestamp, float_val, hr_time, message)
            print(hr_time, message)
        else:
            continue



if __name__ == "__main__":
    # sample()
    dump_log()