class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.seat = kw.get("seat")


car = Car(seat=4, model=2009, make="Toyota")
print(car.model)


# kwargs is a dictionary.
def func(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


func(ali="veli", dursun="wehwet", x=27)
