# 10-Object oriented programming

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

### Superclass

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

