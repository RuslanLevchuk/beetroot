def stop_words(*args: list):
    def inner(func):
        def wrapper(nm):
            res = str(func(nm))
            for i in args[0]:
                res = res.replace(i, '*')
            #print(res)
            return res
        return wrapper
    return inner

@stop_words(['pepsi', 'BMW'])

def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

create_slogan('Steve')


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"