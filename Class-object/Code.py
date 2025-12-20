class Student:
    def __init__(self, name, roll_no):
        self.name = name        # instance variable
        self.roll_no = roll_no  # instance variable


# Creating an Object
# Here, s1 is an object (instance) of the Student class.
# The constructor (__init__) is called automatically.

s1 = Student("Kahkashan", 14)

# Accessing Attributes
# Attributes are accessed using the object name and dot operator.

print("Student Name:", s1.name)
print("Roll Number:", s1.roll_no)

#  Defining and Accessing Methods
# Methods define the behavior of an object.

class StudentGreeting:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)


# Creating an object
s = StudentGreeting("Kahkashan")

# Calling a method
s.greet()


# self Keyword Explained
# 'self' refers to the current object.
# It is used to access instance variables and methods
# inside the class.

class DemoSelf:
    def __init__(self, value):
        self.value = value  # self.value is an instance variable

    def show(self):
        print("Value is:", self.value)


obj = DemoSelf(10)
obj.show()


#  Instance Variables vs Class Variables
class StudentDetails:
    college = "IIT Madras"   # class variable (shared)

    def __init__(self, name):
        self.name = name         # instance variable (object-specific)

    def display(self):
        print("Name:", self.name)
        print("College:", StudentDetails.college)


# Creating multiple objects
s1 = StudentDetails("Kahkashan")
s2 = StudentDetails("Ayesha")

s1.display()
s2.display()


"""
Key Points:
- Constructor initializes object data
- Objects are instances of a class
- self refers to the current object
- Instance variables are unique to each object
- Class variables are shared among all objects
"""
