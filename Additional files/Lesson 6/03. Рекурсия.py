# Рекурсия - вызов функции внутри себя.

def factorial_with_recursion(x):
    # Если вы беретесь за рекурсию, всегда начните с определения крайнего случая!
    if x == 1:
        return 1
    return x * factorial_with_recursion(x - 1)


x = factorial_with_recursion
x(5)

print(factorial_with_recursion(5))


# Лучше заменять рекурсии циклами.
# Поскольку при большой глубине рекурсии может наступить -
# переполнеение стека вызовов. Stack Overflow!
def factorial_with_cycle(x):
    result = 1
    for i in range(x):
        result *= i + 1
    return result
