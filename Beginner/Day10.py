def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def mult(a, b):
    return a * b

switcher = {
    "+": add,
    "-": sub,
    "/": div,
    "*": mult
}

def switch(operation, a, b):
    # Get the function corresponding to the operation
    func = switcher.get(operation)
    if func:
        # If the function exists, call it with the provided arguments
        return func(a, b)
    else:
        return "Invalid operation"

# Get user input for operation and numbers
operation = input("Choose operation (+, -, /, *): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Call the switch function to perform the operation
result = switch(operation, a, b)
print("Result:", result)
