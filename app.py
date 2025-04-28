# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize 
# these values via a constructor. Add a method display() that prints student details.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name {self.name} and Student Marks is {self.marks}.")

s1 = Student("Areeba", 99)
s1.display()


# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class 
# variable and a class method with cls to manage and display the count.


class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total {cls.count} objects created.")

c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()

Counter.show_count()


# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate 
# the class and access both from outside the class.


class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"The {self.brand} car is starting...")

car1 = Car("Toyota")
car1.start()

# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, 
# name) that allows changing the bank name. Show that it affects all instances.


class Bank:
    bank_name = "Habib Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
print(f"Bank 1 {b1.bank_name}")

b2 = Bank()
print(f"Bank 2 {b2.bank_name}")

Bank.change_bank_name("Meezan Bank")

print(f"Bank 1 {b1.bank_name}")
print(f"Bank 2 {b2.bank_name}")


# 5. Static Variables and Static Methods
# static methods ko hum bina instance k class k bahir call kr skty hen class k name s 
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or 
# instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
result = MathUtils.add(10, 8)
print(f"Sum of a + b = {result}.")

# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and 
# another message when it is destroyed (destructor).


class Logger:
    # Constructor automatically call hoty hen or y object k initial setup k lye hoty hen 
    def __init__(self):
        print("Logger object created...")

    # Destructor object k destroy hoty wqt call hota h or y object clean up memory release k lye use hota h 
    def __del__(self):
        print("Logger object destroyed!!!")

log1 = Logger()

del log1


# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary   # Protected variable
        self.__ssn = ssn        # Private variable

emp1 = Employee("Areeba", 50000, "123-450")

print(emp1.name)       # Public variable accessible hoga
print(emp1._salary)    # Protected variable accessible but warning type 
# print(emp1.__ssn)      # Private variable Error ayega
# print(emp1._Employee__ssn)  # Private variable ko aese access kr skty hen


# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject 
# field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name) # super method s parent class k initializer or method ko call krty hen child class m

teacher1 = Teacher("Ayat")
print(teacher1.name)

# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). 
# Inherit a class Rectangle that implements area().


from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(ABC):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    

# shape1 = Shape()
# print(shape1.area()) # print None

rec1 = Rectangle(5, 4)
print(f"Area of Rectangle is {rec1.area()}.")


# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method 
# bark() that prints a message including the dog's name.


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} ({self.breed}) is barking!!!")

dog1 = Dog("Tommy", "German Shepered")
dog1.bark()


# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method 
# increment_book_count() to increase the count when a new book is added.


class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
    
Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()

print(f"Total Book is {Book.total_books}")

# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) 
# that returns the Fahrenheit value.


class TempratureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
temp_in_celsius = 30
temp_in_fahrenheit = TempratureConverter.celsius_to_fahrenheit(temp_in_celsius)

print(f"{temp_in_celsius}°C is {temp_in_fahrenheit}°F")


# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine 
# object to the Car class during initialization. Access a method of the Engine class 
# via the Car class.


class Engine:
    def start(self):
        print("Engine is starting...")

class Car:
    def __init__(self, engine):
        self.engine = engine # engine class ka obj pass kiya

    def drive(self):
        print("Car is driving....")
        self.engine.start() # car k through Engine ka method call h rha h 

engine = Engine() # engine object

car = Car(engine) # car object m engine pass kiya 

car.drive()  # car ka method call kiya 


# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a 
# Department object store a reference to an Employee object that exists 
# independently of it.


class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def get_info(self):
        return f"Employee Name: {self.name} and Role: {self.role} "


class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee

    def department_info(self):
        print(f"Department: {self.name}")
        print(f"Employee: {self.employee.get_info()}")

employee1 = Employee("Areeba", "Labour")

depart = Department("sales", employee1)

depart.department_info()

# Step 2: Delete the department object
del depart

# Step 3: Check if employee1 still exists
print("\nAfter deleting Department:")
print(employee1.get_info())


# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.


class A:
    def show(self):
        print("Show method from class A.")

class B(A):
    def show(self):
        print("Show method from class B.")

class C(A):
    def show(self):
        print("Show method from class C.")

class D(B, C):
    pass

d = D()
d.show()

print(D.mro())  # MRO ----->  Method Resoulation Order


# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" 
# before a function executes. Apply it to a function say_hello().


def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello! This is me Areeba Hammad.")

say_hello()

# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method 
# returning "Hello from Decorator!". Apply it to a class Person.

def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Areeba Ahytisham")
print(p1.greet())
        

