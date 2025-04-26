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