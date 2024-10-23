"""
Модуль для настройки пакета 'pygoodtools' с использованием setuptools.
"""

import os
import re
import sys
import subprocess
import platform
from setuptools import find_packages, setup, Extension
from setuptools.command.build_ext import build_ext

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pygoodtools',
    version='0.5.1',
    packages=find_packages(),
    install_requires=[
        # Укажите зависимости вашего проекта здесь
        # Например: 'requests', 'numpy'
    ],
    entry_points={
        'console_scripts': [
            # Укажите консольные скрипты вашего проекта здесь
            # Например: 'goodtools=goodtools.cli:main'
        ],
    },
    author='Massonskyi',
    author_email='-',
    description='This script sets up the "goodtools" package using setuptools.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/massonskyi/goodtools',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    # ext_modules=[CMakeExtension('pygoodtools')],
    # cmdclass=dict(build_ext=CMakeBuild),
    zip_safe=False,
)