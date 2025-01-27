def format_string(name, age):
    # Create a formatted string using f-strings.
    print(f"My name is {name} and I am {age} years old")
    # Args:
    # name (str): Person's name
name = "Emanuel"
    # age (int): Person's age
age = 25
    # Returns:
    # str: Formatted string
format_string(name, age)

pass

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    number = 15
    if number > 10:
        return("Greater")
    elif number < 10:
        return("Lesser")
    else:
        return("Equal")
number = 15
result = conditional_check(number)
print(result)

pass

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

result = loop_sum(5)
print("The sum of numbers from 1 to 5 is:", result)

pass

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    total = sum(numbers)  
    maximum = max(numbers) 
    minimum = min(numbers)  
    return total, maximum, minimum  

# Example list
numbers = [4, 7, 1, 9, 3]
result = list_operations(numbers)
print("Sum:", result[0])
print("Max:", result[1])
print("Min:", result[2])

pass

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    return [name for name, score in students_dict.items() if score > 80]

students_dict = {
    "Emma": 86,
    "Juma": 75,
    "Cherlie": 95,
    "Francais": 66,
    "John": 89
}

result = dict_operations(students_dict)
print("Students with scores above 80:", result)

pass

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

list1 = [1, 2, 3]
list2 = [2, 3, 4]
result = set_operations(list1, list2)
print(set(list1).intersection(list2))

pass

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    operations = {
        "addition": a + b,  
        "subtraction": a - b,  
        "multiplication": a * b,  
        "division": a / b if b != 0 else "Error: Division by zero",
        "modulus": a % b if b != 0 else "Error: Division by zero"
    }
    return operations 

a = 20
b = 4
result = arithmetic_ops(a, b)
print("arithmetic operation:", result)

pass

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    operations = {
        "and": x and y,  # Logical AND: True if both x and y are True
        "or": x or y,  # Logical OR: True if either x or y is True
        "not_x": not x,  # Logical NOT: Inverts the value of x
        "not_y": not y  # Logical NOT: Inverts the value of y
    }
    return operations  # Return the dictionary with results

x = True
y = False

result = logical_ops(x, y)
print("Logical operations results:", result)

pass

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    operations = {
        "and": a & b,  
        "or": a | b,   
        "xor": a ^ b, 
        "not_a": ~a,
        "not_b": ~b,
        "a_left_shift": a << 1,
        "b_left_shift": b << 1,
        "a_right_shift": a >> 1,
        "b_right_shift": b >> 1
    }
    return operations

a = 5  # Binary: 0101
b = 3  # Binary: 0011

result = bitwise_ops(a, b)
print("Bitwise operations results:", result)

pass