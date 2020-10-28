# Task 1
# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True,
# если оно простое, и False - иначе.

def is_prime(argument):
    k: int = 0  # кол-во делителей
    if argument == 0 or argument == 1:
        return False
    for i in range(2, argument):
        if argument % i == 0:
            k = k + 1
    if k == 0:
        return True
    return False


input_and_calc = is_prime(int(input('Введите число от 0 до 1000: ')))
print(input_and_calc)

# Task 2
# Даны два списка чисел. Посчитайте, сколько уникальных чисел
# содержится одновременно как в первом списке, так и во втором.
# Задача должна быть решена в одну строку.
list_1: list = [1, 2, 3, 4, 11]  # 4 уник
list_2: list = [8, 3, 5, 6, 12, 22, 33]

unique = len(set(list_1) | set(list_2))
print(unique)

# Task 3
# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна
# быть произведена над ними.
# Функция должна вернуть результат вычислений зависящий от третьего аргумент:
# +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
# В остальных случаях нужно возбудить исключение ValueError с сообщением - "Неизвестная операция"
operations_set: set = {'+', '-', '*', '/'}


def arithmetic(x, y, operation):
    if operation == "+":
        return x + y
    if operation == "-":
        return x - y
    if operation == '*':
        return x * y
    if operation == '/':
        return x / y
    if operations_set.isdisjoint(set(operation)):
        raise ValueError("Неизвестная операция")


print(arithmetic(1, 2, '+'))
print(arithmetic(1, 2, '-'))
print(arithmetic(1, 2, '*'))
print(arithmetic(1, 2, '/'))
print(arithmetic(1, 2, '!'))
