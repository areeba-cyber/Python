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