# Operators are 
# Operator-Based Calculator


# This calculator supports the following operators:
# + : Addition
# - : Subtraction
# * : Multiplication
# / : Division

# Type 'exit' anytime to quit the program.



def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the quotient of two numbers, handling division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def calculator():
    """Main function to run the calculator."""
    while True:
        print("\n--- Simple Calculator ---\nThis calculator supports the following operators: \n+ : Addition\n- : Subtraction\n* : Multiplication\n/ : Division")

        # Take operator input
        operator = input("Enter an operator (+, -, *, /): ").strip()

        if operator.lower() == 'exit':
            print("Thank you for using the calculator. Goodbye!")
            break

        if operator not in ('+', '-', '*', '/'):
            print("Invalid operator! Please enter one of +, -, *, /.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        # Perform the selected operation
        if operator == '+':
            print(f"The result is: {add(num1, num2)}")
        elif operator == '-':
            print(f"The result is: {subtract(num1, num2)}")
        elif operator == '*':
            print(f"The result is: {multiply(num1, num2)}")
        elif operator == '/':
            print(f"The result is: {divide(num1, num2)}")


# Run the calculator
if __name__ == "__main__":
    calculator()
