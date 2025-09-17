# 0.) create source and CMakeLists.txt
# 1.) mkdir build
# 2.) cd build
# 3.) cmake ..   -- generates build and configuration files
# 4.) cmake --build .

cmake_minimum_required(VERSION 3.22)

project(Train VERSION 1.0.0 LANGUAGES CXX)
set (CMAKE_CXX_STANDARD 23)

set(CMAKE_BUILD_TYPE debug)
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g")

add_executable(plus_one plus_one.cpp)

add_executable(merge_alt_str merge_alternate.cpp)

add_executable(climbStairs climbstair.cpp)

add_executable(movingAvg movingAverage.cpp)

add_executable(fib fibonacii.cpp)

add_executable(rotstr rotatingStr.cpp)

add_executable(decode decode_msg.cpp)

add_executable(countAndSay countAndSay.cpp)

add_executable(spiralMatrix spiral_matrix.cpp)

add_executable(mergeInter merge_intervals.cpp)

add_executable(permutations permutations.cpp)

add_executable(playStringView playStringView.cpp)

add_executable(shortWordDist shortestWordDistance.cpp)

add_executable(rangeSum rangeSum.cpp)

add_executable(randomPickWei randomPickWeighted.cpp)

add_executable(insertRemoveGetrandom insertRemoveGetrandom.cpp)

add_executable(allGoodIndices allGoodIndices.cpp)

add_executable(removeComments removeComments.cpp)

add_executable(blackBlocks blackBlocks.cpp)

add_executable(blackBlocks_ref blackBlocks_ref.cpp)

add_executable(longestCommonPrefix longestCommonPrefix.cpp)

add_executable(longestCommonPrefix_ref longestCommonPrefix_ref.cpp)

add_executable(mentionsPerUser mentionsPerUser.cpp)
