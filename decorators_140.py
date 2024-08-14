import time
from functools import wraps
import sys

# Adjust recursion limit and max string digits if needed
sys.setrecursionlimit(15000000)
sys.set_int_max_str_digits(0)

def memoize(func):
    """Decorator to cache the results of a function call."""
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper

def timing_decorator(func):
    """Decorator to measure the total execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        duration = end_time - start_time  # Calculate the duration
        return result, duration  # Return both the result and the duration
    return wrapper

@memoize
def lucas_number_recursive(n):
    """Calculate the Nth Lucas number using naive recursion."""
    # Base cases
    if n == 0:
        return 2
    elif n == 1:
        return 1

    # Recursive case
    return lucas_number_recursive(n - 1) + lucas_number_recursive(n - 2)

def calculate_lucas_number(n):
    """Calculate the Nth Lucas number and print the total time taken."""
    # Timing and calculation
    result, duration = timing_decorator(lucas_number_recursive)(n)
    print("Total time taken to compute requested Lucas number",n,f"is {duration:.8f} seconds")
    return result

# Example usage
calculate_lucas_number(139999)
calculate_lucas_number(140000)
