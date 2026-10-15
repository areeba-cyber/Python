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


# Methods inside a class
# Methods are functions defined inside a class. They describe what an object can do.
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, my name is {self.name}")

student1 = Student("Areeba")
student1.introduce()
# Here, introduce() is a method, and student1.introduce() calls it.

# real-world example
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"New balance: {self.balance}")

account1 = BankAccount("Areeba", 1000)

account1.deposit(500)


# Inheritance
# Inheritance means one class can reuse the attributes and methods of another class.
# Think of it like this: a Dog is an Animal. A dog can use the general behavior of an animal, such as eating, while also having its own behavior, such as barking.

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()   # Inherited from Animal
dog.bark()  # Defined in Dog


# Encapsulation
# Encapsulation means keeping data and the methods that operate on that data together, while controlling how the data is accessed or changed.
# Imagine a bank account. You shouldn't be able to change your balance however you want. Instead, you should deposit or withdraw money through controlled methods.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)

print(account.get_balance())

# - self.__balance uses a double underscore to trigger Python's name mangling.
# - deposit() controls how the balance increases.
# - get_balance() provides a controlled way to read the balance.
# - account.__balance will not directly access the original attribute under that name.
# Python doesn't enforce absolute private access like some languages. Name mangling makes accidental access harder, but it is not a security boundary.


# Composition
# Composition means building a class using objects of other classes.
# Think about a car. A car has an engine. The Car class doesn't need to inherit from Engine because a car is not an engine; it has an engine.


class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car is ready to drive")


car = Car()
car.start_car()
