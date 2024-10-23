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
This module defines a metaclass `Meta` and a base class `Base` that utilizes the metaclass.

Classes:
    Meta: A metaclass that adds a `registry` attribute to the class.
    Base: A base class that registers its subclasses in the `registry` attribute.

Metaclass `Meta`:
    Methods:
        __new__(cls, name, bases, attrs):
            Creates a new class and adds a `registry` attribute to it.

Base class `Base`:
    Methods:
        __init_subclass__(cls, **kwargs):
            Initializes the subclass and registers it in the `registry` attribute.
"""


class Meta(type):
    """
    Metaclass that adds a `registry` attribute to the class.
    The `registry` attribute is a dictionary that stores the class name as the key
    and the class itself as the value.
    """

    def __new__(cls, name, bases, attrs):
        """
        Create a new class and add a `registry` attribute to it.

        Args:
            name (str): The name of the new class.
            bases (tuple): The base classes of the new class.
            attrs (dict): The attributes of the new class.

        Returns:
            type: The newly created class with a `registry` attribute.
        """
        new_class = super().__new__(cls, name, bases, attrs)
        new_class.registry = {}
        return new_class

    def register(cls, subclass):
        """
        Register a subclass in the registry.

        Args:
            subclass (type): The subclass to register.
        """
        cls.registry[subclass.__name__] = subclass

    def get_subclass(cls, name):
        """
        Get a subclass by name from the registry.

        Args:
            name (str): The name of the subclass.

        Returns:
            type: The subclass with the given name.
        """
        return cls.registry.get(name)


class Base(metaclass=Meta):
    """
    Base class that registers its subclasses in the `registry` attribute.
    """

    def __init_subclass__(cls, **kwargs):
        """
        Initialize the subclass and register it in the `registry` attribute.

        Args:
            **kwargs: Additional keyword arguments.
        """
        super().__init_subclass__(**kwargs)
        cls.registry[cls.__name__] = cls

    @classmethod
    def get_registered_subclasses(cls):
        """
        Get all registered subclasses.

        Returns:
            dict: A dictionary of registered subclasses.
        """
        return cls.registry
