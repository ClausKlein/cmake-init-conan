find_program(SPELL_COMMAND codespell)
if(NOT SPELL_COMMAND)
    message(WARNING "$(SPELL_COMMAND) requested but executable not found")
    set(SPELL_COMMAND echo CACHE STRING "Spell checker to use not found" FORCE)
endif()

add_custom_target(
    spell-check
    COMMAND "${CMAKE_COMMAND}"
    -D "SPELL_COMMAND=${SPELL_COMMAND}"
    -P "${PROJECT_SOURCE_DIR}/cmake/spell.cmake"
    WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}"
    COMMENT "Checking spelling"
    VERBATIM
)

add_custom_target(
    spell-fix
    COMMAND "${CMAKE_COMMAND}"
    -D "SPELL_COMMAND=${SPELL_COMMAND}"
    -D FIX=YES
    -P "${PROJECT_SOURCE_DIR}/cmake/spell.cmake"
    WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}"
    COMMENT "Fixing spelling errors"
    VERBATIM
)
