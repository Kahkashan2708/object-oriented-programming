# Encapsulation in Object-Oriented Programming (OOP)

## 1. What is Encapsulation?

Encapsulation is one of the four fundamental principles of Object-Oriented Programming.
It refers to **wrapping data (variables) and the methods (functions) that operate on that data into a single unit (class)** and **restricting direct access to the internal data**.

In simple terms:
> Encapsulation = Data Hiding + Controlled Access

---

## 2. Why Encapsulation is Needed

Encapsulation is used to:
- Protect data from unauthorized access
- Prevent accidental modification of data
- Improve code maintainability
- Make code more secure and reliable

---

## 3. How Encapsulation is Achieved

Encapsulation is achieved by:
- Declaring data members as **private**
- Providing **public methods** to access and modify the data safely

In Python, private members are created using **double underscore (`__`)**.

---

## 4. Access Modifiers in Python

| Access Level | Description |
|-------------|-------------|
| Public | Accessible from anywhere |
| Protected (`_`) | Accessible within class and subclasses |
| Private (`__`) | Accessible only within the class |

---

## 5. Example Without Encapsulation

```python
class Student:
    def __init__(self):
        self.marks = 90

s = Student()
s.marks = 500   # Wrong but allowed
```
