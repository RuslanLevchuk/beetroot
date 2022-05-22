list = ['one', 'two', '3', 'four', '5', '6', 'seven', '8', '9', '10']

print([(n, i) for n, i in enumerate(list) if i.isdigit()])