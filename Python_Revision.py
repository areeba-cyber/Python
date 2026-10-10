# Variable 
# A variable is a name used to store a value in a program.
# (Think of a variable as a box 📦 that holds some information. You give the box a name so you can use its contents later.)

name = "Areeba"
age = 23
height = 5.7
print(name)
print(age)
print(height)


# Data types
# A data type tells Python what kind of value a variable stores.
# (For example, a person's age is a whole number, their name is text, and their height might be a decimal number. Python uses different data types to represent these values.)

Python has several built-in data types. Let's learn the most important ones with simple examples.
1. Integer (int)
Whole numbers without decimal points.
age = 23
marks = 90
temperature = -5
print(type(age))
Output: int

2. Float (float)
Numbers with decimal points.
height = 5.7
price = 99.50
print(type(height))
Output: float

3. String (str)
Text enclosed in single or double quotation marks.
name = "Areeba"
city = 'Okara'
print(type(name))
Output: str

4. Boolean (bool)
Represents only two values: True or False.
is_student = True
is_graduated = False
print(type(is_student))
Output: bool

5. List (list)
Stores multiple items in an ordered, changeable collection.
fruits = ["apple", "mango", "banana"]
print(fruits[0])
Output: apple

6. Tuple (tuple)
Stores multiple items in order, but you cannot change its items after creation.
coordinates = (10, 20)
print(type(coordinates))
Output: tuple

7. Set (set)
Stores unique items without guaranteeing a particular order.
numbers = {1, 2, 2, 3}
print(numbers)
Output: {1, 2, 3}

8. Dictionary (dict)
Stores information as key-value pairs.
student = {    "name": "Areeba",    "age": 23}
print(student["name"])
Output: Areeba

9. None (NoneType)
Represents the absence of a value.
result = None
print(type(result))
Output: NoneType


# String
# A string (str) is a sequence of characters used to store text in Python.
# For example, names, cities, emails, and sentences are strings.
name = "Areeba"
city = "Okara"
message = "I am learning Python"
print(name)
print(city)
print(message)

String indexing:
Each character in a string has a position called an index.
Python indexing starts at 0, not 1.
word = "PYTHON"
print(word[0])
print(word[2])
print(word[5])


# Lists, Tuples, Sets, and Dictionaries in Python 🐍
Feature	            List	Tuple	Set	                 Dictionary
Syntax	            []	    ()	    {}	                 {key: value}
Ordered	            Yes	    Yes	    No guaranteed order	 Yes
Changeable	        Yes	    No	    Yes	                 Yes
Allows duplicates	Yes	    Yes	    No	                 Keys must be unique
Access by index	    Yes	    Yes	    No	                 Access by key

A list stores multiple items in a single variable. Lists are ordered, changeable, and allow duplicate values.
A tuple is an ordered collection that cannot be changed after it is created. This property is called immutability.
A set is a collection of unique items. If you add the same value more than once, only one copy is kept.
A dictionary stores data as key-value pairs. Each key identifies its associated value.
# How all four work together
# List: several students
students = ["Ali", "Areeba", "Sara"]

# Tuple: fixed coordinates
location = (30.81, 73.45)

# Set: unique marks
marks = {80, 90, 80, 75}

# Dictionary: one student's details
student = {
    "name": "Areeba",
    "age": 23,
    "skills": ["Python", "React", "SQL"]
}


# If-Else Conditions
# In Python, if-else conditions are used to make decisions in your program. They allow your code to do different things depending on whether a condition is True or False.
marks = 75

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")


# For Loops and While Loops
# A for loop is used when you want to iterate over a sequence, such as a list, string, or range of numbers.
# A while loop repeats code as long as a condition is True.


# Functions in Python
# A function in Python is a reusable block of code that performs a specific task. You write the code once and can use it whenever you need it.
# For example, if you want to print "Hello, World!" many times, you can put that code inside a function instead of writing it repeatedly.
def greet():
    print("Hello, World!")
greet()

- def — tells Python you are defining a function.
- greet — the function's name.
- () — holds parameters if needed.
- : — starts the function body.
- print() — the task the function performs.
- greet() — calls the function to run its code.
Remember: defining a function does not execute it. You must call it.

# . Functions with parameters
def greet(name):
    print("Hello", name)
greet("Areeba")    

