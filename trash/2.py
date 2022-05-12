import functools

def red(func):
    def wrapper(*args, **kwargs):
        f = '<font color="red">'+func(*args, **kwargs)+'</font>'
        return f
    return wrapper

def green(func):
    def wrapper():
        f = '<font color="green">'+func()+'</font>'
        return f
    return wrapper


def bolt(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        f = f"BOLT {func(*args, **kwargs)} BOLT"
        return f
    return wrapper
color = 'red'
def color(color):
    def red(func):
        def wrapper(*args, **kwargs):
            f = f'<font color="{color}">{func(*args, **kwargs)}</font>'
            return f
        return wrapper
    return red


@color('black')
def hi(name):
    return f'hi, {name}'

def print_account():
    return ('I am Terminator')


#hi = green(hi)
#hi = red(hi)
print((hi('Terminator')))
#print_account = red(print_account)
print(print_account())