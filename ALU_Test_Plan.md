# ALU Test Plan

## Purpose

This document defines a simple validation plan for confirming ALU behavior during simulation.

## Test Categories

### Arithmetic Tests
- Add Two Positive Values
- Subtract A Smaller Value From A Larger Value
- Multiply Two Small Values
- Divide A Value By A Non-Zero Operand

### Logic Tests
- AND Two Bit Patterns
- OR Two Bit Patterns
- XOR Two Bit Patterns
- NOT The Accumulator Value

### Shift Tests
- Shift Left By One
- Shift Right By One

## Example Test Cases

| Operation | Input A | Input B | Expected Result |
|----------|---------|---------|-----------------|
| ADD | 5 | 3 | 8 |
| SUB | 9 | 4 | 5 |
| MUL | 3 | 2 | 6 |
| DIV | 8 | 2 | 4 |
| AND | 1100 | 1010 | 1000 |
| OR  | 1100 | 1010 | 1110 |
| XOR | 1100 | 1010 | 0110 |
| SHL | 0011 | - | 0110 |
| SHR | 1000 | - | 0100 |

## Validation Goals

- Confirm correct output for each opcode
- Confirm correct register behavior
- Confirm clean output selection through the multiplexer
- Confirm expected handling of invalid or edge-case inputs

## Future Expansion

When a Logisim circuit file is added, this plan should be expanded with:
- Per-subcircuit screenshots
- Step-by-step simulation captures
- Control-line verification
- Error case testing
