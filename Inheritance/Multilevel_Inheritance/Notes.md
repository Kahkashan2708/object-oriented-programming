## Multilevel Inheritance

Multilevel inheritance occurs when a class is derived from another derived class.

```python
class Grandparent:
    def house(self):
        print("Owns a house")

class Parent(Grandparent):
    def car(self):
        print("Owns a car")

class Child(Parent):
    def bike(self):
        print("Owns a bike")
```
