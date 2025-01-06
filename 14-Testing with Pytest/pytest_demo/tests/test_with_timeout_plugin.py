import pytest
import time


@pytest.mark.timeout(5)  # Set a 5-second timeout
def test_function_with_timeout():
    time.sleep(3)  # Simulate some work (should pass)
    assert True


@pytest.mark.timeout(1)  # Set a 1-second timeout
def test_function_exceeding_timeout():
    time.sleep(2)  # Simulate work that takes too long (should fail)
    assert True