cmake_minimum_required(VERSION 3.22)

project(cppCodeDs VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)

add_executable(pathExists_my path_exists_my.cpp)
add_executable(pathExists_ref path_exists_ref.cpp)


