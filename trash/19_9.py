dict = {
    'f': 3,
    'b': 8,
    'c': 1,
    'd': 6
}

for key, val in sorted(dict.items(), key=lambda it:it[0]):
        print(key, val)
#some_dict = {key: val for key, val in sorted(some_dict.items(), key=lambda item: item[1], reverse=True)}