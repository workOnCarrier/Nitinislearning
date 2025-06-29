#include <iostream>
#include <hiredis/hiredis.h>

int main() {
    // Connect to Redis
    // redisContext* c = redisConnect("127.0.0.1", 6379);
    redisContext* c = redisConnect("host.docker.internal", 6379);
    if (c == nullptr || c->err) {
        if (c) {
            std::cerr << "Connection error: " << c->errstr << std::endl;
            redisFree(c);
        } else {
            std::cerr << "Connection error: can't allocate redis context\n";
        }
        return 1;
    }

    // Set key "foo" to "bar"
    redisReply* reply = (redisReply*)redisCommand(c, "SET foo bar");
    std::cout << "SET: " << reply->str << std::endl;
    freeReplyObject(reply);

    // Get key "foo"
    reply = (redisReply*)redisCommand(c, "GET foo");
    std::cout << "GET foo: " << reply->str << std::endl;
    freeReplyObject(reply);

    // Cleanup
    redisFree(c);
    return 0;
}
