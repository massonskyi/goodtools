# COPYRIGHT (c) 2024 Massonskyi
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTOR
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# COPYRIGHT (c) 2024 Massonskyi

"""
__goodtools__ package

__This package provides a collection of tools and utilities for various purposes.__

__Modules:__
- __core__: Contains core functionalities such as signals, slots, and base core.
    - __pyGTSignal__: Signal class for event handling.
    - __pyGTSlot__: Slot class for event handling.
    - __GTObject__: Base object class.

- __maps__: Provides various map implementations.
    - __unique_map__: Unique map implementation.
    - __map__: General map implementation.
    - __hash_map__: Hash map implementation.
    - __unordered_map__: Unordered map implementation.
    - __tree_map__: Tree map implementation.

- __gttypes__: Defines various data types used in the package.
    - __u8, u16, u32, u64__: Unsigned integer types.
    - __i8, i16, i32, i64__: Signed integer types.
    - __f8, f16, f32, f64__: Floating-point types.
    - __boolean__: Boolean type.
    - __char__: Character type.
    - __string__: String type.
    - __nullptr, NULL__: Null pointer types.
    - __void__: Void type.
"""

from .basetools import *
from .basetypes import *
from .core import *
from lib.goodtools.pygoodtools.fasttools import *


__docs__ = """
__goodtools__ package

__This package provides a collection of tools and utilities for various purposes.__

__Modules:__
- __core__: Contains core functionalities such as signals, slots, and base core.
    - __pyGTSignal__: Signal class for event handling.
    - __pyGTSlot__: Slot class for event handling.
    - __GTObject__: Base object class.

- __maps__: Provides various map implementations.
    - __unique_map__: Unique map implementation.
    - __map__: General map implementation.
    - __hash_map__: Hash map implementation.
    - __unordered_map__: Unordered map implementation.
    - __tree_map__: Tree map implementation.

- __gttypes__: Defines various data types used in the package.
    - __u8, u16, u32, u64__: Unsigned integer types.
    - __i8, i16, i32, i64__: Signed integer types.
    - __f8, f16, f32, f64__: Floating-point types.
    - __boolean__: Boolean type.
    - __char__: Character type.
    - __string__: String type.
    - __nullptr, NULL__: Null pointer types.
    - __void__: Void type.
"""
__version__ = "1.0.0"
__author__ = "Massonskyi"
__license__ = "MIT"