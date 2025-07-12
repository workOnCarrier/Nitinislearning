cmake_minimum_required(VERSION 3.22)

project(LRUTest LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

enable_testing()

find_package(GTest REQUIRED)

set (LRU_SRC    lru.h)
set (LRU_TEST_SRC lru_test.cpp)
set (LRU_run lru_run.cpp)

add_executable( lru_test ${LRU_SRC})
target_link_libraries(lru_test PRIVATE GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(lru_test)


add_executable( lru_run ${LRU_SRC})