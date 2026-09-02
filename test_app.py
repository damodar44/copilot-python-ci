# use pytest to test the function app.py
import pytest
from app import add, subtract, multiply

def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(-1, 1) == -1
    assert multiply(0, 0) == 0
    assert multiply(2, 3) == 6
    assert multiply(-2, -3) == 6
    assert multiply(100, 200) == 20000
    assert multiply(-100, -200) == 20000
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0
    assert multiply(-5, 0) == 0
    assert multiply(0, -5) == 0

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2, 3) == 5
    assert add(-2, -3) == -5
    assert add(100, 200) == 300
    assert add(-100, -200) == -300
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(-5, 0) == -5
    assert add(0, -5) == -5 

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0
    assert subtract(2, 3) == -1
    assert subtract(-2, -3) == 1
    assert subtract(100, 200) == -100
    assert subtract(-100, -200) == 100
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5
    assert subtract(-5, 0) == -5
    assert subtract(0, -5) == 5

#add main function to run the tests
if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    print ("All tests passed!")