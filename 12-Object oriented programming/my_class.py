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