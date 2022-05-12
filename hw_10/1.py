def logger(func):
    def wrapper(*args):
        print(f"Було викликано функцію \"{func.__name__}\" з аргументами:", end=' ')
        print(*args, sep=', ')
        print(f"Результат: {func(*args)}")
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(5,56)
square_all(2, 4, 8, 16)

