"""
Number system conversions for PyLogicTools.
Convert between binary, decimal, and hexadecimal.
"""


def decimal_to_binary(decimal):
    """Convert decimal to binary string."""
    if decimal == 0:
        return "0"
    return bin(decimal)[2:]  # Remove '0b' prefix


def binary_to_decimal(binary):
    """Convert binary string to decimal."""
    return int(binary, 2)


def decimal_to_hex(decimal):
    """Convert decimal to hexadecimal string."""
    return hex(decimal)[2:].upper()  # Remove '0x' prefix, uppercase


def hex_to_decimal(hex_val):
    """Convert hexadecimal string to decimal."""
    return int(hex_val, 16)


def binary_to_hex(binary):
    """Convert binary to hexadecimal."""
    decimal = binary_to_decimal(binary)
    return decimal_to_hex(decimal)


def hex_to_binary(hex_val):
    """Convert hexadecimal to binary."""
    decimal = hex_to_decimal(hex_val)
    return decimal_to_binary(decimal)


def pad_binary(binary, bits=8):
    """Add leading zeros to binary string."""
    return binary.zfill(bits)


def show_conversions(number, base='decimal'):
    """Show number in all three systems."""
    if base == 'decimal':
        dec = number
        bin_val = decimal_to_binary(dec)
        hex_val = decimal_to_hex(dec)
    elif base == 'binary':
        bin_val = number
        dec = binary_to_decimal(bin_val)
        hex_val = decimal_to_hex(dec)
    elif base == 'hex':
        hex_val = number
        dec = hex_to_decimal(hex_val)
        bin_val = decimal_to_binary(dec)
    
    print(f"Decimal: {dec}")
    print(f"Binary:  {bin_val}")
    print(f"Hex:     {hex_val}")


# Quick test
if __name__ == "__main__":
    print("Converting 255:")
    show_conversions(255, 'decimal')
    
    print("\nConverting 1010:")
    show_conversions('1010', 'binary')
    
    print("\nConverting FF:")
    show_conversions('FF', 'hex')