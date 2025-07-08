cmake_minimum_required(VERSION 3.22)

project(OneNightME)

set(CMAKE_CXX_STANDARD 14)

set (SOURCES    match_engine.cpp
#                main.cpp
#order.cpp
#orderBook.cpp
#tradeHandler.cpp
#inputProcessor.cpp
)

add_executable( me ${SOURCES})
