class Counter:
    def __new__(cls):
        obj = super(Counter, cls).__new__(cls)
        if not hasattr(cls, 'my_objects_list'):
            cls.my_objects_list = []
        cls.my_objects_list.append(obj)
        return obj


s = Counter()
print("Object created", s)
s1 = Counter()
print("Object created", s1)

print(Counter.my_objects_list)
