def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {num / denom}"
    except ValueError:
        return "Error: Please enter numeric values only."

# Sample usage:
if __name__ == "__main__":
    print(safe_divide(10, 5))   # Expected output: The result of the division is 2.0
    print(safe_divide(10, 0))   # Expected output: Error: Cannot divide by zero.
    print(safe_divide('ten', 5))