cmake_minimum_required(VERSION 3.22)

project(OneNightME)

set(CMAKE_CXX_STANDARD 20)

set (SOURCES    match_engine.cpp
#                main.cpp
#order.cpp
#orderBook.cpp
#tradeHandler.cpp
#inputProcessor.cpp
)

set (SOURCES_2    match_engine_23.cpp)

add_executable( me ${SOURCES})
add_executable( me_ll ${SOURCES_2})
