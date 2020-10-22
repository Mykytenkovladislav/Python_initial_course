# Ваша задача - создать декоратор для функции, которая принимает неограниченное количество позиционных
# ХЕШИРУЕМЫХ элементов.
# Декоратор добавляет вашей функции следующий функционал:
# Если функция уже вызвалась с такими аргументами - ваша функция должна вернуть результат выполнения
# этой функции из памяти, а не вычислять его заного.
# Если не вызывалась - вычислить результат, положить его в память, и вернуть.

cache_dict: dict = {}  # dict for caching value after the first processing


def search_and_comparing(func):  # decorator
    print('Enter into decorator')

    def wrapper(*args, **kwargs):
        if args in cache_dict:
            print(f'Value already in  cache and it\'s = {cache_dict.get(args)}')  # debug
            return cache_dict.get(args)
        else:
            result = func(*args)
            cache_dict[args] = result
            print(f'Value added into cache and it\'s = {result}')  # debug
            return result

    return wrapper


@search_and_comparing
def main_func(*args):
    multiplication_of_factorials: int = 1  # variable for results
    factorial: int = 1  # factorial variable
    for num in args:  # cycle for every element in received tuple
        if num < 0:
            print("Sorry, factorial does not exist for negative numbers")
        elif num == 0:
            print("The factorial of 0 is 1")
        else:
            for i in range(1, num + 1):  # calculation of factorial
                factorial = factorial * i
            multiplication_of_factorials *= factorial
            factorial = 1  # discharge of factorial variable for next value calculation
    print(f'{multiplication_of_factorials=}')  # debug
    return multiplication_of_factorials


print(main_func(2, 3))
print(main_func(6, 7))
print(main_func(2, 3))
