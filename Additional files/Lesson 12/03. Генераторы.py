# Итераторы - все объекты которые могут участвовать в цикле
from random import random

a = [1, 2]  # Итерируемый объект.

b = a.__iter__()  # метод __iter__ возвращает специальный объект - iterator.
с = b.__iter__()  # Интересным является то,
# что большинство итераторов вохвращают себя при вызове у них метода __iter__()

# b - объект-итератор.

b.__next__()  # Именно его использует цикл for i in …  для получения i:
# При этом, если следующего объекта нет - будет вызвано исключение, и его необъодимо будет обработать

# Итого - Итератор - это такой объект, который реализует в два метода - __iter__ и __next__



# Генераторы - это такие объекты, которые могут участовать в цикле, но только один раз. Это разновидность Итераторов

def some():
    yield from range(10)
    yield from range(20)

for generator in some():
    print(type(generator))



def my_generator(in_range=10):
    current_i = 0
    while current_i < in_range:
        current_i += 1
        yield current_i


for i in my_generator(in_range=15):
    print(i)


def manual_call(generator):
    while True:
        print(
            'manual_call', generator.__next__()
        )


generator_obj = my_generator(in_range=12)
manual_call(generator_obj)


# Для обявления генераторов есть специальный синтаксис:
my_new_generator = (i for i in range(5))  #
