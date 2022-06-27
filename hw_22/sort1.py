def find_min(m):
    mi = m[0]
    ind = 0
    for i in range(len(m)):
        if m[i] < mi:
            ind = i
            mi = m[ind]
    return ind


def selection_sort(arr):
    old_arr = arr.copy()
    new_arr = []
    while len(old_arr) > 0:
        i = find_min(old_arr)
        # i = old_arr.index(min(old_arr))
        new_arr.append(old_arr.pop(i))
    return new_arr