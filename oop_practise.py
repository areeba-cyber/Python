# Classes in OOP
Imagine you want to create a blueprint for students in a university.
Every student has:
- A name
- An age
- A method to introduce themselves
Instead of writing separate code for every student, you create one Student class and use it to create multiple objects.

class Student:
    name = "Areeba"
    age = 23

    def introduce(self):
        print("Hello, I am a student")


# object
# An object is an instance of a class. You create an object by calling the class name with parentheses.
class Student:
    name = "Areeba"

student1 = Student()

print(student1.name)
# Here, Student is the class, and student1 is an object created from that class.


# __init__()
# The __init__() method initializes an object's attributes when you create it. This lets you give different data to different objects.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Areeba", 23)
student2 = Student("Ali", 21)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)