def function_with_uncommon_error(x):
    try:
        if not isinstance(x,(int,float)):
            raise TypeError("Invalid input type. Input must be a number.")
        result = 10 / x
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

# Example usage
result1 = function_with_uncommon_error(5)
print(f"Result 1: {result1}")

result2 = function_with_uncommon_error("abc")
print(f"Result 2: {result2}")

result3 = function_with_uncommon_error(0)
print(f"Result 3: {result3}")

result4 = function_with_uncommon_error(3.14)
print(f"Result 4: {result4}")
