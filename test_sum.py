def add(a,b):
    return a+b
def subtract(a,b):
    return a-b

def test_add():
    assert add(1,2) == 3,"test Fail"

def test_subtract():
    assert subtract(3,2) == 1,"Test Fail"

def test_sub():
    assert subtract(4,2) == 2,"Test Fail"
