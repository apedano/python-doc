import json

import pytest
from deepdiff import DeepDiff
from solid_demo.ocp_classes import Person, Address, PersonSerializer, PersonJson, PersonXml

@pytest.fixture
def sample_person():
    return Person("firstname", "lastname", Address("line1", "city1", "state1", "12345"))

def test_json_serialize(sample_person):
    try:
        serializer: PersonSerializer = PersonJson()
        expected = json.loads("""{
         "first_name": "firstname",
         "last_name": "lastname",
         "address": {
          "line1": "line1",
          "city": "city1",
          "state": "state1",
          "zip": "12345"
         }
        }""")
        actual = json.loads(serializer.marshal(sample_person))

        # Use deepdiff to compare with order-independent check
        diff = DeepDiff(expected, actual, ignore_order=True)

        assert not diff
    except json.JSONDecodeError:
        print("Invalid JSON format in one or both strings.")
        assert False

def test_xml_serialize(sample_person):
    serializer: PersonSerializer = PersonXml()
    person_xml = serializer.marshal(sample_person)
    assert person_xml == "<Person>Person(first_name='firstname', last_name='lastname', address=Address(line1='line1', city='city1', state='state1', zip='12345'))</Person>"