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