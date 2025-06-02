def perform_operation(num1, num2, operation):
    """
    The function should execute arithmetic operations on two numbers based on the specified operation.
    
    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').
    
    Returns:
    int, float: The result of the arithmetic operation.
    
    Raises:
    ValueError: If an unsupported operation is specified or if division by zero is attempted.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError(f"Unsupported operation: {operation}")
