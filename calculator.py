def calculator():
    print("=" * 30)
    print("   SIMPLE CALCULATOR")
    print("=" * 30)
    print("Operations: +  -  *  /")
    print("Type 'exit' to quit")
    print("=" * 30)

    while True:
        num1_input = input("\nEnter first number (or 'exit'): ")
        if num1_input.lower() == 'exit':
            print("Goodbye!")
            break

        operator = input("Enter operator (+, -, *, /): ")

        num2_input = input("Enter second number: ")

        try:
            num1 = float(num1_input)
            num2 = float(num2_input)
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                continue
            result = num1 / num2
        else:
            print("Error: Invalid operator. Use +, -, *, or /")
            continue

        print(f"\nResult: {num1} {operator} {num2} = {result}")


if __name__ == "__main__":
    calculator()