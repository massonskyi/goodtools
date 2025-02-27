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

import ctypes
from typing import Any
class SmartPointer(ctypes.Structure):
    """
    A smart pointer class.
    """
    _fields_ = [("obj", ctypes.py_object)]

    def __init__(self, obj: object, *args: Any, **kw: Any):
        """
        Initialize the smart pointer.
        :param obj: The object to be managed.
        """
        super().__init__(*args, **kw)
        self.obj = obj

    def __enter__(self):
        """
        Enter the context.
        :return: The object.
        """
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context.
        :param exc_type: The exception type.
        :param exc_val: The exception value.
        :param exc_tb: The exception traceback.
        :return: None.
        """
        self.release()

    def get(self):
        """
        Get the managed object.
        :return: The managed object.
        """
        return self.obj

    def set(self, obj: object):
        """
        Set a new object to be managed.
        :param obj: The new object.
        :return: None.
        """
        self.obj = obj

    def release(self):
        """
        Release the managed object.
        :return: None.
        """
        del self.obj