# 0.) create source and CMakeLists.txt
# 1.) mkdir build
# 2.) cd build
# 3.) cmake ..   -- generates build and configuration files
# 4.) cmake --build .

cmake_minimum_required(VERSION 3.22)

project(Train VERSION 1.0.0 LANGUAGES CXX)
set (CMAKE_CXX_STANDARD 23)

add_executable(str2time 
                check_str_to_time_convert.cpp
                )

add_executable(str_toy 
                string_toy.cpp
                )


add_executable(template_int 
                template_int.cpp
                )
