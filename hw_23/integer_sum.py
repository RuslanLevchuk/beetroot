def str_sum(a):
    if type(a) == str:
        a = list(a)
    if len(a) == 1:
        return int(a[0])
    else:
        return int(a.pop())+str_sum(a)


a = '12345'
assert str_sum(a) == 15

inp = input('Type digits:')

try:
    int(inp)
    print(str_sum(inp))
except ValueError:
    print("Type digits only!")

