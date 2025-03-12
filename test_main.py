# tests/test_main.py
from my_python_app.main import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 2) == 8

def test_divide():
    assert divide(6, 3) == 2
    try:
        divide(6, 0)
    except ValueError:
        assert True
    else:
        assert False

