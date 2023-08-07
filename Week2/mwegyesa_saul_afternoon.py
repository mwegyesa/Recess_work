"""""
EXCEPTION HANDLING
 An exception, is an event that occurs during the execution of a program, 
 disrupting the normal flow of instructions.
 Handling exceptions is essential for writing robust and reliable code, as it allows the program to
 continue running despite encountering errors.
      EXAMPLES OF PYTHON EXCEPTIONS
IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
ImportError: This exception is raised when an import statement fails to find or load a module.
SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
NameError: This exception is raised when a variable or function name is not found in the current scope.
IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
KeyError: This exception is raised when a key is not found in a dictionary.
ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
PermissionError: Raised when trying to access a resource without proper permissions.
StopIteration: Raised when the next() function in an iterator does not point to any object.
KeyboardInterrupt: Raised when the user interrupts the execution, usually by pressing Ctrl+C.
SystemExit: Raised when the sys.exit() function is called
"""
# Try and Except Statement
# Try: block: This is the part of the code where you put the statements that might raise an exception.
# Except: block: In this block, you specify the type of exception that you want to catch and handle.
# If an exception of the specified type occurs in the try: block, the code inside the except block will be executed.
# Example
try:
    # Code that may raise an exception
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

    # else block
"""else: block: This block is executed if no exceptions are raised in the try: block. It is generally used to 
define code that should run when there are no exceptions."""


# Example
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print("Result:", result)


divide_numbers(10, 2)  # Output: Result: 5.0
divide_numbers(10, 0)  # Output: Error: Cannot divide by zero.

# finally block
"""finally: block: This block is used to define code that will be executed regardless of 
whether an exception occurs or not."""


# Example
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    finally:
        print("Always execute...")


divide_numbers(10, 2)
# Output:
# Result: 5.0
# Always execute...

divide_numbers(10, 0)
# Output:
# Error: Cannot divide by zero.
# Always execute...

# custom Exceptions
"""Customized exceptions, also known as user-defined exceptions, allow you to create your
own exception classes in Python to handle specific exceptional
conditions that are unique to your application or domain."""


class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}")


def check_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print("Age is valid.")


try:
    check_age(25)
    check_age(150)
except InvalidAgeError as e:
    print(f"Invalid age encountered: {e}")

    # FILE HANDLING IN PYTHON
"""File handling  it refers to the process of
working with files on a computer's filesystem
In Python, file handling is performed using built-in functions and methods 
that allow you to interact with files. The key operations involved in file handling are:

1. Opening a File: To work with a file, you need to open it first. The open() function is used to open a
file and returns a file object that represents the opened file. You can specify the file path and the mode
(e.g., read, write, append, etc.) in the open() function.

2. Reading from a File: After opening a file in read mode, you can read data from it using methods like
read(), readline(), or readlines(). The read() method reads the entire content of the file, while readline()
reads one line at a time, and readlines() reads all lines into a list.

3. Writing to a File: When a file is opened in write or append mode, you can write data to it using the
write() method. The write() method allows you to write text or binary data to the file.

4. Closing a File: After you have finished working with a file, it is essential to close it using the 
close() method to release the system resources associated with the file. Alternatively, 
you can use a with statement to handle file opening and automatically close the file when the block is exited."""

# Example
# Example file path
file_path = "example.txt"

# Opening the file in write mode and writing data to it
with open(file_path, "w") as file:
    file.write("This is line 1.\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")

# Opening the same file in read mode and reading data from it
with open(file_path, "r") as file:
    content = file.read()
    print("Reading the entire content of the file:")
    print(content)

# Opening the file in read mode and reading data line by line
with open(file_path, "r") as file:
    lines = file.readlines()
    print("\nReading the file line by line:")
    for line in lines:
        print(line.strip())  # Stripping the newline character

# Opening the same file in append mode and adding more data
with open(file_path, "a") as file:
    file.write("This is line 4.\n")

# Opening the file in read mode and reading the updated content
with open(file_path, "r") as file:
    updated_content = file.read()
    print("\nReading the updated content of the file:")
    print(updated_content)

# Closing the file (not necessary when using 'with' statement)
# file.close()
