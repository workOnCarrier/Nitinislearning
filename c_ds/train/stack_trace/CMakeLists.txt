cmake_minimum_required(VERSION 3.22)

project(Train_stack_analysis VERSION 1.0.0 LANGUAGES CXX)
set (CMAKE_CXX_STANDARD 23)

add_executable(stack_trace 
                stack_trace_capture_sample_1.cpp
                )

# Add the -rdynamic flag to the linker
target_link_options(stack_trace PRIVATE -rdynamic)

# Or, alternatively, set the flag globally (for all executables)
# set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -rdynamic")