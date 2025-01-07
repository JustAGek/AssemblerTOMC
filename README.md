# AssemblerTOMC

# Assembler: A Simple Assembly to Machine Code Converter

This project implements an assembler for a hypothetical assembly language. The assembler reads source code written in assembly and converts it into binary machine code, leveraging predefined opcode tables for the translation process.

---

## Features

- **Two-Pass Assembly Process**:
  - First Pass: Builds a symbol table to map labels to memory addresses.
  - Second Pass: Translates assembly instructions into binary machine code.
- **Supports Three Instruction Categories**:
  - MRI (Memory Reference Instructions)
  - RRI (Register Reference Instructions)
  - IOI (Input/Output Instructions)
- **Supports Directives**:
  - `ORG`: Sets the starting memory location.
  - `END`: Marks the end of the program.
- **Data Definition**:
  - `DEC`: Defines a decimal value.
  - `HEX`: Defines a hexadecimal value.
- **Handles Labels**: Maps symbolic labels to memory addresses.
- **Removes Comments**: Skips lines or parts of lines starting with `/`.

---

## Table of Contents

- [Setup](#setup)
- [Assembly Language Syntax](#assembly-language-syntax)
- [Workflow](#workflow)
- [File Structure](#file-structure)
- [Usage](#usage)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)

---

## Setup

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JustAGek/AssemblerTOMC.git
   cd AssemblerTOMC
   ```

2. Prepare input files:
   - Assembly source code file (`.asm` or `.S`).
   - Opcode table files (`mri.txt`, `rri.txt`, `ioi.txt`).

---

## Assembly Language Syntax

### Labels

- Labels are symbolic references to memory addresses.
- Must end with a comma (`,`).

**Example**:
```asm
START,
```

---

### Instructions

#### Memory Reference Instructions (MRI)

- Format: `<INSTRUCTION> <OPERAND>`
- Example: `ADD VALUE`

#### Register Reference Instructions (RRI)

- Format: `<INSTRUCTION>`
- Example: `CLA`

#### Input/Output Instructions (IOI)

- Format: `<INSTRUCTION>`
- Example: `INP`

---

### Directives

#### `ORG`
Sets the starting memory location.

**Example**:
```asm
ORG 100
```

#### `END`
Marks the end of the program.

**Example**:
```asm
END
```

---

### Data Definitions

- **DEC**: Defines a decimal value.
- **HEX**: Defines a hexadecimal value.

**Examples**:
```asm
VALUE DEC 10
CONST HEX F
```

---

## Workflow

1. **First Pass**:
   - Identifies labels and builds a symbol table.

2. **Second Pass**:
   - Converts assembly instructions into binary using opcode tables and the symbol table.

---

## File Structure

```
assembler/
│
├── assembler.py          # Assembler implementation
├── testcode.asm          # Sample assembly source code
├── mri.txt               # MRI opcode table
├── rri.txt               # RRI opcode table
├── ioi.txt               # IOI opcode table
├── testcode.mc           # Expected machine code output
└── README.md             # Documentation
```

---

## Usage

1. **Run the assembler**:
   ```bash
   python assembler.py
   ```

2. **Input and Output**:
   - Input: Assembly source code (`testcode.asm`) and opcode tables (`mri.txt`, `rri.txt`, `ioi.txt`).
   - Output: Binary machine code (`generated_output.mc`).

---

## Error Handling

The assembler reports errors for:

- Invalid instructions.
- Unsupported number formats.
- Missing or incorrect labels.

**Example**:
```
Error: Invalid instruction 'XYZ' at line 10
```

---

## Testing

1. The project includes a sample test case:
   - Input: `testcode.asm`.
   - Expected Output: `testcode.mc`.
change the file content according to your test cases

2. Run the assembler and verify the output:
   ```bash
   python testscript.py
   ```

3. The script automatically compares the generated output with the expected output and reports success or failure.

---
