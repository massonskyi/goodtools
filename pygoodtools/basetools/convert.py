import ctypes

libc = ctypes.CDLL(None)

# Определение прототипов функций
libc.sprintf.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
libc.sprintf.restype = ctypes.c_int

libc.sscanf.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]
libc.sscanf.restype = ctypes.c_int

def int_to_hex(value: int) -> str:
    """
    Convert an integer value to a hexadecimal string.
    Args:
        value (int): The integer value to convert.
    Returns:
        str: The hexadecimal representation of the integer value.
    """
    hex_str = ctypes.create_string_buffer(12)
    libc.sprintf(hex_str, b"%X", value)
    return hex_str.value.decode("utf-8")

def hex_to_int(hex_str: str) -> int:
    """
    Convert a hexadecimal string to an integer value.
    Args:
        hex_str (str): The hexadecimal string to convert.
    Returns:
        int: The integer value of the hexadecimal string.
    """
    value = ctypes.c_int()
    libc.sscanf(hex_str.encode("utf-8"), b"%X", ctypes.byref(value))
    return value.value

def int_to_oct(value: int) -> str:
    """
    Convert an integer value to an octal string.
    Args:
        value (int): The integer value to convert.
    Returns:
        str: The octal representation of the integer value.
    """
    oct_str = ctypes.create_string_buffer(12)
    libc.sprintf(oct_str, b"%o", value)
    return oct_str.value.decode("utf-8")

def oct_to_int(oct_str: str) -> int:
    """
    Convert an octal string to an integer value.
    Args:
        oct_str (str): The octal string to convert.
    Returns:
        int: The integer value of the octal string.
    """
    value = ctypes.c_int()
    libc.sscanf(oct_str.encode("utf-8"), b"%o", ctypes.byref(value))
    return value.value

def int_to_bin(value: int) -> str:
    """
    Convert an integer value to a binary string.
    Args:
        value (int): The integer value to convert.
    Returns:
        str: The binary representation of the integer value.
    """
    bin_str = ctypes.create_string_buffer(34)  # 32 bits + '0b' + null terminator
    libc.sprintf(bin_str, b"%b", value)
    return bin_str.value.decode("utf-8")

def bin_to_int(bin_str: str) -> int:
    """
    Convert a binary string to an integer value.
    Args:
        bin_str (str): The binary string to convert.
    Returns:
        int: The integer value of the binary string.
    """
    value = ctypes.c_int()
    libc.sscanf(bin_str.encode("utf-8"), b"%b", ctypes.byref(value))
    return value.value

def float_to_str(value: float) -> str:
    """
    Convert a float value to a string.
    Args:
        value (float): The float value to convert.
    Returns:
        str: The string representation of the float value.
    """
    str_buffer = ctypes.create_string_buffer(64)  # Buffer size to hold the float string
    libc.sprintf(str_buffer, b"%f", value)
    return str_buffer.value.decode("utf-8")

def str_to_float(str_value: str) -> float:
    """
    Convert a string to a float value.
    Args:
        str_value (str): The string to convert.
    Returns:
        float: The float value of the string.
    """
    value = ctypes.c_double()
    libc.sscanf(str_value.encode("utf-8"), b"%lf", ctypes.byref(value))
    return value.value


def float_to_hex(value: float) -> str:
    """
    Convert a float value to a hexadecimal string.
    Args:
        value (float): The float value to convert.
    Returns:
        str: The hexadecimal representation of the float value.
    """
    hex_str = ctypes.create_string_buffer(64)
    libc.sprintf(hex_str, b"%a", value)
    return hex_str.value.decode("utf-8")

def float_to_bin(value: float) -> str:
    """
    Convert a float value to a binary string.
    Args:
        value (float): The float value to convert.
    Returns:
        str: The binary representation of the float value.
    """
    try:
        int_value = float_to_int(value)
    except OverflowError:
        return "inf"

    except ValueError:
        return "nan"

    except Exception:
        return "unknown"

    bin_str = ctypes.create_string_buffer(34)
    libc.sprintf(bin_str, b"%b", int_value)
    return bin_str.value.decode("utf-8")

def float_to_oct(value: float) -> str:
    """
    Convert a float value to an octal string.
    Args:
        value (float): The float value to convert.
    Returns:
        str: The octal representation of the float value.
    """
    try:
        int_value = float_to_int(value)
    except OverflowError:
        return "inf"

    except ValueError:
        return "nan"

    except Exception:
        return "unknown"
    oct_str = ctypes.create_string_buffer(22)
    libc.sprintf(oct_str, b"%o", int_value)
    return oct_str.value.decode("utf-8")

def float_to_int(value: float) -> int:
    """
    Convert a float value to an integer.
    Args:
        value (float): The float value to convert.
    Returns:
        int: The integer representation of the float value.
    """
    return int(value)

def str_to_hex(value: str) -> str:
    """
    Convert a string to a hexadecimal string.
    Args:
        value (str): The string to convert.
    Returns:
        str: The hexadecimal representation of the string.
    """
    try:
        int_value = str_to_int(value)
    except ValueError:
        return "nan"

    except Exception:
        return "unknown"
    hex_str = ctypes.create_string_buffer(12)
    libc.sprintf(hex_str, b"%X", int_value)
    return hex_str.value.decode("utf-8")

def str_to_bin(value: str) -> str:
    """
    Convert a string to a binary string.
    Args:
        value (str): The string to convert.
    Returns:
        str: The binary representation of the string.
    """
    try:
        int_value = str_to_int(value)
    except ValueError:
        return "nan"

    except Exception:
        return "unknown"
    bin_str = ctypes.create_string_buffer(34)
    libc.sprintf(bin_str, b"%b", int_value)
    return bin_str.value.decode("utf-8")

def str_to_oct(value: str) -> str:
    """
    Convert a string to an octal string.
    Args:
        value (str): The string to convert.
    Returns:
        str: The octal representation of the string.
    """
    try:
        int_value = str_to_int(value)
    except ValueError:
        return "nan"

    except Exception:
        return "unknown"
    oct_str = ctypes.create_string_buffer(12)
    libc.sprintf(oct_str, b"%o", int_value)
    return oct_str.value.decode("utf-8")

def str_to_int(value: str) -> int:
    """
    Convert a string to an integer.
    Args:
        value (str): The string to convert.
    Returns:
        int: The integer representation of the string.
    """
    return int(value)