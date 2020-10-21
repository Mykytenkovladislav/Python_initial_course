# Ваша задача - создать декоратор для функции, которая принимает неограниченное количество
# позиционных ХЕШИРУЕМЫХ элементов.

# Если функция уже вызвалась с такими аргументами - ваша функция должна вернуть результат выполнения этой функции
# из памяти, а не вычислять его заного.

# Если не вызывалась - вычислить результат, положить его в память, и вернуть.

cache_dict: dict = {}  # dict for caching value after the first processing


def search_and_comparing(func):  # decorator
    print('Enter into decorator')

    def wrapper(*args, **kwargs):
        for item in args:  # checking every element from received values
            if item in cache_dict:
                print(f'Value already in  cache and it\'s = {cache_dict.get(item)}:')
            else:
                result = func(item)
                print(f'Value added into cache and it\'s = {result}')

    return wrapper


@search_and_comparing
def main_func(item):
    print(f'some action in main func with received {item=}')
    cache_dict[item] = (item * 2)  # adding value into dict for caching after some action
    return cache_dict.get(item)


main_func(1, 2.2, '312', 1, 2.2, '312', )
