## 1. What is Inheritance?

Inheritance is one of the core principles of Object-Oriented Programming.
It allows a **class (child class)** to acquire the **properties and methods of another class (parent class)**.

In simple terms:
> Inheritance allows code reuse by creating new classes from existing ones.

---

## 2. Why Inheritance is Needed

Inheritance helps to:
- Reuse existing code
- Reduce code duplication
- Improve code organization
- Represent real-world relationships
- Make programs easier to maintain and extend

---

## 3. Basic Terminology

- **Parent Class / Base Class**: The class whose properties are inherited
- **Child Class / Derived Class**: The class that inherits from another class
- **Reusability**: Using parent class code in child class

---

## 4. Syntax of Inheritance in Python

```python
class Parent:
    pass

class Child(Parent):
    pass
```
* Child inherits from Parent
* Child can access all public and protected members of Parent

## Example of Inheritance
```class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")
```
## 6. Types of Inheritance

Python supports the following types of inheritance:

(a) Single Inheritance

(b) Multiple Inheritance

(c) Multilevel Inheritance

(d) Hierarchical Inheritance

(e) Hybrid Inheritance
