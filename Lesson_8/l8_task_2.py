def some_hell_function(sq, dv):
    try:
        sq = int(sq)
        dv = int(dv)
        return (sq**2)/dv
    except ValueError as message:
        print(f"Error: {message}")
    except ZeroDivisionError as message:
        print(f"Error: {message}")
    # with and without rising error printing some message

    finally:
        print('lalala...result is...')


while True:
    a = input('Type a: ')
    b = input('Type b: ')
    # if a or b is incorrect, function have nothing to return an print will be 'None'
    print(some_hell_function(a, b))