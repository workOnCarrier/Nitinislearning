cmake_minimum_required(VERSION 3.22)

project(Train VERSION 1.0.0 LANGUAGES CXX)
set (CMAKE_CXX_STANDARD 23)


set(CMAKE_BUILD_TYPE debug)
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g")
# add_executable( sample1 vowel_reverse.cpp)

# add_executable( pali palindrome.cpp)
add_executable( quardSum quardSum.cpp)

add_executable( backspaceRemove backspaceRemove.cpp)

add_executable(minWindowSort minWindowSort.cpp)
