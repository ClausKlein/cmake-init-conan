# Parent project does not export its library target, so this CML implicitly
# depends on being added from it, i.e. the testing is done only from the build
# tree and is not feasible from an install location

project(mytestTests LANGUAGES CXX)

# ---- Dependencies ----

find_package(Catch2 REQUIRED)
include(Catch)

# ---- Tests ----

add_executable(mytest_test source/mytest_test.cpp)
target_link_libraries(
    mytest_test PRIVATE
    mytest_lib
    Catch2::Catch2WithMain
)
target_compile_features(mytest_test PRIVATE cxx_std_17)

catch_discover_tests(mytest_test)

# ---- End-of-file commands ----

add_folders(Test)
