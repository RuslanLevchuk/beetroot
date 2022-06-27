def int_sum(a):
    if a < 10:
        return a
    else:
        return a%10 + int_sum(a//10)


a = 5001001001
assert int_sum(a) == 8


print(int_sum(a))