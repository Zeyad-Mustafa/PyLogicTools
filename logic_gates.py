"""
Basic logic gate operations for PyLogicTools.
Simple functions for AND, OR, NOT, XOR, NAND, and NOR operations.
"""

def AND(*inputs):
    """
    Performs logical AND operation on multiple inputs.
    
    Args:
        *inputs: Boolean values to AND together
        
    Returns:
        bool: True if all inputs are True, False otherwise
        
    Examples:
        >>> AND(True, True)
        True
        >>> AND(True, False)
        False
        >>> AND(True, True, True)
        True
    """
    if not inputs:
        return True  # Empty AND is True by convention
    
    return all(inputs)


def OR(*inputs):
    """
    Performs logical OR operation on multiple inputs.
    
    Args:
        *inputs: Boolean values to OR together
        
    Returns:
        bool: True if any input is True, False if all are False
        
    Examples:
        >>> OR(True, False)
        True
        >>> OR(False, False)
        False
        >>> OR(False, False, True)
        True
    """
    if not inputs:
        return False  # Empty OR is False by convention
    
    return any(inputs)


def NOT(input_val):
    """
    Performs logical NOT operation on a single input.
    
    Args:
        input_val (bool): Boolean value to invert
        
    Returns:
        bool: Opposite of input value
        
    Examples:
        >>> NOT(True)
        False
        >>> NOT(False)
        True
    """
    return not input_val


def XOR(*inputs):
    """
    Performs logical XOR (exclusive OR) operation.
    Returns True if odd number of inputs are True.
    
    Args:
        *inputs: Boolean values to XOR together
        
    Returns:
        bool: True if odd number of inputs are True
        
    Examples:
        >>> XOR(True, False)
        True
        >>> XOR(True, True)
        False
        >>> XOR(True, True, True)
        True
    """
    if not inputs:
        return False
    
    true_count = sum(inputs)
    return true_count % 2 == 1


def NAND(*inputs):
    """
    Performs logical NAND (NOT AND) operation.
    
    Args:
        *inputs: Boolean values
        
    Returns:
        bool: NOT of AND operation
        
    Examples:
        >>> NAND(True, True)
        False
        >>> NAND(True, False)
        True
    """
    return NOT(AND(*inputs))


def NOR(*inputs):
    """
    Performs logical NOR (NOT OR) operation.
    
    Args:
        *inputs: Boolean values
        
    Returns:
        bool: NOT of OR operation
        
    Examples:
        >>> NOR(False, False)
        True
        >>> NOR(True, False)
        False
    """
    return NOT(OR(*inputs))


def XNOR(*inputs):
    """
    Performs logical XNOR (NOT XOR) operation.
    
    Args:
        *inputs: Boolean values
        
    Returns:
        bool: NOT of XOR operation
        
    Examples:
        >>> XNOR(True, True)
        True
        >>> XNOR(True, False)
        False
    """
    return NOT(XOR(*inputs))


# Helper function for testing all gates
def test_all_gates():
    """
    Simple test function to verify all logic gates work correctly.
    """
    print("Testing Logic Gates:")
    print("-" * 20)
    
    # Test basic gates
    print(f"AND(True, True): {AND(True, True)}")
    print(f"AND(True, False): {AND(True, False)}")
    print(f"OR(True, False): {OR(True, False)}")
    print(f"OR(False, False): {OR(False, False)}")
    print(f"NOT(True): {NOT(True)}")
    print(f"NOT(False): {NOT(False)}")
    print(f"XOR(True, False): {XOR(True, False)}")
    print(f"XOR(True, True): {XOR(True, True)}")
    print(f"NAND(True, True): {NAND(True, True)}")
    print(f"NOR(False, False): {NOR(False, False)}")
    print(f"XNOR(True, True): {XNOR(True, True)}")


if __name__ == "__main__":
    # Run tests when file is executed directly
    test_all_gates()