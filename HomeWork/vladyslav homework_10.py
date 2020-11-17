# Task 1
def some(upper_border):
    current_i = 0
    test_list = list(range(upper_border))
    while current_i < test_list[upper_border - 1]:
        if test_list[current_i] % 3 == 0:
            yield test_list[current_i]
            current_i += 1
        else:
            current_i += 1


# Task 2
for generator in some(30):
    print(generator)

# Task 3
a = some(30)
b = a.__iter__()

while True:
    try:
        print(next(b))
    except StopIteration as e:
        break


# Task 4 zip but as func

def zip_func(*args):
    iterators: iter = [iter(it) for it in args]
    empty_object = object()
    while iterators:
        result: list = []
        for it in iterators:
            elem = next(it, empty_object)
            if elem is empty_object:
                return
            result.append(elem)
        yield tuple(result)


a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 3]

for item in (zip_func(a, b, c)):
    print(item)

# Task 4 enumerate but as func
test_list = ['a', 'b', 3, 4, 'test']
test_string = 'test string'
test_dict = {1: 1, 2: 2, 3: 3}


def enumerate_func(item_x):
    counter: int = 0
    for items in item_x:
        result: tuple = counter, items
        yield result
        counter += 1


iterated_func = enumerate_func(test_list)
iterator_1: iter = iterated_func.__iter__()

while True:  # variant with while cycle
    try:
        print(iterator_1.__next__())
    except StopIteration:
        break

for values in enumerate_func(test_string):  # variant with for cycle
    print(values)

for values in enumerate_func(test_dict):  # variant with for cycle
    print(values)

# Task 5 reversed but as func
test_list = ['a', 'b', 3, 4, 'test']
test_string = 'test string'
test_dict = {1: 'test', 2: 'papa', 3: 'Kappa'}


def reversed_func(input_value):
    if type(input_value) is dict:  # reversed for dicts
        reversed_dict = {}
        list_with_keys = list(input_value.keys())  # list with keys for reverting in future
        len_dict = len(list_with_keys)  # for indexing elements
        for i in list_with_keys:
            reversed_dict[list_with_keys[len_dict - 1]] = input_value.get(list_with_keys[len_dict - 1])
            len_dict -= 1
        yield reversed_dict
    else:  # reversed for all other
        item_x = input_value[::-1]
        yield item_x


for values in reversed_func(test_list):  # variant with for cycle
    print(values)

for values in reversed_func(test_string):  # variant with for cycle
    print(values)

for values in reversed_func(test_dict):  # variant with for cycle
    print(values)
