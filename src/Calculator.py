def addition(a, b):
    a = float(a)
    b = float(b)
    return a + b


def subtraction(a, b):
    a = float(a)
    b = float(b)
    return a - b


def multiplication(a, b):
    a = float(a)
    b = float(b)
    return a * b


def division(a, b, c):
    a = float(a)
    b = float(b)
    if (b == 0):
        return None
    else:
        return round(a / b / c)


def squaring(a):
    a = float(a)
    return a ** 2


def squareRoot(a, b):
    a = float(a)
    if (a < 0):
        return None
    else:
        return round(a**(1/2), b)

def lenth(a):
    if (len(a.split('.')) > 1):
        return len(a.split('.')[1])
    else:
        return 0


class Calculator:
    result = 0

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(b, a)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b, c):
        self.result = division(a, b, c)
        return self.result

    def square(self, a):
        self.result = squaring(a)
        return self.result

    def sqrt(self, a, b):
        self.result = squareRoot(a, b)
        return self.result

    def getLength(self, a):
        return lenth(a)

    def __init__(self):
        pass
