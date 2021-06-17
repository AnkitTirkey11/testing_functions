def add(a,b):
    return a+b
def subtract(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def test_add():
    if (add(1,2) == 3):
        print(True)

def test_subtract():
    if subtract(3,2) == 1:
        print(True)

def test_sub():
    if subtract(4,2) == 2:
        print(True)

def test_multiplication():
    if multiplication(3,2) == 6:
        print(True)

test_add()
test_subtract()
test_sub()
test_multiplication()
