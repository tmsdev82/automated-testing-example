import pytest

@pytest.fixture
def get_person():
    return {
        "age": 23,
        "name": "Joe"
    }