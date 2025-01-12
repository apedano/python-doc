import pytest
from solid_demo.srp_wrong_classes import Employee, Actor

@pytest.mark.parametrize(
    "actor_name, actor",
    Actor.__members__.items()
)
def test_actor_supported(actor_name, actor):
    employee = Employee()
    assert employee.isActorSupported(actor) == True

#This test shows that thr SRP principle (a module should be linked to one actor only)
def test_incompatible_actor_violating_srp():
    actor: Actor = Actor.CEO
    employee = Employee()
    #suppose this change is made for an actor CTO which makes the CFO functionality incompatible
    employee.makeIncompatibleFor(actor)
    assert employee.isActorSupported(actor) == False