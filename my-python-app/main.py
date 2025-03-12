# my-python-app/main.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Math Operations")
    print(f"Addition: 5 + 3 = {add(5, 3)}")
    print(f"Subtraction: 5 - 3 = {subtract(5, 3)}")
    print(f"Multiplication: 5 * 3 = {multiply(5, 3)}")
    print(f"Division: 6 / 2 = {divide(6, 2)}")

