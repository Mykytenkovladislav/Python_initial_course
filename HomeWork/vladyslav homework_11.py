from time import sleep


class City:
    """
    Класс описывающий город и его методы
    """
    def __init__(self, name: str):
        self.name = name


class Road:
    """
    Класс описывающий дорогу и её методы
    """

    def __init__(self, name: str, type_of_road: str, quantity: int,
                 material: str, a_point: City, b_point: City, max_speed: int, length: int):
        self.name = name
        self.type_of_road = type_of_road
        self.quantity = quantity
        self.material = material
        self.a_point = a_point
        self.b_point = b_point
        self.max_speed = max_speed
        self.length = length

    @staticmethod
    def car_on_the_road(car_number: str, end_point: City, road):
        """
        Информация о поездке после выезда машины на дорогу
        """
        print(f'Car {car_number} on the road {road.name} and destination point is {end_point.name}')


class Car:
    def __init__(self, car_number: str, max_speed: int = 0, weight: int = 0, model: str = 'lada',
                 passenger_seats: int = 4, owner: str = 'Someone'):
        """
        Инициализация параметров класса
        :param car_number: номер машины
        :param max_speed: максимальная скорость
        :param weight: вес
        :param model: модель
        :param passenger_seats: кол-во пассажирских мест
        :param owner: владелец
        """
        self.car_number = car_number
        self.model = model
        self.weight = weight
        self.max_speed = max_speed
        self.passenger_seats = passenger_seats
        self.owner = owner

    def start_engine(self):
        """
        Заводим двигатель
        """
        print(f'Engine of {self.car_number} started')
        sleep(1)

    def stop_engine(self):
        """
        Останавливаем двигатель
        """
        print(f'Engine of {self.car_number} started')
        sleep(1)

    def drive(self, start_point: City, end_point: City, current_speed: int = 0, road: Road = None,
              driver=None,
              passengers_quantity: int = 0):
        """
        Выезд на дорогу
        :param start_point: стартовая локация (объект класса City)
        :param end_point: конечная локация (объект класса City)
        :param current_speed: текущая скорость машины
        :param road: дорога (объект класса Road)
        :param driver: водитель
        :param passengers_quantity: кол-во пассажиров
        """
        if not driver:
            driver = self.owner
        passengers_drop = passengers_quantity - self.passenger_seats
        if self.passenger_seats < passengers_quantity:
            f'You are taking more passengers than you should. Drop {passengers_drop} passengers'
        self.start_engine()
        if self.max_speed < current_speed:
            print('Check your speedometer')
            current_speed = self.max_speed
        Road.car_on_the_road(self.car_number, end_point, road)
        if current_speed > road.max_speed:
            print(f'Change your speed, because now it\'s more than it is allowed')
            self.change_speed(road.max_speed, current_speed, road)
        print(
            f'{driver} drives {self.model} on {road.name} from {start_point.name} to {end_point.name} at'
            f' {current_speed} km/h with {self.passenger_seats} passengers')

    def stop(self, current_speed, road: Road = None):
        """
        Остановка где-то на дороге
        :param current_speed: текущая скорость
        :param road: дорога, на которой будет произведена остановка
        """
        print(f'Pit-stop your {self.model} somewhere on the {road.name}')
        self.change_speed(0, current_speed, road)
        self.stop_engine()

    def change_speed(self, desired_speed: int, current_speed: int, road: Road):  # TODO current speed как и с Owner
        """
        Изменение скорости
        :param desired_speed: к какой скорости изменить
        :param current_speed: с какой скорости изменить
        :param road: дорога на которйо происходит изменение скорости
        :return:
        """
        if desired_speed > road.max_speed:
            print(f'Change your speed, because now it\'s more than it allowed')
        if desired_speed > self.max_speed:
            print(f'Your speed can\'t be more max speed: {self.max_speed}')
            desired_speed = self.max_speed
        print(f'Speed of {self.car_number} changed from {current_speed} to {desired_speed}')


kharkiv = City('Kharkiv')
energodar = City('Energodar')
kharkiv_energodar = Road('|road to home|', 'Magisterial', 70, 'Asphalt', kharkiv, energodar, 250, 406)
car_tesla = Car('XX0000XX', 350, 2000, 'Tesla X', 5, 'Egor')
car_kalina = Car('__Valhala__', 150, 1800, 'Lada Kalina', 5, 'Vladyslav')

car_tesla.drive(kharkiv, energodar, 1000, kharkiv_energodar, 'Egor', 1)
car_tesla.change_speed(2000, 350, kharkiv_energodar)
car_kalina.drive(energodar, kharkiv, 100, kharkiv_energodar, 'Owner', 8)
