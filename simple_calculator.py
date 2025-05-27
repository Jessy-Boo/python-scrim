#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: ./simple_calculator.py <number1> <operator> <number2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        operator = sys.argv[2]
        num2 = float(sys.argv[3])
    except ValueError:
        print("Error: Invalid number input. Please provide valid numbers.")
        sys.exit(1)

    result = 0
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero.")
            sys.exit(1)
        result = num1 / num2
    else:
        print(f"Error: Invalid operator '{operator}'. Supported operators are +, -, *, /")
        sys.exit(1)

    print(result)

if __name__ == "__main__":
    main()
