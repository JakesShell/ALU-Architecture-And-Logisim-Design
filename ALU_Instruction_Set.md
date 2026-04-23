# ALU Instruction Set

## Purpose

This file defines a simple instruction set for a basic ALU design intended for educational implementation in Logisim.

## Core Operation Categories

### Arithmetic Operations
- ADD
- SUB
- MUL
- DIV

### Bitwise Logic Operations
- AND
- OR
- XOR
- NOT

### Shift Operations
- SHL
- SHR

## Suggested Control Encoding

| Opcode | Operation | Description |
|--------|-----------|-------------|
| 0000 | ADD | Add Operand To Accumulator |
| 0001 | SUB | Subtract Operand From Accumulator |
| 0010 | MUL | Multiply Accumulator By Operand |
| 0011 | DIV | Divide Accumulator By Operand |
| 0100 | AND | Bitwise AND |
| 0101 | OR  | Bitwise OR |
| 0110 | XOR | Bitwise XOR |
| 0111 | NOT | Bitwise Inversion Of Accumulator |
| 1000 | SHL | Shift Left |
| 1001 | SHR | Shift Right |

## Register Intent

### Accumulator
Primary register used to store the active working result.

### Operand Register
Stores the value used as the second input for arithmetic and logic operations.

### Output Register
May be used to capture the final ALU result for observation or downstream flow.

## Design Notes

- Arithmetic operations should update the accumulator.
- Bitwise operations should operate on accumulator and operand inputs where relevant.
- Shift operations should define whether they are logical or arithmetic shifts.
- Division behavior should define how divide-by-zero is handled.
