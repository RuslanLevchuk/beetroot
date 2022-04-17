import random
def slot_machine ():
    dict = ['☼', '♁', '♲', '✄', '𝄞', '🕱', '⑦']
    ints = [random.randint(0, 6) for i in range(3)]
    print(' '.join(str(dict[i]) for i in ints))
    check = list(set(ints))
    if len(check) == 1:
        print('Coincide!')
        if check[0] == 5:
            print('loose!')
        elif check[0] == 6:
            print('Jack pot!')

while 1:
    inp = input('Press ENTER to play ')
    if inp == '':
        slot_machine()