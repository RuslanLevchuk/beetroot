import time
import sort1
import sort2
import random
import csv


def stand(func, n):
    times = []

    for i in n:
        t1 = time.perf_counter()
        func()
        t2 = time.perf_counter()
        times.append(t2 - t1)

    return sum(times)/len(times)

headers = ['len', 'sort1', 'sort2', 'sorted', 'sort']
raz = 5
k = range(raz)
N = list(range(0, 10000, 1))
test_file = 'max.csv'

with open(test_file, 'w', encoding='UTF8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for j in N:
        r = list(range(j))
        random.shuffle(r)
        res1 = stand((lambda: sort1.selection_sort(r)), k)
        res2 = stand((lambda: sort2.selection_sort(r)), k)
        res3 = stand((lambda: sorted(r)), k)*1000
        res4 = stand((lambda: r.sort()), k)*1000
        writer.writerow([j, res1, res2, res3, res4])
        if j%100 == 0:
            print(j)

file.close()



