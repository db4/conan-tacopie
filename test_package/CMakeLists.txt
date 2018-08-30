project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

if(NOT WIN32)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
endif()

add_executable(tacopie_logger logger.cpp)
target_link_libraries(tacopie_logger ${CONAN_LIBS})
set_target_properties(tacopie_logger PROPERTIES COMPILE_DEFINITIONS "__TACOPIE_LOGGING_ENABLED=1")
