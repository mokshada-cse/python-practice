# basics.py
# Author: Mokshada
# First Python practice file

# Function to greet a user
def greet(name):
    return "Hello, " + name + "!"

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Main part of the program
if __name__ == "__main__":
    user_name = "Mokshada"
    print(greet(user_name))
    print("5 + 3 =", add(5, 3))
    print("5 - 3 =", subtract(5, 3))
