install(
    TARGETS mytest_exe
    RUNTIME COMPONENT mytest_Runtime
)

if(PROJECT_IS_TOP_LEVEL)
  include(CPack)
endif()
