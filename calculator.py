#!/usr/bin/env python3
"""
Simple Calculator Application in Python
Supports basic arithmetic operations with a command-line interface
"""

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    """Raise x to the power of y"""
    return x ** y

def modulo(x, y):
    """Get remainder of x divided by y"""
    if y == 0:
        return "Error: Division by zero"
    return x % y

def sqrt(x):
    """Calculate square root of x"""
    if x < 0:
        return "Error: Cannot calculate square root of negative number"
    return x ** 0.5

def calculator():
    """Main calculator function with user interface"""
    print("=" * 50)
    print("        SIMPLE CALCULATOR (Python)")
    print("=" * 50)
    print("\nOperations available:")
    print("  +  : Addition")
    print("  -  : Subtraction")
    print("  *  : Multiplication")
    print("  /  : Division")
    print("  ** : Power/Exponentiation")
    print("  %  : Modulo (Remainder)")
    print("  √  : Square Root")
    print("  =  : Calculate result")
    print("  c  : Clear/New calculation")
    print("  q  : Quit")
    print("=" * 50)

    while True:
        try:
            # Get first number
            num1_input = input("\nEnter first number (or 'q' to quit): ").strip()
            
            if num1_input.lower() == 'q':
                print("Thank you for using the Calculator. Goodbye!")
                break
            
            if num1_input.lower() == 'c':
                continue
            
            num1 = float(num1_input)
            
            # Get operator
            operator = input("Enter operator (+, -, *, /, **, %, √): ").strip()
            
            if operator == '√':
                result = sqrt(num1)
                print(f"\n√{num1} = {result}")
                continue
            
            # Get second number
            num2_input = input("Enter second number: ").strip()
            num2 = float(num2_input)
            
            # Perform calculation
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            elif operator == '**':
                result = power(num1, num2)
            elif operator == '%':
                result = modulo(num1, num2)
            else:
                print("Invalid operator! Please use +, -, *, /, **, %, or √")
                continue
            
            # Display result
            print("\n" + "-" * 50)
            print(f"Result: {num1} {operator} {num2} = {result}")
            print("-" * 50)
            
            # Ask if user wants to continue
            again = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
            if again != 'y':
                print("Thank you for using the Calculator. Goodbye!")
                break
        
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

class AdvancedCalculator:
    """Advanced calculator class with history tracking"""
    
    def __init__(self):
        self.history = []
    
    def calculate(self, num1, operator, num2):
        """Perform calculation and store in history"""
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return None
            result = num1 / num2
        elif operator == '**':
            result = num1 ** num2
        elif operator == '%':
            if num2 == 0:
                return None
            result = num1 % num2
        else:
            return None
        
        self.history.append(f"{num1} {operator} {num2} = {result}")
        return result
    
    def show_history(self):
        """Display calculation history"""
        if not self.history:
            print("No history available.")
        else:
            print("\nCalculation History:")
            for i, item in enumerate(self.history, 1):
                print(f"{i}. {item}")
    
    def clear_history(self):
        """Clear calculation history"""
        self.history = []
        print("History cleared.")

if __name__ == "__main__":
    # Run the simple calculator
    calculator()
