fio = 'Ruslan Mykolaiovych Levchuk'

fio_length = len(fio)
fio1 = fio.split()
name, otch, fam = fio1[0], fio1[1], fio1[2]
print(name, otch, fam)

print(f"o: {fio.count('o')}")
print(f"e: {fio.count('e')}")

fio_s = f"{fio1[0]}\n{fio1[1]}\t{fio1[2]}"
print(fio_s)