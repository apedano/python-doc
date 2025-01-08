def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3, "hello")  # Output: 1 2 3 hello

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="Alice", age=30, city="New York")  # Output: name: Alice

def my_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs) #{'name': 'Alice', 'age': 30}
    print("Second argument:", args[1])
    print("Name keyword value:", kwargs['name'])

my_function(1, 2, name="Alice", age=30)
# Positional arguments: (1, 2)
# Keyword arguments: {'name': 'Alice', 'age': 30}
#Second argument: 2
#Name keyword value: Alice