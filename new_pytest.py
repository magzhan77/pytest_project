import pytest

@pytest.fixture
def users():
    return ['alice', 'bob', 'charlie']

def test_user_count(users):
    assert len(users) == 3

@pytest.mark.parametrize("username", ['alice', 'bob', 'charlie'])
def test_username_in_users(users, username):
    assert username in users

@pytest.mark.parametrize("count", [1, 2, 3])
def test_user_count_dynamic(users, count):
    assert len(users) == count



# Code to be tested
def add(a, b):
    return a + b

# Test function
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


