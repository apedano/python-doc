import pytest
from src.srp_correct_classes import Employee, Actor, Status, EmployeeFacade, ActorNotAllowedException

@pytest.fixture
def sample_employee():
    employee = Employee("sample", 1)
    return employee

@pytest.fixture
def employee_facade():
    return EmployeeFacade()

#This test shows that thr SRP principle (a module should be linked to one actor only)
def test_ceo_change_status(sample_employee, employee_facade):
    ceo: Actor = Actor.CEO
    new_status = Status.FIRED
    assert sample_employee.status != new_status
    employee_facade.change_status(ceo, new_status, sample_employee)
    assert sample_employee.status == new_status

def test_not_cfo_actor_on_change_status(sample_employee, employee_facade):
    now_allowed_actor = Actor.CFO
    new_status = Status.FIRED
    with pytest.raises(ActorNotAllowedException, match="CFO not allowed for this call"):
        employee_facade.change_status(now_allowed_actor, new_status, sample_employee)

def test_ceo_set_hour_rate(sample_employee, employee_facade):
    ceo: Actor = Actor.CEO
    new_hour_rate = 100
    assert sample_employee.hour_rate != new_hour_rate
    employee_facade.set_hour_rate(ceo, new_hour_rate, sample_employee)
    assert sample_employee.hour_rate == new_hour_rate





