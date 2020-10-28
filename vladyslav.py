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
