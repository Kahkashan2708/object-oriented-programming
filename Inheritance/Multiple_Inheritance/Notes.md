## Multiple Inheritance

Multiple inheritance occurs when a child class inherits from more than one parent class.

```python
class Father:
    def skill1(self):
        print("Gardening")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass
```
