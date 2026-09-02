# use pytest to test the function app.py
import pytest
from app import add, subtract

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
    print ("All tests passed!")