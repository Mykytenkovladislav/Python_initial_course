# decorators test
def decorator(func):
    def inner(n, m):
        print('decorator start')
        func(n, m)
        print('decorator finish')
    return inner