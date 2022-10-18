def add(*asd):
    print(asd[1])
    total = 0
    for n in asd:
        total += n
    return total

def multiply(*qwerty):
    total = 1
    for n in qwerty:
        total *= n
    return total

def calculate(n, **kwargs):
    # print(kwargs["add"])
    # for key, value in kwargs.items():
    n *= kwargs["multiply"]
    n += kwargs["add"]
    return n

class Car:
    def __init__(self, **kw):
        if __name__ == '__main__' :
            self.make = kw["make"]
            self.model = kw.get("model")

my_car = Car(make="Ford")
print(my_car.model)
print(calculate(2, add=3, multiply=5))
print(add(2,3,4,5))
print(multiply(2,3,4,5))



