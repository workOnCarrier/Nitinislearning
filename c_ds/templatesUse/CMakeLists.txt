# 0.) create source and CMakeLists.txt
# 1.) mkdir build
# 2.) cd build
# 3.) cmake ..   -- generates build and configuration files
# 4.) cmake --build .

cmake_minimum_required(VERSION 3.22)

project(CustomPriorityQueue VERSION 1.0.0 LANGUAGES CXX)
set (CMAKE_CXX_STANDARD 20)

add_executable(custPriorityq 
                play_priority_queue.cpp
                )

add_executable(variable_parms 
                variable_params.cpp
                )

add_executable(map_use_learn map_use_learn.cpp)

add_executable(vector_use_learn vector_use_learn.cpp)

add_executable(play_crtp curiously_recurring_template.cpp)