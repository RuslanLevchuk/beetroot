def some_func():
    a=1
    b=2
    print(len(locals()))

some_func()

print(some_func.__code__.co_nlocals)