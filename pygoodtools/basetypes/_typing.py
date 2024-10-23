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
This module defines two classes, `Void` and `Pointer`, which serve as base types for various operations.
Classes:
    Void:
        Methods:
            __init__(*args, **kwargs):
                Initialize the Void instance.
            __getattr__(name):
            __call__(*args, **kwargs):
            _void_method(*args, **kwargs):
            __repr__():
            __str__():
            __bool__():
            __eq__(other):
            __ne__(other):
            __len__():
            __contains__(item):
            __iter__():
            __getitem__(key):
            __setitem__(key, value):
            __delitem__(key):
            __add__(other):
            __sub__(other):
            __mul__(other):
            __truediv__(other):
            __floordiv__(other):
            __mod__(other):
            __pow__(other, modulo=None):
            __and__(other):
            __or__(other):
            __xor__(other):
            __invert__():
            __lshift__(other):
            __rshift__(other):
            __lt__(other):
            __le__(other):
            __gt__(other):
            __ge__(other):
    Pointer:
        Attributes:
            obj (object): The object to which the pointer points.
        Methods:
            __getattr__(name):
            __setattr__(name, value):
            __delattr__(name):
            __call__(*args, **kwargs):
            __repr__():
            __str__():
            __bool__():
            __eq__(other):
            __ne__(other):
            __len__():
            __contains__(item):
            __iter__():
            __getitem__(key):
            __setitem__(key, value):
            __delitem__(key):
            __add__(other):
            __sub__(other):
            __mul__(other):
            __truediv__(other):
            __floordiv__(other):
            __mod__(other):
            __pow__(other, modulo=None):
            __and__(other):
            __or__(other):
            __xor__(other):
            __invert__():
            __lshift__(other):
            __rshift__(other):
            __lt__(other):
            __le__(other):
            __gt__(other):
            __ge__(other):
