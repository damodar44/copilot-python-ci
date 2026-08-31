# use pytest to test the function app.py
import pytest
from app import add

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

#add main function to run the tests
if __name__ == "__main__":
    test_add()
    print ("All tests passed!")