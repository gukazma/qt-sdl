set(TARGET_NAME DemoApp)

find_package(Qt5 COMPONENTS Core Widgets Gui OpenGL REQUIRED)
find_package(SDL2 REQUIRED CONFIG)
find_package(OpenGL REQUIRED)
find_package(GLEW REQUIRED)
find_package(glm REQUIRED)
find_package(PNG REQUIRED)
find_package(nlohmann_json CONFIG REQUIRED)


set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)


file(GLOB_RECURSE CPP_HEAD_FILES CONFIGURE_DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/*.h)
file(GLOB_RECURSE CPP_SOUCE_FILES CONFIGURE_DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp)
file(GLOB_RECURSE UI_SOUCE_FILES CONFIGURE_DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/*.ui)
set(QRC_FILE ${CMAKE_CURRENT_SOURCE_DIR}/QResources/resources.qrc)
set(APPRC_FILE ${CMAKE_CURRENT_SOURCE_DIR}/QResources/appicon.rc)
set(Translatefile ${CMAKE_CURRENT_SOURCE_DIR}/QResources/Translations/zh_CN.ts)


source_group(TREE "${CMAKE_CURRENT_SOURCE_DIR}" FILES ${CPP_HEAD_FILES} ${CPP_SOUCE_FILES})

add_executable(${TARGET_NAME} ${CPP_HEAD_FILES} ${CPP_SOUCE_FILES} ${UI_SOUCE_FILES}  ${QRC_FILE} ${APPRC_FILE} ${Translatefile})
set_target_properties(${TARGET_NAME} PROPERTIES FOLDER Apps)
target_link_libraries(${TARGET_NAME} PRIVATE
Qt5::Core
Qt5::Gui
Qt5::Widgets
Qt5::OpenGL
SDL2::SDL2main
SDL2::SDL2-static
GLEW::GLEW
glm::glm
PNG::PNG
nlohmann_json::nlohmann_json
)

if(MSVC)
message("Finding windeployqt")
find_program(DEPLOYQT_EXECUTABLE windeployqt)
add_custom_command(TARGET ${TARGET_NAME} POST_BUILD
  COMMAND ${DEPLOYQT_EXECUTABLE} ${CMAKE_BINARY_DIR}/bin/${TARGET_NAME}.exe
  COMMENT "Deploying qt dependencies after build..."
  WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
)

set_target_properties(${TARGET_NAME} PROPERTIES
LINK_FLAGS_RELEASE "/SUBSYSTEM:WINDOWS /ENTRY:mainCRTStartup"
)
endif()


find_program(LUPDATE_EXE lupdate)
add_custom_target(
      TranslateUpdate
      COMMAND ${LUPDATE_EXE} -recursive ./ -ts ./QResources/Translations/zh_CN.ts
      WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}
      VERBATIM)

find_program(LRELEASE_EXE lrelease)
add_custom_target(
      TranslateRelease
      COMMAND ${LRELEASE_EXE} ./QResources/Translations/zh_CN.ts
      WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}
      VERBATIM)

set_target_properties(TranslateUpdate PROPERTIES FOLDER Apps)
set_target_properties(TranslateRelease PROPERTIES FOLDER Apps)