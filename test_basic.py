from main import add, subtract

def test_addition():
    assert add(1, 1) == 2

def test_subtraction():
    assert subtract(2, 1) == 1
