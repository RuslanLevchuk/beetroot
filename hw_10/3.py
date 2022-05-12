def arg_rules(type_: type, max_length: int, contains: list):
    def inner_func(func):
        def wrapper(name):
            if len(name) > 15:
                return False
            for symbol in contains:
                if symbol not in name:
                    return False
            return func(name)
        return wrapper
    return inner_func


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'