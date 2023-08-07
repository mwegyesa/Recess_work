
             #PYTHON REGULAR EXPRESSIONS
"""Regex (regular expressions) in Python allow you to work with patterns in strings, making it easier to search, 
match, and manipulate text. Python's re module provides functions to work with regular expressions.

Here's a basic overview of some common functions and syntax in Python's re module:

re.search(pattern, string): Searches for the first occurrence of the pattern in the given string and
 returns a match object if found. If no match is found, it returns None.

re.match(pattern, string): Similar to re.search(), but it only matches at the beginning of the string.

re.findall(pattern, string): Returns all non-overlapping occurrences of the pattern in the string as a list.

re.finditer(pattern, string): Returns an iterator yielding match objects for all occurrences of the pattern in the string.

re.sub(pattern, replacement, string): Replaces all occurrences of the pattern in the string with the replacement string.

re.split(pattern, string): Splits the string by the occurrences of the pattern and returns a list of substrings.

The pattern argument in these functions is the regular expression you want to use. Regular
 expressions consist of special characters and rules that describe the pattern you want to match. For example:

. matches any character except a newline.
* matches zero or more occurrences of the preceding element.
+ matches one or more occurrences of the preceding element.
\d matches any digit (0-9).
\w matches any alphanumeric character and underscore.
[] defines a character class, e.g., [a-z] matches any lowercase letter.
() defines a group."""    


              #PASSWORD VALIDATION USING REGEX
import re

def is_valid_password(password):
    # Define the regex pattern for password validation
    # (?=.*[A-Z]) - At least one uppercase letter
    # (?=.*[a-z]) - At least one lowercase letter
    # (?=.*\d)    - At least one digit
    # (?=.*[!@#$%^&*]) - At least one special character
    # .{8,}      - At least 8 characters long
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$"

    # Check if the password matches the regex pattern
    if re.match(pattern, password):
        return True
    else:
        return False

# Test cases
password1 = "#Mwegyesa@1"
password2 = "Saul123"
password3 = "SaulMwegyesa"  # Missing special character

print(is_valid_password(password1)) 
print(is_valid_password(password2))  
print(is_valid_password(password3))  


              #GENERATORS IN PYTHON
"""In Python, a generator is a type of iterable, like a list or a tuple, but it does not store all the 
values in memory at once. Instead, it generates the values on-the-fly as you iterate over it, which 
makes it memory-efficient and suitable for working with large datasets or infinite sequences.

Generators are created using functions that contain one or more yield statements. 
When a function with a yield statement is called, it does not execute the function body immediately. Instead,
it returns a generator object, and the function's state is saved. When you iterate over the generator
(using a loop or built-in functions like next()), the function body is executed until it
reaches the yield statement. The value after the yield is returned as the current item of 
the iteration, and the function's state is saved again. This process continues
each time the generator is iterated.

"""

     #USING GENERATOR FUNCTION TO YIELD FACTORIAL OF FIRST 6 INTEGERS
import math

def factorial_generator(n):
    for num in range(1, n+1):
        yield math.factorial(num)

# Using the generator to print factorial of first 6 numbers
gen = factorial_generator(6)

for factorial in gen:
    print(factorial)

                      #ITERATORS IN PYTHON
"""In Python, an iterator is an object that implements two methods:
__iter__() and __next__(). It allows you to traverse through a sequence of elements, like
a list or a string, one item at a time, without the need to know the underlying structure of the sequence.

Here's a brief explanation of each method:

__iter__(): This method returns the iterator object itself. It is called when you create
an iterator using the iter() function on an iterable object.

__next__(): This method returns the next item from the iterator.
It is called when you use the next() function on the iterator. 
When there are no more items to return, the method should raise the 
StopIteration exception to signal the end of the iteration."""

                  #USING AN ITERATOR TO PRINT THE SQUARES OF FIRST 100 INTEGERS
class SquaresIterator:
    def __init__(self):
        self.current = 1
        self.max_num = 100

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max_num:
            square = self.current ** 2
            self.current += 1
            return square
        else:
            raise StopIteration

# Creating the iterator
squares_iter = SquaresIterator()

# Using the iterator to print squares of the first 100 numbers
for square in squares_iter:
    print(square)


                     #DECORATORS IN PYTHON
                     
"""decorators are a powerful and flexible feature that allows you to modify or
extend the behavior of functions or methods. Decorators use a higher-order function 
(a function that takes another function as an argument) 
to wrap or modify the target function, thereby adding functionality to it
without changing its source code."""


       #DIVIDE BY TWO DECORATOR
def divide_by_two_decorator(func):
    def decorated_function():
        result = func()
        return result / 2
    return decorated_function

@divide_by_two_decorator
def multiply(a, b):
    return a * b

@divide_by_two_decorator
def square(x):
    return x ** 2

print(multiply(5, 6))  
print(square(4))       
