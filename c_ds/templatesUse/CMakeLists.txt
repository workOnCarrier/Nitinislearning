# 0.) create source and CMakeLists.txt
# 1.) mkdir build
# 2.) cd build
# 3.) cmake ..   -- generates build and configuration files
# 4.) cmake --build .

cmake_minimum_required(VERSION 3.22)

project(CustomPriorityQueue VERSION 1.0.0 LANGUAGES CXX)
set (CMAKE_CXX_STANDARD 17)

add_executable(custPriorityq 
                play_priority_queue.cpp
                )
