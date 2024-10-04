cmake_minimum_required(VERSION 3.12)
project(PyGoodTools)

set(CMAKE_CXX_STANDARD 14)

# Добавить pybind11
add_subdirectory(pybind11)

# Указать директории с заголовочными файлами
include_directories(include)

# Создать фиктивный файл для компиляции библиотеки
file(WRITE ${CMAKE_BINARY_DIR}/dummy.cpp "")

# Создать библиотеку из исходников C++
add_library(PyGoodTools SHARED ${CMAKE_BINARY_DIR}/dummy.cpp)

# Создать обертку для Python
pybind11_add_module(gt_wrapper scripts/bindings.cpp)

# Линковка обертки с библиотекой
target_link_libraries(gt_wrapper PRIVATE PyGoodTools)