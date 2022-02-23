def oops():
    raise IndexError('this is error')


def func():
    try:
        oops()
    except IndexError as err:
        print(f"Error: {err}")


#oops()

func()