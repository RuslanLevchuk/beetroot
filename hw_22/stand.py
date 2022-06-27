import time
import sort1
import sort2
import random

def stand(func, n):
    times = []

    for i in n:
        t1 = time.perf_counter()
        func()
        t2 = time.perf_counter()
        times.append(t2 - t1)

    return f"avg = {sum(times)/len(times)}"


def test():
    n = 10000
    f = open('1.txt', 'a')
    for i in range(n):
        for j in range(n):
            f.write('1')
    f.close()


raz = 3
k = range(raz)
N = [5000, 10000, 20000]


for j in N:
    r = list(range(j))
    random.shuffle(r)
    print(stand((lambda: sort1.selection_sort(r)), k))
    print(stand((lambda: sort2.selection_sort(r)), k))
    print(stand((lambda: test()), k))

