def add(a,b):
    return a+b
def subtract(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def test_add():
    assert add(1,2) == 3,"Test Failed"
    #if (add(1,2) == 3):
    #    print(True)

def test_subtract():
    assert subtract(3,2) == 1,"Test Fail"
    #if subtract(3,2) == 1:
    #    print(True)

def test_sub():
    assert subtract(4,2) == 2,"Test Fail"
    #if subtract(4,2) == 2:
    #    print(True)

def test_multiplication():
    assert multiplication(4,4) == 16,"Test Fail"
    #if multiplication(4,4) == 16:
    #    print(True)

def test_mult():
    assert multiplication(3,3) == 9,"Test Failed"
#test_add()
#test_subtract()
#test_sub()
#test_multiplication()
