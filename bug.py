def function_with_uncommon_error(x):
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Invalid input type.")
        return None

# This will raise a TypeError since it's trying to divide an integer by a string
result = function_with_uncommon_error("abc")
print(result)