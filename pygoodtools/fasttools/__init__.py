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
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
"""
This module initializes and exposes various components of the `pygoodtools` package.

Modules:
    - command: Contains the Command class.
    - factory: Contains the CallbackFactory class.
    - functor: Contains the F class.
    - mediator: Contains the Mediator class.
    - meta: Contains the Meta class.
    - observer: Contains the Observer and Subject classes.
    - singleton: Contains the Singleton class.
    - smart_ptr: Contains the SmartPointer class.
    - time_ptr: Contains the TimeitPtr class.
    - visitor: Contains the Visitor class.

Exposed Classes:
    - pyGTCommand: Alias for Command class.
    - pyGTCallback: Alias for CallbackFactory class.
    - pyGTFunctor: Alias for F class.
    - pyGTSingleton: Alias for Singleton class.
    - pyGTSmartPointer: Alias for SmartPointer class.
    - pyGTTimeitPtr: Alias for TimeitPtr class.
    - pyGTVisitor: Alias for Visitor class.
    - pyGTMediator: Alias for Mediator class.
    - pyGTMeta: Alias for Meta class.
    - pyGTSubject: Alias for Subject class.
    - pyGTObserver: Alias for Observer class.
"""



from .cache import lru_cache
from .class_method_checked import ensure_method_exists
from .context_manager import contextmanager
from .log_calls import log_calls
from .memoization import memoize
from .timeit import timeit
from .singleton import singleton
from .type_checked import is_type
from .retry import retry


__all__ = [
    'lru_cache',
    'ensure_method_exists',
    'contextmanager',
    'log_calls',
    'memoize',
    'timeit',
    'singleton',
    'is_type',
    'retry',
]
