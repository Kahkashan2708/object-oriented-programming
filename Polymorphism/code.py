# 1. Runtime Polymorphism (Method Overriding)
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()   # Same method call, different behavior

# 2. Polymorphism Using Inheritance

class Shape:
    def area(self):
        print("Area not defined")

class Rectangle(Shape):
    def area(self):
        print("Area of rectangle: length × width")

class Circle(Shape):
    def area(self):
        print("Area of circle: π × r²")


shapes = [Rectangle(), Circle()]

for shape in shapes:
    shape.area()


# 3. Duck Typing (Polymorphism Without Inheritance)

class Bird:
    def fly(self):
        print("Bird flies")

class Airplane:
    def fly(self):
        print("Airplane flies")

def make_it_fly(obj):
    obj.fly()

make_it_fly(Bird())
make_it_fly(Airplane())


# 4. Method Overloading (Python Style)
# Python does not support traditional method overloading.
# It is achieved using default or variable-length arguments.

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()

print("Add two numbers:", calc.add(10, 20))
print("Add three numbers:", calc.add(10, 20, 30))

# 5. Operator Overloading

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def display(self):
        print(f"({self.x}, {self.y})")


p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2   # Uses __add__ method

p3.display()

