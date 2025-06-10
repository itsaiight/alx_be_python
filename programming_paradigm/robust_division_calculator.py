def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        return num / denom
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"