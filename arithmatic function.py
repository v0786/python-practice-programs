def perform_arithmetic_operation():
    while True:
        # Get user input for the operation
        operation = input("Enter an arithmetic operation (+, -, *, /) or 'q' to quit: ")

        # Check if the user wants to quit
        if operation.lower() == 'q':
            print("Exiting the program.")
            break

        # Get user input for operands
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        # Perform the selected operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            continue

        # Display the result
        print(f"Result: {num1} {operation} {num2} = {result}")

# Call the function to start the program
perform_arithmetic_operation()
