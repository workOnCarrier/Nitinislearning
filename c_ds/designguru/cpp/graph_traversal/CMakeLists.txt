cmake_minimum_required(VERSION 3.22)

project(cppCodeDs VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)

add_executable(pathExists_my path_exists_my.cpp)
add_executable(pathExists_ref path_exists_ref.cpp)


add_executable(islands_my noOfProvinces_my.cpp)
add_executable(islands_ref noOfProvinces_ref.cpp)

add_executable(isSafeNodeMy save_node_my.cpp)
add_executable(isSafeNodeRef save_node_ref.cpp)

add_executable(isBusRoute_my bus_routes_my.cpp)
# add_executable(isBusRoute_ref bus_routes_ref.cpp)
