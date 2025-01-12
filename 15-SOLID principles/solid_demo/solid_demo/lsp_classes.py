from abc import abstractmethod, ABC



class TwoDimShape(ABC):

    def __init__(self, dim1:float, dim2:float):
        self._dim1 = dim1
        self._dim2 = dim2

    @abstractmethod
    def calculate_area(self):
        pass


class Triangle(TwoDimShape):
    def calculate_area(self):
        return round((self._dim1*self._dim2)/2, 2)

class Rectangle(TwoDimShape):
    def calculate_area(self):
        return round(self._dim1*self._dim2, 2)

class InvalidShape(TwoDimShape):
    def calculate_area(self):
        raise InvalidShapeException

class InvalidShapeException(Exception):
    pass
