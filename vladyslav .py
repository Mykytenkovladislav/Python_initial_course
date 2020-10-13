# 3) Написать функцию которая в качестве аргумента принимает словарь, в котором:
# в качестве ключей — числа „int“ а в качестве значений — либо словарь, с такой же структурой, либо None.
# Функция должна вернуть максимально большое число находящееся в этом словаре на произвольной глубине.

input_dict: dict = {
    2: None,
    4: None,
    12: {
        9: None,
        -8: None,
        547: {
            658: None,
            777: None,
            567: None
        }
    },
    15: None,
    59: {
        9: None,
        758: None,
    }
}


def recursive_func(input_dicts: dict):
    none_value_check = None
    max_value = 0
    for keys in input_dicts:
        if keys > max_value:
            max_value = keys
        for elem in keys:

    pass
    return max_value == recursive_func


print(recursive_func(input_dict))
