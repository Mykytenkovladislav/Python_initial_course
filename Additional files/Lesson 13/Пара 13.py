# как мы обычно открываем фаил?
try:
    somefile = open("hello.txt", "w")
    try:
        somefile.write("hello world")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)

# с помощью context manager
with open("hello.txt", "w") as file_obj:
    file_obj.write("hello world")



class Road:
    def __init__(self, q, m):
        self.quantity = q
        self.material = m


class Car:
    def __init__(self, max_speed=0, weight=0, model='lada'):
        self.model = model
        self.weight = weight
        self.max_speed = max_speed

    def drive(self, speed: int = 0, road: Road = None):
        print(f'drive {speed}')


my_car = Car(max_speed=245, weight=2000, model='Tesla X')

my_road = Road(67, 'Щебень')

my_car.drive(speed=200, road=my_road)
