def selection_sort(arr):
    old_arr = arr.copy()
    new_arr = []
    while len(old_arr) > 0:
        i = old_arr.index(min(old_arr))
        new_arr.append(old_arr.pop(i))
    return new_arr