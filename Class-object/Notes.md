# Classes and Objects in Object-Oriented Programming (OOP)

## 1. Introduction

In Object-Oriented Programming, **classes and objects** are the foundation of the entire paradigm.  
They help model real-world entities by combining **data (attributes)** and **behavior (methods)** into a single unit.

---

## 2. What is a Class?

A **class** is a **blueprint or template** used to create objects.  
It defines:
- What data an object will have (attributes)
- What actions an object can perform (methods)

> A class does not occupy memory until an object is created from it.

### Real-World Analogy
- **Class** → Blueprint of a house
- **Object** → Actual house built from the blueprint

---

## 3. What is an Object?

An **object** is an **instance of a class**.  
It represents a real-world entity and occupies memory.

Each object:
- Has its own data
- Can call the methods defined in the class

---

## 4. Syntax of Class in Python

```python
class ClassName:
    def __init__(self):
        # constructor
        pass
```
* class → keyword to define a class

* __init__ → constructor, automatically called when object is created

* self → refers to the current object

## Constructor (__init__ Method)

A constructor is a special method used to initialize object data.
