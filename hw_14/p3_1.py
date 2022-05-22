def GreatNumerator(lst):
    for n, v in enumerate(lst):
        yield f"{n} {v}"


list = ['sony', 'samsung', 'dell', 'lenovo', 'toshiba', 'panasonic']


for i in GreatNumerator(list):
    print(i)