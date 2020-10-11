def some_name_for_function1():
    return


def some_name_for_function2():
    pass  # оператор зашлушка


some_name_for_function1()  # -> None
some_name_for_function2()  # -> None


# Аргументы
def some_func_with_position(x: int, y: float):  # x, y - 2 позиционных параметра
    return x * y


result1 = some_func_with_position(3, 5)  # x=3, y=5


def some_func_with_keys(some_key_arg: str = 'some_default_value') -> str:  # some_key_arg - именнованный аргумент.
    # 'some_default_value' - значение по умолчанию
    return some_key_arg + some_key_arg.replace('value', '****')


# При этом нет необходимости следить за порядоком аргументов;
# Есть значение по умолчанию для аргуументов, поэтому эти аргументы можно упускать.


result2 = some_func_with_keys()
result3 = some_func_with_keys(some_key_arg='some value some value some value')


# комбинации аргументов


def example(a, b, *args, x, y=None, z=2, u=5, **kwargs):
    type(args)  # tuple
    type(kwargs)  # dict
    pass


# Старайтесь не использовать мутабельные объекты в качестве параметров по умолчанию!
# Пример плохого использования
def change_list_bad_example(a, some_list=[]):
    some_list.append(a)
    return some_list


my_some_list1 = change_list_bad_example(1)
my_some_list2 = change_list_bad_example('zero')
my_some_list3 = change_list_bad_example('2')
print(my_some_list1, my_some_list2, my_some_list3)


#  [1, 'zero', '2'] [1, 'zero', '2'] [1, 'zero', '2']


def change_list_good_example(a, some_list=None):
    if not some_list:
        some_list = []
    some_list.append(a)
    return some_list


# Строки документации
# Строка документации - строка под def в тройных кавычках
def some_def_example():
    """This is example documentation"""
    return