"""

from typing import final



__all__ = [
    'Void', 
    'Pointer',
    'NULL',
    'Nullptr',
]

from pygoodtools.core import Base

@final
class Void(Base):
    """
    A class that represents a 'void' type, which essentially does nothing.
    It can be used as a placeholder or a default value where no action is required.
    """
    _instance = None
   
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Void, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, *args, **kwargs):
        pass

    def __getattr__(self, name):
        """
        Return a method that does nothing for any attribute access.
        """
        return self._void_method

    def __call__(self, *args, **kwargs):
        """
        Allow the instance to be called like a function, but do nothing.
        """
        return self

    def _void_method(self, *args, **kwargs):
        """
        A method that does nothing and returns the instance itself.
        """
        return self

    def __repr__(self):
        """
        Return a string representation of the instance.
        """
        return "<Void>"

    def __str__(self):
        """
        Return a string representation of the instance.
        """
        return "Void"

    def __bool__(self):
        """
        Always return False when evaluated in a boolean context.
        """
        return False

    def __eq__(self, other):
        """
        Check equality with another instance.
        """
        return isinstance(other, Void) or isinstance(other, NULL) or isinstance(other, Nullptr)

    def __ne__(self, other):
        """
        Check inequality with another instance.
        """
        return not self.__eq__(other)

    def __len__(self):
        """
        Always return 0 for the length.
        """
        return 0

    def __contains__(self, item):
        """
        Always return False for containment checks.
        """
        return False

    def __iter__(self):
        """
        Return an empty iterator.
        """
        return iter([])

    def __getitem__(self, key):
        """
        Return the instance itself for any key access.
        """
        return self

    def __setitem__(self, key, value):
        """
        Do nothing for item assignment.
        """
        pass

    def __delitem__(self, key):
        """
        Do nothing for item deletion.
        """
        pass

    def __add__(self, other):
        """
        Return the instance itself for addition.
        """
        return self

    def __sub__(self, other):
        """
        Return the instance itself for subtraction.
        """
        return self

    def __mul__(self, other):
        """
        Return the instance itself for multiplication.
        """
        return self

    def __truediv__(self, other):
        """
        Return the instance itself for true division.
        """
        return self

    def __floordiv__(self, other):
        """
        Return the instance itself for floor division.
        """
        return self

    def __mod__(self, other):
        """
        Return the instance itself for modulo operation.
        """
        return self

    def __pow__(self, other, modulo=None):
        """
        Return the instance itself for power operation.
        """
        return self

    def __and__(self, other):
        """
        Return the instance itself for bitwise AND operation.
        """
        return self

    def __or__(self, other):
        """
        Return the instance itself for bitwise OR operation.
        """
        return self

    def __xor__(self, other):
        """
        Return the instance itself for bitwise XOR operation.
        """
        return self

    def __invert__(self):
        """
        Return the instance itself for bitwise inversion.
        """
        return self

    def __lshift__(self, other):
        """
        Return the instance itself for left shift operation.
        """
        return self

    def __rshift__(self, other):
        """
        Return the instance itself for right shift operation.
        """
        return self

    def __lt__(self, other):
        """
        Always return False for less than comparison.
        """
        return False

    def __le__(self, other):
        """
        Always return False for less than or equal comparison.
        """
        return False

    def __gt__(self, other):
        """
        Always return False for greater than comparison.
        """
        return False

    def __ge__(self, other):
        """
        Always return False for greater than or equal comparison.
        """
        return False
    

@final
class Pointer(Base):
    """
    A class that represents a pointer to an object.
    It can be used to reference and manipulate the object it points to.
    """

    obj: object

    def __getattr__(self, name):
        """
        Delegate attribute access to the pointed object.
        """
        return getattr(self.ptr, name)

    def __setattr__(self, name, value):
        """
        Delegate attribute setting to the pointed object, except for 'ptr'.
        """
        if name == 'ptr':
            super().__setattr__(name, value)
        else:
            setattr(self.ptr, name, value)

    def __delattr__(self, name):
        """
        Delegate attribute deletion to the pointed object.
        """
        delattr(self.ptr, name)

    def __call__(self, *args, **kwargs):
        """
        Allow the instance to be called like a function, delegating to the pointed object.
        """
        return self.ptr(*args, **kwargs)

    def __repr__(self):
        """
        Return a string representation of the pointer.
        """
        return f"<Pointer to {repr(self.ptr)}>"

    def __str__(self):
        """
        Return a string representation of the pointed object.
        """
        return str(self.ptr)

    def __bool__(self):
        """
        Return the boolean value of the pointed object.
        """
        return bool(self.ptr)

    def __eq__(self, other):
        """
        Check equality with another pointer or object.
        """
        if isinstance(other, Pointer):
            return self.ptr == other.ptr
        return self.ptr == other

    def __ne__(self, other):
        """
        Check inequality with another pointer or object.
        """
        return not self.__eq__(other)

    def __len__(self):
        """
        Return the length of the pointed object if applicable.
        """
        return len(self.ptr)

    def __contains__(self, item):
        """
        Check if the item is in the pointed object if applicable.
        """
        return item in self.ptr

    def __iter__(self):
        """
        Return an iterator for the pointed object if applicable.
        """
        return iter(self.ptr)

    def __getitem__(self, key):
        """
        Get an item from the pointed object if applicable.
        """
        return self.ptr[key]

    def __setitem__(self, key, value):
        """
        Set an item in the pointed object if applicable.
        """
        self.ptr[key] = value

    def __delitem__(self, key):
        """
        Delete an item from the pointed object if applicable.
        """
        del self.ptr[key]

    def __add__(self, other):
        """
        Add another object to the pointed object if applicable.
        """
        return self.ptr + other

    def __sub__(self, other):
        """
        Subtract another object from the pointed object if applicable.
        """
        return self.ptr - other

    def __mul__(self, other):
        """
        Multiply the pointed object by another object if applicable.
        """
        return self.ptr * other

    def __truediv__(self, other):
        """
        Divide the pointed object by another object if applicable.
        """
        return self.ptr / other

    def __floordiv__(self, other):
        """
        Floor divide the pointed object by another object if applicable.
        """
        return self.ptr // other

    def __mod__(self, other):
        """
        Get the modulo of the pointed object by another object if applicable.
        """
        return self.ptr % other

    def __pow__(self, other, modulo=None):
        """
        Raise the pointed object to the power of another object if applicable.
        """
        return pow(self.ptr, other, modulo)

    def __and__(self, other):
        """
        Perform bitwise AND with the pointed object if applicable.
        """
        return self.ptr & other

    def __or__(self, other):
        """
        Perform bitwise OR with the pointed object if applicable.
        """
        return self.ptr | other

    def __xor__(self, other):
        """
        Perform bitwise XOR with the pointed object if applicable.
        """
        return self.ptr ^ other

    def __invert__(self):
        """
        Perform bitwise inversion on the pointed object if applicable.
        """
        return ~self.ptr

    def __lshift__(self, other):
        """
        Perform left shift on the pointed object if applicable.
        """
        return self.ptr << other

    def __rshift__(self, other):
        """
        Perform right shift on the pointed object if applicable.
        """
        return self.ptr >> other

    def __lt__(self, other):
        """
        Check if the pointed object is less than another object.
        """
        return self.ptr < other

    def __le__(self, other):
        """
        Check if the pointed object is less than or equal to another object.
        """
        return self.ptr <= other

    def __gt__(self, other):
        """
        Check if the pointed object is greater than another object.
        """
        return self.ptr > other

    def __ge__(self, other):
        """
        Check if the pointed object is greater than or equal to another object.
        """
        return self.ptr >= other
@final
class NULL(Base):
    """
    A class that represents a NULL value.
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(NULL, cls).__new__(cls)
        return cls._instance

    def __repr__(self):
        return "NULL()"

    def __str__(self):
        return "NULL"

    def __bool__(self):
        return False

    def __eq__(self, other):
        return isinstance(other, NULL) or isinstance(other, Void) or isinstance(other, Nullptr)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return self.__eq__(other)

    def __gt__(self, other):
        return False

    def __ge__(self, other):
        return self.__eq__(other)

    def __hash__(self):
        return hash(None)

@final
class Nullptr(Base):
    """
    A class that represents a nullptr value.
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Nullptr, cls).__new__(cls)
        return cls._instance

    def __repr__(self):
        return "nullptr()"

    def __str__(self):
        return "nullptr"

    def __bool__(self):
        return False

    def __eq__(self, other):
        return isinstance(other, Nullptr) or isinstance(other, Void) or isinstance(other, NULL)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return self.__eq__(other)

    def __gt__(self, other):
        return False

    def __ge__(self, other):
        return self.__eq__(other)

    def __hash__(self):
        return hash(None)

