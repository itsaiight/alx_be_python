def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        return num / denom
    except ValueError:
        return "Invalid input: Please enter numeric values for numerator and denominator."
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"