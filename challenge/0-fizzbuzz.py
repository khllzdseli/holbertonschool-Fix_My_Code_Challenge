#!/usr/bin/env python3
"""
FizzBuzz Implementation - Fixed logical order for multiples of both 3 and 5
"""
import sys

def fizzbuzz(n):
    if n < 1: return
    output = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0: output.append("FizzBuzz")
        elif i % 3 == 0: output.append("Fizz")
        elif i % 5 == 0: output.append("Buzz")
        else: output.append(str(i))
    print(" ".join(output))

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Missing argument")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
        fizzbuzz(number)
    except ValueError:
        print("Argument must be an integer")
        sys.exit(1)
