class MyClass:
    def __init__(self):
        self._age = 25

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

obj = MyClass()
print(obj.age)
