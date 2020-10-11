def some_def_f(x, y):
    return x ** y


some_lamda_f = lambda x, y: x ** y



some_lamda_f1 = lambda x, y: x and y


result0 = some_lamda_f1(1, 0)
result1 = some_def_f(2, 3)
result2 = some_lamda_f(2, 3)

# lambda:
# не содержит return
# не содержит цикл
# не содержит условных конструкций
# но может содержать условные выражения
some_lamda_f2 = lambda x, y: x and y
