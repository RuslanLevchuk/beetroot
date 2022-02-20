tpl_1 = ('hello', 3, 5, 'world')
tpl_2 = ('he', 'he', 'he', 'he')

def compare_f (tpl):
    for i in tpl:
        for j in tpl:
            if j != i:
                return False
    return True

print(compare_f(tpl_1))
print(compare_f(tpl_2))