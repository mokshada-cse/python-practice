# arithmetic.py
# Author: Mokshada
# Simple Python practice: basic arithmetic

# Multiply two numbers
def multiply(a, b):
    return a * b

# Divide two numbers
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Main program
if __name__ == "__main__":
    print("5 * 3 =", multiply(5, 3))
    print("10 / 2 =", divide(10, 2))
    print("10 / 0 =", divide(10, 0))
