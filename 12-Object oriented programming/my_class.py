# Define a class named MyClass
class MyClass:

    # Constructor method that initializes the class object
    def __init__(self):
        # Define a protected variable with an initial value of 10
        # The variable name starts with a single underscore, which indicates protected access
        self._protected_var = 10

        # Define a private variable with an initial value of 20
        # The variable name starts with two underscores, which indicates private access
        self.__private_var = 20

    def myMethod(self):
        return self.__private_var


# Create an object of MyClass class
obj = MyClass()

# Access the protected variable using the object name and print its value
# The protected variable can be accessed outside the class but
# it is intended to be used within the class or its subclasses
print(obj._protected_var)  # output: 10

print(obj.myMethod())  # output: 20

# Try to access the private variable using the object name and print its value
# The private variable cannot be accessed outside the class, even by its subclasses
# This will raise an AttributeError because the variable is not accessible outside the class
print(obj.__private_var)  # AttributeError: 'MyClass' object has no attribute '__private_var'

