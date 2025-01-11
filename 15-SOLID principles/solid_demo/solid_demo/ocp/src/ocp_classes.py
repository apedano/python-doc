import json
import dict2xml as dict2xml
from abc import abstractmethod, ABC
from dataclasses import dataclass

@dataclass
class Address:
    line1: str
    city: str
    state: str
    zip: str

@dataclass
class Person:
    first_name: str
    last_name: str
    address: Address


class PersonSerializer(ABC):
    @abstractmethod
    def marshal(self, person:Person):
        pass

class PersonJson(PersonSerializer):
    def marshal(self, person:Person):
        return json.dumps(person)

class PersonXml(PersonSerializer):
    def marshal(self, person:Person):
        return dict2xml.dict2xml(person, wrap="Person")