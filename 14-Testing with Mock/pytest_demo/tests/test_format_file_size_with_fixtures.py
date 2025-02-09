import pytest

@pytest.fixture()
def welcome_message():
    """Return a welcome message."""
    return "Welcome to our application!"

def test_welcome_message(welcome_message):
    """Test if the fixture returns the correct welcome message."""
    assert welcome_message == "Welcome to our application!"