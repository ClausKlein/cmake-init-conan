cmake_minimum_required(VERSION 3.21...3.27)

include(cmake/prelude.cmake)

project(
    mytest
    VERSION 0.1.0
    DESCRIPTION "Short description"
    HOMEPAGE_URL "https://example.com/"
    LANGUAGES CXX
)

include(cmake/project-is-top-level.cmake)
include(cmake/variables.cmake)

# ---- Declare library ----

add_library(
    mytest_lib OBJECT
    source/lib.cpp
)

target_include_directories(
    mytest_lib ${warning_guard}
    PUBLIC
    "$<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/source>"
)

target_compile_features(mytest_lib PUBLIC cxx_std_17)

find_package(fmt REQUIRED)
target_link_libraries(mytest_lib PRIVATE fmt::fmt)

# ---- Declare executable ----

add_executable(mytest_exe source/main.cpp)
add_executable(mytest::exe ALIAS mytest_exe)

set_property(TARGET mytest_exe PROPERTY OUTPUT_NAME mytest)

target_compile_features(mytest_exe PRIVATE cxx_std_17)

target_link_libraries(mytest_exe PRIVATE mytest_lib)

# ---- Install rules ----

if(NOT CMAKE_SKIP_INSTALL_RULES)
  include(cmake/install-rules.cmake)
endif()

# ---- Developer mode ----

if(NOT mytest_DEVELOPER_MODE)
  return()
elseif(NOT PROJECT_IS_TOP_LEVEL)
  message(
      AUTHOR_WARNING
      "Developer mode is intended for developers of mytest"
  )
endif()

include(cmake/dev-mode.cmake)
