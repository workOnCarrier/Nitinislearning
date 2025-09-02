## consumer group
Step	Actor	Protocol Message	Purpose
1	Consumer	HeartbeatRequest	Signal activity, detect rebalance
2	Broker	HeartbeatResponse	May include REBALANCE_IN_PROGRESS
3	Consumer	JoinGroupRequest	Rejoin group, declare topic subscription
4	Broker	JoinGroupResponse	Confirm group membership
5	Leader Consumer	SyncGroupRequest	Submit partition assignments
6	Broker	SyncGroupResponse	Notify consumers of assignments
7	Consumer	HeartbeatRequest/Response	Resume normal operation
----
### consumer group rebalance when broker triggers it
When a consumer group rebalance is triggered **by the broker** (such as for monthly maintenance in AWS MSK), the sequence of protocol messages exchanged between Kafka and consumers resembles the typical rebalance workflow but with the **initial trigger coming from the broker's group coordinator** rather than consumers themselves. Here is a simplified flow with sample messages:

## Broker-Initiated Consumer Group Rebalance Protocol Message Sequence

1. **Rebalance Trigger Notification (HeartbeatResponse or OffsetFetchResponse)**
   - The group coordinator (broker) signals the need for a rebalance by responding to consumer heartbeat or offset fetch requests with a `REBALANCE_IN_PROGRESS` error code or similar rebalance indication.
   - This alerts all consumers in the group that a rebalance is about to happen and they must prepare to rejoin.[1][6]

2. **Consumers Revoke Current Assignments**
   - Upon receiving the rebalance notification, each consumer internally revokes its current partition assignments and stops processing data from those partitions.[6]

3. **JoinGroupRequest from Consumers**
   - All consumers send a `JoinGroup` request to the group coordinator to rejoin the group, declaring their subscriptions and readiness for new assignment.[3][10]

4. **JoinGroupResponse by Coordinator**
   - The group coordinator collects all members, assigns one as group leader, and sends a `JoinGroup` response confirming group membership and providing leader details.[10]

5. **SyncGroupRequest by Leader**
   - The group leader sends a `SyncGroup` request containing the new partition assignment decisions to the group coordinator.[10]

6. **SyncGroupResponse by Coordinator**
   - The coordinator sends a `SyncGroup` response to each consumer with their updated partition assignments.[10]

7. **Consumers Resume Heartbeats and Processing**
   - Consumers acknowledge the new assignments and resume sending heartbeats and processing records for their assigned partitions.[3][6]

### Notes on Broker-Initiated Rebalance
- The **rebalance trigger is proactive from the broker side**, commonly due to maintenance events like scaling, partition redistribution, or broker restarts in MSK.[1][3]
- The protocol flow that follows remains the same as consumer-initiated rebalances but is **orchestrated by the group coordinator broker** to ensure consistent state across the group.[6][1]
- This approach ensures minimal downtime and balanced partition distribution after maintenance activities.

This sequence helps AWS MSK maintain cluster integrity and operational goals such as load balancing and fault tolerance during scheduled monthly maintenance rebalances.[1][3][6]

[1](https://www.netdata.cloud/academy/apache-kafka-consumer-lags/)
[2](https://github.com/AutoMQ/automq/wiki/Kafka-Rebalancing:-Concept-&-Best-Practices)
[3](https://www.redpanda.com/guides/kafka-performance-kafka-rebalancing)
[4](https://www.instaclustr.com/blog/rebalance-your-apache-kafka-partitions-with-the-next-generation-consumer-rebalance-protocol/)
[5](https://www.confluent.io/blog/kip-848-consumer-rebalance-protocol/)
[6](https://developer.confluent.io/courses/architecture/consumer-group-protocol/)
[7](https://www.responsive.dev/blog/guide-to-kafka-streams-rebalancing)
[8](https://www.architecture-weekly.com/p/understanding-kafkas-consumer-protocol)
[9](https://kafka.apache.org/documentation/)
[10](https://www.confluent.io/blog/cooperative-rebalancing-in-kafka-streams-consumer-ksqldb/)

## producer group
When a rebalance happens, the sequence of producer protocol messages involved is minimal because producers do not participate in consumer group rebalancing directly. The typical producer message sequence is limited to:

1. MetadataRequest / MetadataResponse
    * Producers request updated metadata to learn about partition leadership and routing changes. This happens because partitions might have been reassigned or leadership shifted during the rebalance.
2. InitProducerIdRequest / InitProducerIdResponse (For transactional producers)
    * If the producer is transactional or idempotent and a rebalance or fencing event occurs, the producer may request a new producer ID and epoch to maintain exactly-once semantics.
3. ProduceRequest / ProduceResponse
    * Producers continue sending data to the brokers as usual, based on the updated metadata.
4. ProducerFenced Error (If applicable for transactional producers) 
    * If a fencing event arises (e.g., another producer claims the same transactional ID), the broker may send a fencing error prompting the existing producer to shutdown or reinitialize.

