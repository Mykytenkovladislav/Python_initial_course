# Специальный компактный синтаксис для созания коллекций List, Dict

# List comprehensions

some_iterable = ['wa', 1, 2, 5, '2f', 2, '2', 'ert', '567z', []]
new_list = [item.upper() for item in some_iterable if isinstance(item, str)]
# Для каждого элемента(item) последовательности (some_iterable),
# выполняем операцию ( item.upper() ), если условия для этого элемента выполняется

# Dict comprehensions
new_dict = {item.upper(): item.lower() for item in some_iterable if isinstance(item, str)}

