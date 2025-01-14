import string
from abc import abstractmethod, ABC


# A change in one operation method need recompile also of the dependent classes which are not dependent
# on that operation
# On python dependencies are resolved in runtime so no recompile is needed
# Interfaces Segregation Principle is related to those (statically typed )languages that require compilation
class WrongIndependentService:
    def operation1(self, service_name: string):
        return "operation1 at {}".format(service_name)

    def operation2(self, service_name: string):
        return "operation1 at {}".format(service_name)

    def operation3(self, service_name: string):
        return "operation1 at {}".format(service_name)


class WrongService1():
    def __init__(self, independent_service: WrongIndependentService):
        self.__service = independent_service

    def do_operation(self):
        return self.__service.operation1("wrong service name")


class Operations1(ABC):
    @abstractmethod
    def operation1(self, service_name: string):
        pass

class Operations2(ABC):
    @abstractmethod
    def operation2(self, service_name: string):
        pass

class Operations3(ABC):
    @abstractmethod
    def operation3(self, service_name: string):
        pass

class Service(Operations1):

    def __init__(self, service_name: string):
        self.__service_name = service_name

    def operation1(self, service_name: string):
        return "operation1 at {}".format(self.__service_name)

    def operation2(self, service_name: string):
        return "operation2 at {}".format(self.__service_name)

    def operation3(self, service_name: string):
        return "operation3 at {}".format(self.__service_name)


class Service1User(Operations1):


    def operation1(self, service_name: string):
        return "operation1 at {}".format(self.__service_name)

