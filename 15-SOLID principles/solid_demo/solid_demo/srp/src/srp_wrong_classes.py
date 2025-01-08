from enum import IntFlag, auto
class Actor(IntFlag):
    CEO = auto() #1
    CFO = auto() #2
    CTO = auto() #3


class Employee:

    def __init__(self):
        print("Employee class initialized")
        self._supported_actors = Actor.CEO | Actor.CFO | Actor.CTO

    def makeIncompatibleFor(self, actor: Actor):
        if actor in self._supported_actors :
            self._supported_actors = ~actor
        else:
            print("Supported actors does not contain {} already. No change".format(actor))
        self.printSupportedActors()

    def isActorSupported(self, actor: Actor):
        return actor in self._supported_actors

    def printSupportedActors(self):
        print("supported actors now are: {}".format(self._supported_actors.__repr__()))