# The return statement
# The return statement sends a result back to the place where the function was called.
def add(a, b):
    return a + b
result = add(10, 20)
print(result)

print()	                                                               return
Displays a value on the screen.	                                       Sends a value back to the caller.
Does not automatically give the value back for further use.	           Allows the result to be reused.


# *args and **kwargs in Python 
# In Python, *args and **kwargs allow a function to accept a flexible number of arguments.

1. What is *args?
*args allows you to pass multiple positional arguments to a function without knowing in advance how many there will be.
# without args
def add(a, b):
    print(a + b)
add(10, 20)
# This function accepts only two arguments. If you pass three, it will raise an error.

# with *args
def add(*args):
    print(args)
add(10, 20, 30, 40)

2. What is **kwargs?
**kwargs allows you to pass multiple keyword arguments — arguments supplied using names.
def student(**kwargs):
    print(kwargs["name"])
    print(kwargs["age"])

student(name="Areeba", age=23)

*args
Positional arguments
- Collects values into a tuple.
- Arguments don't need names.

**Kwargs
Keyword arguments
- Collects values into a dictionary.
- Arguments have names.

# Real world example
def student_info(*students, **details):
    print("Students :", students)
    print("Details :", deatils)

student_info(
    "Areeba", "Ali", "Ahmed",
    age = 23,
    semester = 6
)


# Lambda Functions in Python 
# A lambda function is a small, anonymous function in Python that is written in a single expression.
# In simple words, a lambda function lets you write a short function in one line without using def.
Lambda function syntax
lambda arguments: expression

double = lambda x: x * 2
print(double(4))

# Lambda with if-else
check = lambda n: "Even" if n % 2 == 0 else "Odd"
print(check(4))
print(check(7))


# List and Dictionary Comprehensions
# List and dictionary comprehensions let you create lists and dictionaries in a shorter, cleaner way instead of writing multiple lines with loops.
numbers = [i for i in range(1, 6)]
print(numbers)


# Exception Handling in Python 
# Exception handling in Python means handling errors that occur while a program is running so that your program doesn't crash unexpectedly.
# For example, if you divide a number by zero, Python raises an error. Exception handling lets you handle that error gracefully.

try and except
We use try and except to handle exceptions.
- try: Contains the code that might cause an error.
- except: Runs if a matching error occurs.

Common types of exceptions
Exception	        Meaning	               Example
ZeroDivisionError	Dividing by zero	   10 / 0
ValueError	        Invalid value	       int("hello")
TypeError	        Incompatible types	   "5" + 5
IndexError	        Invalid list index	   [1, 2][5]
KeyError	        Missing dictionary key	{"name": "Ali"}["age"]
FileNotFoundError	File doesn't exist	    Opening a missing file



try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")


# The else block
The else block runs only when no exception occurs in the try block.
try:
    number = int(input("Enter a number: "))
    result = 10 / number

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Enter a valid number.")

else:
    print("Result:", result)


# The finally block
# The finally block runs whether an exception occurs or not.

# The raise keyword
The raise keyword lets you intentionally raise an exception when a condition is invalid.

age = -5
if age < 0:
    raise ValueError("Age cannot be negative.")

# complete example
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    result = num1 / num2

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError as error:
    print(error)

else:
    print("Result:", result)

finally:
    print("Calculator closed.")


# Modules in Python 
# A module in Python is a file containing Python code—such as functions, variables, and classes—that you can reuse in another Python file.
# Instead of writing all your code in one file, you can divide it into smaller, organized files.

Built-In module in python
math	       Mathematical operations
random	       Generate random values
datetime	   Work with dates and times
os	           Interact with the operating system
statistics     Calculate mean, median, and more
# entire module
import math
print(math.sqrt(16))

# import a specific function
from math import sqrt
print(sqrt(16))

# import with an alias
import math as m
print(m.sqrt(36))


# What is the difference between a module and a package?
These two terms are related but different.

Module
A single Python file, such as calculator.py.

Package
A way to organize related modules inside a directory. A regular Python package commonly contains an __init__.py file.

my_project/
    main.py
    utilities/
        __init__.py
        calculator.py
        greetings.py

Here, utilities is the package, while calculator.py and greetings.py are modules.


# pip?
Some modules are not included with Python. You can install external libraries using pip, Python's package installer.
python -m pip install numpy