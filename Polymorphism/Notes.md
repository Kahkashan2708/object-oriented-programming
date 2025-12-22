# Polymorphism in Object-Oriented Programming (OOP)

## 1. What is Polymorphism?

Polymorphism is one of the four fundamental principles of Object-Oriented Programming.
The word *polymorphism* means **“many forms.”**

In OOP, polymorphism allows **the same method or operation to behave differently for different objects**.

In simple terms:
> Polymorphism = One interface, multiple behaviors

---

## 2. Why Polymorphism is Needed

Polymorphism helps to:
- Write flexible and scalable code
- Reduce conditional logic
- Improve code readability
- Allow objects to behave differently using the same method name
- Support dynamic behavior at runtime

---

## 3. Real-World Analogy

Consider a word **“drive”**:
- A person drives a car
- A pilot drives a plane
- A manager drives a team

Same word, different actions — this is polymorphism.

---

## 4. Types of Polymorphism

There are two main types of polymorphism:

1. Compile-Time Polymorphism  
2. Run-Time Polymorphism  

---

## 5. Compile-Time Polymorphism

Compile-time polymorphism is achieved **before program execution**.
It is mainly implemented using:
- Method overloading
- Operator overloading

> Note: Python does not support traditional method overloading like C++ or Java.

---

## 6. Method Overloading (Python Style)

In Python, method overloading is achieved using:
- Default arguments
- Variable-length arguments

Example:
```python
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
```
---
## 7. Operator Overloading

Operator overloading allows operators to behave differently for different data types.

Example:
```python
print(10 + 20)      # Addition
print("Hello" + "World")  # String concatenation
```

## 8. Run-Time Polymorphism

Run-time polymorphism occurs during program execution.
It is achieved using:

* Method overriding

* Inheritance

## 9. Method Overriding and Polymorphism

Method overriding allows a child class to provide its own implementation of a parent class method.

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")
```

Calling the same method gives different output.

## 10. Polymorphism Using Inheritance
```python
class Cat(Animal):
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

Same method call → different behavior.

## 11. Polymorphism Without Inheritance (Duck Typing)

Python supports polymorphism even without inheritance.
This is called **duck typing**.

“If it looks like a duck and quacks like a duck, it is a duck.”

Example:

```python
class Bird:
    def fly(self):
        print("Bird flies")

class Airplane:
    def fly(self):
        print("Airplane flies")

def make_it_fly(obj):
    obj.fly()
```
## 12. Benefits of Polymorphism

* Code reusability

* Extensibility

* Cleaner code

* Loose coupling

* Better abstraction

---
## Difference Between Method Overloading and Method Overriding

| Feature            | Method Overloading        | Method Overriding          |
|--------------------|---------------------------|----------------------------|
| Happens in         | Same class                | Parent–child class         |
| Method name        | Same                      | Same                       |
| Parameters         | Different                 | Same                       |
| Binding time       | Compile-time              | Run-time                   |
---
