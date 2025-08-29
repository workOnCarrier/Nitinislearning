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
