# PyLogicTools

A comprehensive Python library for logical operations, Boolean algebra, and propositional logic tools.

## 🚀 Features

- **Boolean Logic Operations**: Support for AND, OR, NOT, XOR, and other logical operations
- **Truth Table Generation**: Automatically generate truth tables for complex logical expressions
- **Logic Expression Parsing**: Parse and evaluate logical expressions from strings
- **Circuit Simulation**: Simulate digital logic circuits
- **Logic Simplification**: Simplify Boolean expressions using various algorithms
- **Educational Tools**: Perfect for learning and teaching digital logic concepts

## 📦 Installation

### From PyPI (recommended)
```bash
pip install pylogictools
```

### From Source
```bash
git clone https://github.com/Zeyad-Mustafa/PyLogicTools.git
cd PyLogicTools
pip install -e .
```

## 🔧 Quick Start

### Basic Logic Operations
```python
from pylogictools import LogicGate, TruthTable

# Create logic gates
and_gate = LogicGate.AND()
or_gate = LogicGate.OR()
not_gate = LogicGate.NOT()

# Perform operations
result = and_gate.evaluate(True, False)  # Returns False
print(f"True AND False = {result}")
```

### Truth Table Generation
```python 
from pylogictools import TruthTable

# Generate truth table for a complex expression
expression = "(A AND B) OR (NOT C)"
table = TruthTable.from_expression(expression)
table.display()
```

### Logic Expression Parsing
```python
from pylogictools import LogicParser

parser = LogicParser()
result = parser.evaluate("(True AND False) OR True")
print(f"Result: {result}")  # Result: True
```

## 📚 Documentation

### Core Classes

#### `LogicGate`
Represents basic logic gates and operations.

**Methods:**
- `AND(*inputs)` - Logical AND operation
- `OR(*inputs)` - Logical OR operation  
- `NOT(input)` - Logical NOT operation
- `XOR(*inputs)` - Logical XOR operation
- `NAND(*inputs)` - Logical NAND operation
- `NOR(*inputs)` - Logical NOR operation

#### `TruthTable`
Generate and display truth tables for logical expressions.

**Methods:**
- `from_expression(expression)` - Create table from string expression
- `from_variables(variables, expression_func)` - Create table from function
- `display()` - Print formatted truth table
- `to_csv(filename)` - Export table to CSV

#### `LogicParser`
Parse and evaluate logical expressions from strings.

**Methods:**
- `parse(expression)` - Parse expression into internal representation
- `evaluate(expression, variables=None)` - Evaluate expression with given variables
- `simplify(expression)` - Simplify Boolean expression

## 🎯 Examples

### Example 1: Digital Circuit Simulation
```python
from pylogictools import Circuit, LogicGate

# Create a simple circuit
circuit = Circuit()
circuit.add_gate("AND1", LogicGate.AND())
circuit.add_gate("OR1", LogicGate.OR())
circuit.add_gate("NOT1", LogicGate.NOT())

# Connect gates
circuit.connect("AND1.output", "OR1.input1")
circuit.connect("NOT1.output", "OR1.input2")

# Set inputs and run simulation
circuit.set_input("AND1.input1", True)
circuit.set_input("AND1.input2", False)
circuit.set_input("NOT1.input", False)

result = circuit.simulate()
print(f"Circuit output: {result}")
```

### Example 2: Boolean Expression Simplification
```python
from pylogictools import BooleanSimplifier

simplifier = BooleanSimplifier()
original = "(A AND B) OR (A AND NOT B)"
simplified = simplifier.simplify(original)
print(f"Original: {original}")
print(f"Simplified: {simplified}")  # Output: A
```

### Example 3: Educational Truth Table
```python
from pylogictools import TruthTable

# Create truth table for De Morgan's Law demonstration
expression1 = "NOT (A AND B)"
expression2 = "(NOT A) OR (NOT B)"

table1 = TruthTable.from_expression(expression1)
table2 = TruthTable.from_expression(expression2)

print("De Morgan's Law Verification:")
print("NOT (A AND B) ≡ (NOT A) OR (NOT B)")
print("\nTable 1:")
table1.display()
print("\nTable 2:")
table2.display()
```

## 🧪 Testing

Run the test suite:
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pylogictools

# Run specific test file
pytest tests/test_logic_gates.py
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup
```bash
# Clone the repository
git clone https://github.com/Zeyad-Mustafa/PyLogicTools.git
cd PyLogicTools

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"

# Run pre-commit hooks
pre-commit install
```

### Running Tests
```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=pylogictools --cov-report=html
```

## 📋 Requirements

- Python 3.7+
- NumPy (for numerical operations)
- Pandas (for truth table export)
- Click (for CLI interface)



## 👨‍💻 Author

**Zeyad Mustafa**
- GitHub: [@Zeyad-Mustafa](https://github.com/Zeyad-Mustafa)
- Email: [zeyad.uni@gmail.com](zeyad.uni@gmail.com)

## 🙏 Acknowledgments

- Inspired by digital logic design principles
- Built for educational and practical applications
- Thanks to the Python community for excellent tools and libraries

## 📈 Roadmap

- [ ] Add support for sequential logic (flip-flops, counters)
- [ ] Implement Karnaugh map generation and simplification
- [ ] Add GUI interface for visual circuit design
- [ ] Support for VHDL/Verilog export
- [ ] Integration with hardware simulation tools
- [ ] Advanced optimization algorithms


## ⭐ Show Your Support

If you found this project helpful, please give it a star on GitHub!

---

**Happy Logic Building! 🔧⚡**
