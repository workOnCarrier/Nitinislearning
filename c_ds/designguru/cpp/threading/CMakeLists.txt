cmake_minimum_required(VERSION 3.22)

project(threading VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)

add_executable( buggy buggy_for_review.cpp)

add_executable( locked_bugfix bugfixed_with_locks.cpp)

add_executable( lockfree_bugfix bugfixed_with_lockfree.cpp)
