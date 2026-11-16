def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def format_number(num):
    # Display whole numbers without trailing '.0' (e.g., 10.0 -> 10)
    return int(num) if num.is_integer() else round(num, 6)

def calculator():
    print("=================================")
    print("    SIMPLE PYTHON CALCULATOR     ")
    print("=================================")

    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice. Please select a number between 1 and 5.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {format_number(num1)} + {format_number(num2)} = {format_number(result)}")

        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {format_number(num1)} - {format_number(num2)} = {format_number(result)}")

        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {format_number(num1)} * {format_number(num2)} = {format_number(result)}")

        elif choice == '4':
            result = divide(num1, num2)
            if result is None:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {format_number(num1)} / {format_number(num2)} = {format_number(result)}")

if __name__ == "__main__":
    calculator()