class CountCallNumber:

  def __init__(self, func):
    self.func = func
    self.call_number = 0
  #This method is called by Python when the decorated function is called
  def __call__(self, *args, **kwargs):
    self.call_number += 1
    print("This is execution number " + str(self.call_number))
    result = self.func(*args, **kwargs)
    print("After function call")
    return result 

@CountCallNumber
def say_hi(name):
  print("Hi! My name is " + name)

say_hi("Jack")
# This is execution number 1
# Hi! My name is Jack

say_hi("James")
# This is execution number 2
# Hi! My name is James