cmake_minimum_required(VERSION 3.15)
project(conanCppTemplate LANGUAGES CXX VERSION 0.1.0)

# spdlog使用外部fmt
add_definitions(-DSPDLOG_FMT_EXTERNAL)
aux_source_directory(${PROJECT_SOURCE_DIR}/src SOURCES)

include(CTest)
enable_testing()

add_library(hello SHARED ${SOURCES})
target_include_directories(hello PUBLIC include)

add_executable(main.exe ${SOURCES} src/bin/main.cpp)
target_include_directories(main.exe PRIVATE include)
target_link_libraries(main.exe PRIVATE fmt spdlog)

install(TARGETS hello main.exe)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)