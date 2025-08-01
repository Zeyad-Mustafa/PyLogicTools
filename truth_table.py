"""
Simple truth table generator for PyLogicTools.
"""

from itertools import product
from .logic_gates import AND, OR, NOT, XOR


def generate_table(variables, expression_func):
    """
    Generate truth table for given variables and expression.
    
    Args:
        variables (list): Variable names like ['A', 'B']
        expression_func (function): Function that takes values and returns result
        
    Returns:
        list: Truth table rows
    """
    num_vars = len(variables)
    combinations = list(product([0, 1], repeat=num_vars))
    
    table = []
    for combo in combinations:
        result = expression_func(*combo)
        row = list(combo) + [int(result)]
        table.append(row)
    
    return table


def show_table(variables, table):
    """Display truth table in a nice format."""
    # Header
    header = " | ".join(variables) + " | Result"
    print(header)
    print("-" * len(header))
    
    # Rows
    for row in table:
        row_str = " | ".join(map(str, row))
        print(row_str)


def and_table(var_names=['A', 'B']):
    """Generate AND gate truth table."""
    table = generate_table(var_names, lambda a, b: AND(a, b))
    show_table(var_names, table)
    return table


def or_table(var_names=['A', 'B']):
    """Generate OR gate truth table."""
    table = generate_table(var_names, lambda a, b: OR(a, b))
    show_table(var_names, table)
    return table


def xor_table(var_names=['A', 'B']):
    """Generate XOR gate truth table."""
    table = generate_table(var_names, lambda a, b: XOR(a, b))
    show_table(var_names, table)
    return table


def not_table(var_names=['A']):
    """Generate NOT gate truth table."""
    table = generate_table(var_names, lambda a: NOT(a))
    show_table(var_names, table)
    return table


# Quick test
if __name__ == "__main__":
    print("AND Gate:")
    and_table()
    print("\nOR Gate:")
    or_table()
    print("\nXOR Gate:")
    xor_table()