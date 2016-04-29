project(FoundationTimer)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

if(SHARED)
  add_library(timer SHARED timer.cpp)
else()
  add_library(timer STATIC timer.cpp)
endif()
   
target_link_libraries(timer PUBLIC ${CONAN_LIBS}) 
   
add_executable(example main.cpp)
target_link_libraries(example timer)