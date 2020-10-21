# Декоратор - это такая функция,
# принимающая в качестве аргументов функцию,
# создающая внутри себя функцию и возвращающая новую функцию

# Пример объявления декораторов


def benchmark(func):
    import time
    print(
        "Я обычная функция которая принимает в качестве аргумента функциию, "
        "создает внутри себя функцию и возвращает ее"
    )

    def wrapper(*args, **kwargs):
        print("А я функция, которая была создана во время вызова декоратора")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return result

    return wrapper


@benchmark
def some_f(x: int, y: int):
    return x ** y


def fetch_webpage1(*args, **kwargs):
    import requests
    webpage = requests.get('https://google.com')


fetch_webpage1 = benchmark(fetch_webpage1)


# У этой операции есть синтаксический сахар
@benchmark
def fetch_webpage2():
    import requests
    webpage = requests.get('https://google.com')


fetch_webpage2()


# декораторы с аргументами - Это настоящие фабрики декораторов.
# Пример объявления декораторов с аргументами.
# Как это читать???
def benchmark(iters):
    # Внешняя функция получает какие-то аргументы и на основании этих аргументов она строит функцию обертку
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total / iters))
            return return_value

        return wrapper

    return actual_decorator


@benchmark(iters=10)
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


webpage = fetch_webpage('https://google.com')
print(webpage)


def bread(func):
    def wrapper():
        print("</------\>")
        func()
        print("<\______/>")

    return wrapper


def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")

    return wrapper


def sandwich1(food="--ветчина--"):
    print(food)


sandwich1()
# выведет: --ветчина--

sandwich1 = bread(ingredients(sandwich1))
sandwich1()


# Что выведет sandwich1() ????


@bread
@ingredients
def sandwich2(food="--ветчина--"):
    print(food)


sandwich2()

# выведет:
# выведет:
# </------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>
