def function(name):
    return f'Hi, {name}, and everyone! '

def multiple (func):
    def inner_func(x):
        return func(x)*3
    return inner_func

greeteeng = multiple(function)
print(greeteeng('Viktor'))