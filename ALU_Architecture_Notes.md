# ALU Architecture Notes

## High-Level Structure

A basic ALU design for Logisim should typically include:

- Input Buses
- Accumulator Register
- Operand Register
- Operation Select Control
- Arithmetic Subcircuits
- Logic Subcircuits
- Shift Subcircuits
- Output Selection Multiplexer
- Output Register

## Suggested Internal Blocks

### Arithmetic Unit
Handles:
- Addition
- Subtraction
- Multiplication
- Division

### Logic Unit
Handles:
- AND
- OR
- XOR
- NOT

### Shift Unit
Handles:
- Shift Left
- Shift Right

### Control Unit
Maps opcodes to subcircuit selection and output routing.

### Multiplexer Layer
Chooses which functional block drives the final output.

## Suggested Logisim Build Order

1. Build Input And Output Registers
2. Build Addition And Subtraction
3. Build Logic Operations
4. Build Shift Operations
5. Add Multiplexer-Based Output Selection
6. Connect Control Signals
7. Validate Each Operation One By One

## Implementation Note

If the full Logisim circuit is built later, this document should be updated with:
- Subcircuit names
- Bit widths
- Control line definitions
- Screenshots of the final design
