# 12A-Enums

## Declaration
Inherits from Enum itself

```python
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @classmethod
    def from_date(self, date):
        return self(date.isoweekday())
```

```python
#Access by value
print(Weekday(3)) #Weekday.WEDNESDAY

#Access by name
print(Weekday['SATURDAY']) #Weekday.SATURDAY

print(type(Weekday.MONDAY)) #<enum 'Weekday'>

print(Weekday.TUESDAY.name) #TUESDAY

print(Weekday.WEDNESDAY.value) #3

from datetime import date
print("Today is {}".format(Weekday.from_date(date.today()))) #Today is Weekday.WEDNESDAY
```

## Automatic value generation `auto()`

```python
from enum import Enum, auto
class AutoPowerThree(Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        print("Name: {}, start:{}, count:{}, last_values{}".format(name, start, count, last_values))
        return 3 ** count

class PowersOfThree(AutoPowerThree):
    THREE_ONE = auto()
    THREE_TWO = auto()
    THREE_THREE = auto()
    THREE_FOUR = auto()

print(PowersOfThree.THREE_THREE.value) #9

#Name: THREE_ONE, start:1, count:0, last_values[]
#Name: THREE_TWO, start:1, count:1, last_values[1]
#Name: THREE_THREE, start:1, count:2, last_values[1, 3]
#Name: THREE_FOUR, start:1, count:3, last_values[1, 3, 9]
```

## Aliases

Allows duplicate value in enum

```python
class Shape(Enum):
    SQUARE = 2
    DIAMOND = 1
    CIRCLE = 3
    ALIAS_FOR_SQUARE = 2
```

## Iteration

```python
for wd in list(Weekday):
    print(wd.name)
```

## `__members__` special attribute

The special attribute __members__ is a **read-only ordered map of names to members**. 
It includes all names defined in the enumeration, including the aliases:

```python
for name, member in Shape.__members__.items():
    print(name, member)

#SQUARE Shape.SQUARE
#DIAMOND Shape.DIAMOND
#CIRCLE Shape.CIRCLE
#ALIAS_FOR_SQUARE Shape.SQUARE
```

## Enum with reserved and custom attributes and members

```python
class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    VENUS   = (4.869e+24, 6.0518e6)
    EARTH   = (5.976e+24, 6.37814e6)
    MARS    = (6.421e+23, 3.3972e6)
    JUPITER = (1.9e+27,   7.1492e7)
    SATURN  = (5.688e+26, 6.0268e7)
    URANUS  = (8.686e+25, 2.5559e7)
    NEPTUNE = (1.024e+26, 2.4746e7)

    def __init__(self, mass, radius): #reserved must match the input list
        self.mass = mass       # in kilograms
        self.radius = radius   # in meters

    def __str__(self): #reserved for to string
        return 'Planet {} with mass {} Kg and radius {} m '.format(self.name, self.mass, self.radius)

    def order_of(self):
        return list(Planet.__members__.keys()).index(self.name) + 1

    @property
    def surface_gravity(self):
        # universal gravitational constant  (m3 kg-1 s-2)
        G = 6.67300E-11
        return G * self.mass / (self.radius * self.radius)

    @classmethod
    def our_planet(self):
        return self.EARTH

print(Planet.our_planet()) #Planet EARTH with mass 5.976e+24 Kg and radius 6378140.0 m
print(Planet.JUPITER) #Planet JUPITER with mass 1.9e+27 Kg and radius 71492000.0 m
print(Planet.URANUS.order_of()) #7
```
## Dataclass support

A `@dataclass` annotated method can be used to initialize the enum (without overriding the `__init__` method)

The `tail` field is set to not be showned in the `__repr__` method (string representation reserved method)

The `__repr__` method will not show the data class name

```python
from dataclasses import dataclass, field
@dataclass
class CreatureDataMixin:
    size: str
    legs: int
    tail: bool = field(repr=False, default=True) 

class Creature(CreatureDataMixin, Enum):
    BEETLE = 'small', 6, False
    DOG = 'medium', 4

print(Creature.DOG.__repr__()) #<Creature.DOG: size='medium', legs=4> 
print(Creature.BEETLE.tail) #False
```

## `Flag` enums

`Flag` is the same as `Enum`, but its members support the bitwise operators `&` (AND), `|` (OR), `^` (XOR), and `~` (INVERT); 
the results of those operations are (aliases of) members of the enumeration.

One way to declare them is assignign powers of a base in order to support logical operations 

```python
from enum import Flag
class Color(Flag):
    RED = 1
    GREEN = 2
    BLUE = 4
```

An alternative is automatic value assignment
```python
from enum import Flag, auto
class Color(Flag):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print(Color.BLUE.value) #4
```

We can define lists as logical OR sequence 

```python
purple = Color.RED | Color.BLUE
white = Color.RED | Color.GREEN | Color.BLUE

print(purple) #Color.RED|BLUE
print(purple.value) #5
print(white) #Color.RED|GREEN|BLUE
print(white.value) #7

```
### Functions

```python
#contains
print(Color.GREEN in purple) #False
print(Color.GREEN in white) #True
print(purple in white) #True
print(white in purple) #False
#__or__
purple = Color.RED | Color.BLUE
white = Color.RED | Color.GREEN | Color.BLUE
#__bool__ Returns True if any members in flag, False otherwise:
print(bool(Color.GREEN)) #True
print(bool(white)) #True
black = Color(0)
print(bool(black)) # False
#__and__
print((purple & white).__repr__()) #<Color.RED|BLUE: 5>
print((purple & Color.GREEN).__repr__()) #<Color: 0>
#__invert__(self): Returns all the flags in type(self) that are not in self:
print((~white).__repr__()) #<Color: 0>
print((~purple).__repr__()) #<Color.GREEN: 2>
print((~Color.RED).__repr__()) #<Color.GREEN|BLUE: 6>
```

## `IntFlag` enums
It is the same as Flag, 
but its members are also integers and can be used anywhere that an integer can be used.

```python
from enum import IntFlag, auto
class ColorInt(IntFlag):
    RED = auto() #1
    GREEN = auto() #2
    BLUE = auto() #3

print((ColorInt.RED & 2).__repr__()) #<Color: 0>
print((ColorInt.RED | 2).__repr__()) #<Color.RED|GREEN: 3>
print(ColorInt.RED + 5) #6
```