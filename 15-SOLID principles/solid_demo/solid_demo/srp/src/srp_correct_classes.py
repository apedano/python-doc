import string
from dataclasses import dataclass, field
from enum import IntFlag, auto

class Actor(IntFlag):
    CEO = auto() #1
    CFO = auto() #2
    CTO = auto() #3

class Status(IntFlag):
    HIRED = auto()
    FIRED = auto()
    RETIRED = auto()

@dataclass
class Employee:
    name: string
    monthly_hours: int
    hour_rate: float = field(default = 10.0)
    status: Status = field(default = Status.HIRED)

class AdminService:
    def change_status(self, status: Status, employee: Employee):
        employee.status = status

    def set_hour_rate(self, hour_rate: float, employee: Employee):
        employee.hour_rate = hour_rate

class TechnicService:
    def log_hours(self, hours: int, employee: Employee):
        employee.monthly_hours += hours

class FinancialService:

    def calculate_salary(self, employee: Employee):
        return employee.monthly_hours * employee.hourRate

class EmployeeFacade:

    def __init__(self, ):
        self.__admin_service = AdminService()
        self.__technic_service = TechnicService()
        self.__financial_service = FinancialService()

    def change_status(self, actor: Actor, status: Status, employee: Employee):
        if actor == Actor.CEO:
            self.__admin_service.change_status(status, employee)
        else:
            raise ActorNotAllowedException("{} not allowed for this call".format(actor.name))

    def set_hour_rate(self, actor: Actor, hour_rate: float, employee: Employee):
        if actor == Actor.CEO:
            self.__admin_service.set_hour_rate(hour_rate, employee)
        else:
            raise ActorNotAllowedException("{} not allowed for this call".format(actor.name))

    def log_hours(self, actor: Actor, hours: int, employee: Employee):
        if actor == Actor.CTO:
            self.__technic_service.log_hours(hours, employee)
        else:
            raise ActorNotAllowedException("{} not allowed for this call".format(actor.name))

    def calculate_salary(self, actor: Actor, employee: Employee):
        if actor == Actor.CFO:
            return self.__financial_service.calculate_salary(employee)
        else:
            raise ActorNotAllowedException("{} not allowed for this call".format(actor.name))



class ActorNotAllowedException(Exception):
    pass