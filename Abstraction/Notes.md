# Abstraction 

Abstraction is one of the four fundamental principles of Object-Oriented Programming.
It refers to **hiding implementation details and showing only essential features to the user**.

In simple terms:
> Abstraction focuses on *what an object does*, not *how it does it*.

---

## 2. Why Abstraction is Needed

Abstraction helps to:
- Reduce complexity
- Improve code readability
- Hide unnecessary implementation details
- Increase security
- Make systems easier to maintain and extend

---

## 3. Real-World Analogy

**Car Driving**
- You use steering, brake, and accelerator
- You do not know how the engine internally works

You interact with **what the car does**, not **how it works internally**.
This is abstraction.

---

## 4. How Abstraction is Achieved

In Python, abstraction is achieved using:
1. Abstract classes
2. Abstract methods

Python provides the **`abc` (Abstract Base Class)** module for this purpose.

---

## 5. Abstract Class

An **abstract class**:
- Cannot be instantiated (object cannot be created)
- May contain abstract methods and normal methods
- Acts as a blueprint for child classes

---

## 6. Abstract Method

An **abstract method**:
- Is declared but not implemented
- Must be implemented by all child classes
- Forces child classes to follow a structure

---

## 7. Syntax of Abstraction in Python

```python
from abc import ABC, abstractmethod

class ClassName(ABC):
    @abstractmethod
```
    def method_name(self):
        pass
