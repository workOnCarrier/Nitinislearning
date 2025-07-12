#include <gtest/gtest.h>


#include "lru.h"

// Unit tests
TEST(LRUTest, PutAndGet) {
    LRU<int> cache(2);
    cache.put(1, 10);
    cache.put(2, 20);
    EXPECT_EQ(cache.get(1), 10);
    EXPECT_EQ(cache.get(2), 20);
}

TEST(LRUTest, Eviction) {
    LRU<int> cache(2);
    cache.put(1, 10);
    cache.put(2, 20);
    cache.put(3, 30); // Should evict key 1
    EXPECT_THROW(cache.get(1), std::runtime_error);
    EXPECT_EQ(cache.get(2), 20);
    EXPECT_EQ(cache.get(3), 30);
}

TEST(LRUTest, UpdateExisting) {
    LRU<int> cache(2);
    cache.put(1, 10);
    cache.put(1, 15); // Update value
    EXPECT_EQ(cache.get(1), 15);
}

TEST(LRUTest, AccessMovesToFront) {
    LRU<int> cache(2);
    cache.put(1, 10);
    cache.put(2, 20);
    cache.get(1); // Now 2 is LRU
    cache.put(3, 30); // Should evict 2
    EXPECT_THROW(cache.get(2), std::runtime_error);
    EXPECT_EQ(cache.get(1), 10);
    EXPECT_EQ(cache.get(3), 30);
}

// Integration test
TEST(LRUTest, IntegrationScenario) {
    LRU<std::string> cache(3);
    cache.put(1, "one");
    cache.put(2, "two");
    cache.put(3, "three");
    EXPECT_EQ(cache.get(2), "two");
    cache.put(4, "four"); // evicts 1
    EXPECT_THROW(cache.get(1), std::runtime_error);
    cache.put(5, "five"); // evicts 3
    EXPECT_THROW(cache.get(3), std::runtime_error);
    EXPECT_EQ(cache.get(2), "two");
    EXPECT_EQ(cache.get(4), "four");
    EXPECT_EQ(cache.get(5), "five");
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}