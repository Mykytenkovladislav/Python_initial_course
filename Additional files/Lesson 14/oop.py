# 1) Понятие класса и объекта
# Класс - это чертеж по которому создаются объекты

# 2) Объект - сущность созданная по определенному классу (чертежу),
# иногда его называют instance

class Cat:
    def __init__(self, color='Black'):
        self.color = color


murzik: Cat = Cat()
barsik: Cat = Cat(color='red')


# 3) Атрибуты классов и объектов (иногда их называют поля)

class Cat2:
    average_weight = 4.1  # Атрибут класса

    def __init__(self, color='Black', weight=average_weight):
        # Обратите внимение, что внутри методов объектов будут доступны атрибуты класса
        self.color = color  # Атрибут объекта
        self.weight = weight  # Атрибут объекта


average_cat_weight = Cat2.average_weight  # Обращение к атрибуту класса

gosha = Cat2(weight=13)  # для обращения к атрибуту объекта нужно иметь объект!
gosha.weight = gosha.weight  # Обращение к атрибуту объекта


# Инициализация и нектороые магические методы
class Cat3:
    average_weight = 4.1  # Атрибут класса

    def __new__(cls, *args, **kwargs):
        """
        Этот метод вызывается до создания самого объекта, перед методом __init__
        Он создает пустой объект в памяти
        """
        return super().__new__(cls)

    def __init__(self, name='', weight=average_weight):
        """
        В этот метод попадают все аргументы переданные в при создании объекта
        Он инициализирует объект, добавляя в него атрибуты
        """
        self.name = name
        self.weight = weight

    def __str__(self) -> str:  # Вызывается при приведении объекта к строке например функцией str()
        """Этот метод должен возвращать человеко-читаемое описание объекта"""
        return f"Cat with name: {self.name}"

    def __repr__(self) -> str:  # Вызывается, например, при выводе ошибки
        """
        Этот метод должен возвращать максимально-подробную информацию
        по воссозданию объекта
        """
        return f"Cat(name={self.name})"

    # Магические методы сравнения

    def __eq__(self, other):
        """Этот магический метод вызывается при использовании оператора '==' """
        return self.weight == other.weight

    def __le__(self, other):
        """Этот магический метод вызывается при использовании оператора '<=' """
        return self.weight <= other.weight

    def __ge__(self, other):
        """Этот магический метод вызывается при использовании оператора '>=' """
        return self.weight >= other.weight

    def __lt__(self, other):
        """Этот магический метод вызывается при использовании оператора '<' """
        return self.weight < other.weight

    def __gt__(self, other):
        """Этот магический метод вызывается при использовании оператора '>' """
        return self.weight > other.weight

    # вызов объекта как функции

    def __call__(self, action='Мурлыкать'):
        if action == 'Мурлыкать':
            print('Mrr-rrr mrr-rrr')
        else:
            print('Котик не хочет этого делать.')
        return ''


# инициализация объектов
oleh = Cat3(name='Олег', weight=3)
kesha = Cat3(name='Кеша', weight=5)

# Сравнение объектов (котиков)
print(oleh == kesha)
print(oleh >= kesha)
print(oleh <= kesha)
print(oleh > kesha)
print(oleh < kesha)

# Вызов объекта (котика) как функции
oleh(action='Мурлыкать')
kesha(action='Играться')


class Cat4:
    average_weight = 4.1  # Атрибут класса

    def __init__(self, name='', weight=average_weight, fluffiness=10):
        self.name = name
        self.weight = weight
        self.fluffiness = fluffiness  # пушистость

    # этот декоратор говорит о том что этот метод будет использоваться классом, а не объектом
    @classmethod
    def is_fat_cat(cls, cat):
        assert isinstance(cat, cls), 'Это не объект класса Cat4'
        if cat.weight > cls.average_weight:
            return True
        return False

    # Этот декоратор позволяет обращатся к методу класса как к атрибуту,
    # не явно вызывая его
    @property
    def volume(self):
        return self.weight + (self.fluffiness // 5)

    @staticmethod
    def some_method(*args, **kwargs):
        """
        Иногда возникает потребность использовать класс
        просто для структурирования кода,
        без надобности использовать какие-либо поля класса,
        как своеобразный мешок для функций
        """
        return args, kwargs


c1 = Cat4()
print('Толстые ли эти котики?', Cat4.is_fat_cat(c1))
# print('Толстые ли эти котики?', Cat4.is_fat_cat(oleh))  => Вызовет ошибку


print(c1.volume)  # Вызовет метод volume, причем без использования оператора '()'


# Наследоваание

class Transport:
    def __init__(self, max_move_speed=0):
        self.max_move_speed = max_move_speed

    def move(self):
        return f'move with speed {self.max_move_speed}'


class Car(Transport):
    def __init__(self, *args, model='', **kwargs):
        self.model = model
        super().__init__(*args, **kwargs)
        super(Transport, self).__init__(*args, **kwargs)


some_transport = Transport(max_move_speed=50)
car1 = Car(max_move_speed=350, model='Tesla X')


class AirPlane(Transport):
    def __init__(self, *args, wing_length=10, **kwargs):
        self.wing_length = wing_length
        super().__init__(*args, **kwargs)

    def move(self):
        parent_result = super().move()
        return f'{parent_result} При этом мы летим!'


class AirCar(Car, AirPlane):
    pass



class Counter:
    def __new__(cls):
        obj = super(Counter, cls).__new__(cls)
        if not hasattr(cls, 'objects_list'):
            cls.objects_list = []
        cls.objects_list.append(obj)
        return obj

s = Counter()
print("Object created", s)
s1 = Counter()
print("Object created", s1)

Counter.objects_list
