class Car:
    def __new__(cls):
        obj = super(Car, cls).__new__(cls)
        if not hasattr(cls, 'car_count'):
            cls.car_count = []
        cls.car_count.append(obj.__name__)
        return obj


car_a = Car()
car_b = Car()
print(Car.car_count)
