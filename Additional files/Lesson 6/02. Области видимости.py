def example1(x: int, y: int):
    # Идентификаторы 'x' и 'y' являются:
    # - local для example1()
    # - nonlocal для example2()

    def example2(a, b):
        return a + 2, b + 3  # 'a' - локальный идентификатор функции cube()

    return max(
        *example2(x, y), *example2(y, x)
    )
    # Функция max() находится во встроенной области видимости


# Идентификаторы 'q', 'w' и 'e' имеют глобальную область видимости
q, w, e = 1, 2, 4
print(example1(q, w))  # 8

# По умолчанию,
# идентификаторы из других областей доступны только для чтения
x = 'someeee'


def example_with_global():
    x = 'zzzzzzz'  # не поменяет значение x вне функции,
    # а создаст новый идентификатор x для локальной обслати видимости

    # Но есть способ поменять глобальную переменную
    global x
    # Теперь мы можем менять x
    x = 2
    # И Теперь x - идентификатор нового объекта - 2


def func():
    def first_inner_func():
        value = 100  # 'value' - локальный идентификатор

    value = 10
    first_inner_func()
    print(value)  # 10

    def second_inner_func():
        nonlocal value
        value = 100  # nonlocal позволяет использовать value из func()

    second_inner_func()
    print(value)  # 100
