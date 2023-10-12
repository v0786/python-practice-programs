def perform_arithmetic_operation(operator, num1, num2):
    """
    Perform arithmetic operations on two numbers.

    Args:
    operator (str): The arithmetic operator ('+', '-', '*', '/').
    num1 (float): The first number.
    num2 (float): The second number.

    Returns:
    float: The result of the arithmetic operation.
    """
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Error: Invalid operator"
    
    return result

#
