from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract class
    """

    @abstractmethod
    def area(self):
        pass

    def description(self):
        print("This is a shape")


class Rectangle(Shape):
    """
    Child class implementing abstract method
    """

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of rectangle:", self.length * self.width)


class Circle(Shape):
    """
    Child class implementing abstract method
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of circle:", 3.14 * self.radius * self.radius)


rect = Rectangle(5, 4)
circle = Circle(3)

rect.description()
rect.area()

circle.description()
circle.area()


class Vehicle(ABC):
    """
    Another example of abstraction
    """

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with button")


car = Car()
bike = Bike()

car.start()
bike.start()

