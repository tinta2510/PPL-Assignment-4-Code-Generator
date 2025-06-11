# PPL-Assignment-4-MiniGo-Code-Generator
## Overview
This is the fourth and final assignment for the **Principles of Programming Languages (CO3005)** course at HCMC University of Technology (VNU-HCM). In this stage, we implement a **code generation phase** for the MiniGo language.

The objective is to generate **Jasmin assembly code** from the **AST (Abstract Syntax Tree)** created in Assignment 2. This Jasmin code is then compiled into **Java bytecode** that can be executed on a **Java Virtual Machine (JVM)**, forming the final component of a MiniGo compiler.

## Project Context
This assignment completes the MiniGo compiler pipeline:
- [Assignment 1 – Lexer & Recognizer](https://github.com/tinta2510/PPL-Assignment-1-MiniGo-Lexer-and-Recognizer)
- [Assignment 2 – AST Generation](https://github.com/tinta2510/PPL-Assignment-2-MiniGo-AST-Generation)
- [Assignment 3 – Static Checker](https://github.com/tinta2510/PPL-Assignment-3-MiniGo-Static-Checker)

## Environment Setup
Refer to the Environment Setup section in the [Assignment 1](https://github.com/tinta2510/PPL-Assignment-1-MiniGo-Lexer-and-Recognizer).

## Project Files
- `CodeGenerator.py`: Main file responsible for traversing AST and producing Jasmin code.
- `Emitter.py`: Helper class for emitting Jasmin instructions.
- `CodeGenSuite.py`: Contains 100 test cases to verify the correctness of code generation.

## Features
- Generation of Jasmin code for:
  - Variable/constant/function declarations
  - Control flow: `if`, `for`, `break`, `continue`
  - Function/method calls and returns
  - Struct and interface operations
- Final output: `.j` files converted to JVM `.class` files that run using `java`.
- Main class always named `MiniGoClass`.
- Semantic validation assumed completed in Assignment 3.
- Note: `for-each` loop is not supported in test cases.

## Usage
1. Generate Jasmin code using your code generator.
2. Use `jasmin.jar` to compile `.j` files:
   ```bash
   java -jar jasmin.jar MiniGoClass.j
    ```
3. Run the resulting bytecode with:
    ```bash
    java MiniGoClass
    ```