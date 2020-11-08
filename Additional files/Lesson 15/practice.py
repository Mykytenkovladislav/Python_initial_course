"""
MRO это про порядок наследования
Этот алгоритм помогает понять какой следует вызвать метод из какого родителя
в том случае если он не обнаружен в классе-потомке
"""


class Mammals:
    total_mammals = 0

    def __init__(self, name, info_class, lifetime):
        self.name = name
        self.info_class = info_class
        self.lifetime = lifetime
        Mammals.total_mammals += 1

    @classmethod
    def total_mammals_count(cls):
        """
        @classmethod используется когда надо использовать атрибуты или методы класса
        без привязки к какому-то его экземпляру
        """
        print("Total objects: ", cls.total_mammals)

    @property
    def lifetime(self):
        """
        декоратор для реализации инкапсуляции для сокрытия и валидации данных
        """
        return self.__lifetime

    @lifetime.setter
    def lifetime(self, lifetime):
        if lifetime < 0:
            raise Exception('Не может вид иметь отрицательное время существование')
            print()
        else:
            self.__lifetime = lifetime

    def movement(self, speed=None):
        """
        Полиморфизм: возможность объекта вести себя по разному. Как пример через перегрузку
        """
        if speed is None:  # пример перегрузки
            print(f'Жаль, {self.name} только двигается, но с неизвестной скоростью')
        else:
            print(f' {self.name}  двигаемся со скоростью {speed}')

    def bite(self, strength):
        print(f'{self.name}делает кусь с силой {strength}')

    @staticmethod
    def get_info():
        print(f'Одна из целей применения статических методов, это группировка методов внутри класса'
              f'для них не надо создавать объектов и можно вызывать вот так: \n Car.get_info()')


class Dog(Mammals):  # Наследование, т.к. собака тоже является Млекопитающим
    """
    Класс для реализации наследования. Наследование это возможность использовать к примеру методы родителей
    """

    def __init__(self, name):
        self.name = name

    def bite(self, strength):
        print(f'А собаки, как {self.name} делает кусь с силой {strength}')


class Cat(Mammals):  # Наследование, т.к. собака тоже является Млекопитающим

    def __init__(self, name):
        self.name = name
