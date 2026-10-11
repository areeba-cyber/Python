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