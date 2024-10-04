#!/bin/bash
set -e

# Установите необходимые зависимости
/opt/python/cp39-cp39/bin/pip install -r /io/requirements.txt || true

# Соберите wheel-файлы для всех поддерживаемых версий Python
for PYBIN in /opt/python/*/bin; do
    "${PYBIN}/pip" wheel /io/ -w /io/wheelhouse/
done

# Исправьте wheel-файлы для совместимости с manylinux
for whl in /io/wheelhouse/*.whl; do
    auditwheel repair "$whl" -w /io/wheelhouse/
done

# Удалите оригинальные wheel-файлы, которые не совместимы с manylinux
rm /io/wheelhouse/*-linux_*.whl
