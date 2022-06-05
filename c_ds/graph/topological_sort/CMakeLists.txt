
cmake_minimum_required(VERSION 3.10)

project(Topologicalsort VERSION 0.1)

set(SOURCE_test eval_graph_t.cpp)
set(SOURCE topological_sort.cpp)
add_executable(${PROJECT_NAME} ${SOURCE})
add_executable(Test_graph_functions ${SOURCE_test})