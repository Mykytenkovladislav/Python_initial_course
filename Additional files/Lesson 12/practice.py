def some(upper_border):
    current_i = 0
    test_list = list(range(upper_border))
    while current_i < test_list[upper_border - 1]:
        if test_list[current_i] % 3 == 0:
            yield test_list[current_i]
            current_i += 1
        else:
            current_i += 1


for generator in some(30):
    print(generator)

a = some(30)
b = a.__iter__()

while True:
    try:
        print(next(b))
    except StopIteration as e:
        break


# task: zip but as func

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

for iter_value in zip_func(a, b, c):
    print(iter_value)