import pytest
from src.ocp_classes import Person, Address, PersonSerializer, PersonJson, PersonXml

@pytest.fixture
def sample_person():
    return Person("firstname", "lastname", Address("line1", "city1", "state1", "12345"))

def test_json_serialize(sample_person):
    serializer: PersonSerializer = PersonJson()
    person_json = serializer.marshal(sample_person)
    assert person_json == "wrong string"

def test_xml_serialize(sample_person):
    serializer: PersonSerializer = PersonXml()
    person_xml = serializer.marshal(sample_person)
    assert person_xml == "wrong string"