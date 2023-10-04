# Vulnerable Python Code with Unit Tests

# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

# Function to find the maximum element in a list
def find_max(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Unit tests for the functions
def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(-1) == 1  # Vulnerability: Negative input is not handled

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 0) == 2  # Vulnerability: Division by zero is not caught

def test_find_max():
    assert find_max([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 9
    assert find_max([]) == 0  # Vulnerability: Incorrect default value

if __name__ == "__main__":
    test_factorial()
    test_divide()
    test_find_max()
    print("All tests passed.")
