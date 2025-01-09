# 10-Object oriented programming

<!-- TOC -->
* [10-Object oriented programming](#10-object-oriented-programming)
  * [Encapsulation](#encapsulation)
    * [Public members](#public-members)
    * [Protected Members:](#protected-members)
    * [Private Members:](#private-members)
  * [Define a class](#define-a-class)
  * [Inheritance](#inheritance)
    * [BaseClass](#baseclass)
      * [Sublcass](#sublcass)
  * [Polimorphism](#polimorphism)
  * [Abstraction](#abstraction)
  * [Static members](#static-members)
    * [Static attribute](#static-attribute)
    * [Static method](#static-method)
  * [Use decorators in class definition](#use-decorators-in-class-definition)
    * [`@classmethod`](#classmethod)
    * [`@staticmethod`](#staticmethod)
    * [`@property`](#property)
    * [`@dataclasses`](#dataclasses)
<!-- TOC -->

## Encapsulation

**Encapsulation** is one of the fundamental concepts of object-oriented programming, which helps to **protect the data and methods of an object from unauthorized access and modification**.

In Python, encapsulation can be achieved by using **access modifiers**. 

### Public members

* Attributes and methods **without any leading underscores** are considered public.
* They can be accessed from anywhere within or outside the class 


### Protected Members:
* Attributes and methods with a **single leading underscore** (_) are considered protected.
* They are **intended to be used within the class and its subclasses**. However, **they can still be accessed from outside the class**, but it's generally discouraged.

### Private Members:
* Attributes and methods with **double leading underscores** (__) are considered private.
* They are intended to be **used only within the class itself**.


## Define a class

```python
# Define a class named MyClass
class MyClass:

    # Constructor method that initializes the class object
    def __init__(self):
        self.public_var = 30
        
        # Define a protected variable with an initial value of 10
        # The variable name starts with a single underscore, which indicates protected access
        self._protected_var = 10

        # Define a private variable with an initial value of 20
        # The variable name starts with two underscores, which indicates private access
        self.__private_var = 20

    def public_method(self):
            return self.__private_var
    
    def _protected_method(self):
            print("This is a protected method.")
        
    def __private_method(self):
            print("This is a private method")

# Create an object of MyClass class
obj = MyClass()

print(obj.public_var)  # output: 30

# Access the protected variable using the object name and print its value
# The protected variable can be accessed outside the class but
# it is intended to be used within the class or its subclasses
print(obj._protected_var)  # output: 10

print(obj.public_method())  # output: 20

# Try to access the private variable using the object name and print its value
# The private variable cannot be accessed outside the class, even by its subclasses
# This will raise an AttributeError because the variable is not accessible outside the class
print(obj.__private_var)  # AttributeError: 'MyClass' object has no attribute '__private_var'
```

## Inheritance

**Inheritance** promotes code reuse and allows you to create a hierarchy of classes that share common attributes and methods. 

### BaseClass

```python
# Define a class named Animal
class Animal:

    # Constructor method that initializes the class object with a name attribute
    def __init__(self, name):
        self.name = name

    # Method that is defined in the Animal class but does not have a body
    # This method will be overridden in the subclasses of Animal
    def speak(self):
        print("")
```

#### Sublcass

```python
#Class has Animal as superclass
class Dog(Animal):

    # Override the speak method of the Animal class
    def speak(self):
        print("Woof!")


fido = Dog('Fido')
fido.speak() #Woof!
```
## Polimorphism

**Method overriding** is when a subclass provides its own implementation of a method that is already defined in its parent class. 
This allows the subclass to modify the behavior of the method without changing its name or signature.

**Method overloading** is when multiple methods have the same name but different parameters. 
**Python does not support method overloading directly**, but it can be achieved using default arguments or variable-length arguments.
```python
#The Shape class is defined with an abstract area method, which is intended to be overridden by subclasses.
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    # The Rectangle class is defined with an __init__ method that initializes
    # width and height instance variables.
    # It also defines an area method that calculates and returns
    # the area of a rectangle using the width and height instance variables.
    def __init__(self, width, height):
        self.width = width  # Initialize width instance variable
        self.height = height  # Initialize height instance variable

    def area(self):
        return self.width * self.height  # Return area of rectangle


 # The Circle class is defined with an __init__ method
 # that initializes a radius instance variable.
 # It also defines an area method that calculates and
 # returns the area of a circle using the radius instance variable.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Initialize radius instance variable

    def area(self):
        return 3.14 * self.radius ** 2  # Return area of circle using pi * r^2

# The shapes list is created with one Rectangle object and one Circle object. The for
# loop iterates over each object in the list and calls the area method of each object
# The output will be the area of the rectangle (20) and the area of the circle (153.86).
shapes = [Rectangle(4, 5), Circle(7)]  # Create a list of Shape objects
for shape in shapes:
    print(shape.area())  # Output the area of each Shape object
```

## Abstraction

Python does not have built-in support for abstract classes or interfaces, but they can be implemented using:
* the `abc` (**abstract base class**) module: This module provides the `ABC` class and the `abstractmethod` decorator, which can be used to define abstract classes and methods.

Overall, abstraction is a powerful tool for managing complexity and improving code quality in object-oriented programming, and Python provides a range of options for achieving abstraction in your code.

```python
# Import the abc module to define abstract classes and methods
from abc import ABC, abstractmethod

class Shape():
    def __init__(self, dimension):
        self._dimension1 = dimension

# Define an abstract class called Shape that has an abstract method called area
class TwoDimShape(ABC, Shape):
    
    @abstractmethod
    def area(self):
        pass

# Define a Rectangle class that inherits from Shape
class Rectangle(TwoDimShape):
    def __init__(self, width, height):
        self._dimension1 = width
        self._dimension2 = height

    # Implement the area method for Rectangles
    def area(self):
        return self._dimension1 * self._dimension2

# Define a Circle class that also inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self._dimension1 = radius

    # Implement the area method for Circles
    def area(self):
        return 3.14 * self._dimension1 ** 2

# Create a list of shapes that includes both Rectangles and Circles
shapes = [Rectangle(4, 5), Circle(7)]

# Loop through each shape in the list and print its area
for shape in shapes:
    print(shape.area())
```

## Static members

### Static attribute

```python
class MyClass:
    static_var = 10

    def __init__(self, instance_var):
        self.instance_var = instance_var

# Accessing the static attribute
print(MyClass.static_var)  # Output: 10
```

### Static method

```python
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method")

# Calling the static method
MyClass.static_method()  # Output: This is a static method 
```

## Use decorators in class definition

### `@classmethod`

Used to define methods **bounded to the class instead of the instances**
Used for:

* Creating factory methods to create instances of the class.
* Implementing alternative constructors.
* Accessing class-level attributes without creating an instance.

```python
class MyClass:
    @classmethod
    def from_string(cls, string):
        # Create an instance from a string
        return cls(string)
```

### `@staticmethod`

Defines a **method that is not bound to the class or its instances**.

* Creating utility functions that are related to the class but don't need access to instance or class attributes.

```python
class MyClass:
    @staticmethod
    def is_even(num):
        return num % 2 == 0
```

### `@property`
This can be bounded to a non-public class attribute and it is linked to three other decorators:

* `@property` (used as a getter)
* `@<property_name>.setter`
* `@<property_name>.deleter`

```python
class House:

    def __init__(self, price):
        self._price = price

    @property #getter
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")

    @price.deleter
    def price(self):
        del self._price

house = House(50000.0)  # Create instance
house.price = 45000.0   # Update value
print(house.price)             # Access value 45000.0

# Delete the instance attribute
del house.price

# The instance attribute doesn't exist
print(house.price)

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    house.price
  File "<pyshell#20>", line 8, in price
    return self._price
AttributeError: 'House' object has no attribute '_price'
```

### `@dataclasses`

`Dataclasses` are python classes, but are suited for storing data objects. 
This module provides a decorator and functions for automatically adding generated special methods such as `__init__()` and `__repr__()` (as the `toString()` in Java) to user-defined classes.

**It resables the @Data annotation in Lombok**

A standard class declaration is 

```python
class Number:
    def __init__(self, val):
        self.val = val

obj = Number(2)
obj.val
# 2
```

with the decorator it becomes

```python
@dataclass
class Number:
    val: int

obj = Number(2)
obj.val
# 2
```

> It is **mandatory to specify the field type** but the `typing.Any` can be used

```python
from dataclasses import dataclass
from typing import Any

@dataclass
class WithoutExplicitTypes:
  name: Any
  value: Any = 42
```
 
We can also define **default values** for the attributes

```python
@dataclass
class Product:
    name: str
    count: int = 0
    price: float = 0.0

obj = Product("Python")
obj.name
# Python

obj.count
# 0

obj.price
# 0.0
```
`field` definitions can also be used

```python
dataclasses.field(*, default=MISSING, default_factory=MISSING, init=True, repr=True, hash=None, compare=True, metadata=None, kw_only=MISSING)
```
More details [here](https://docs.python.org/3/library/dataclasses.html)

```python
@dataclass
class C:
    x: int
    y: int = field(repr=False)
    z: int = field(repr=False, default=10)
    mylist: list[int] = field(default_factory=list)

c = C()
c.mylist += [1, 2, 3]

```







