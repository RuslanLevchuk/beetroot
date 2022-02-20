ditc = {'artem': '09365043540', 'igor': '06735242577'}

while 1:
    name = (input("Type name to view or type 'q' to exit: "))
    name = name.lower()
    if name == 'q':
        break
    if name in ditc.keys():
        print(f"{name.capitalize()}: tel.: {ditc.get(name)}")
        del_c = input('What to do? Delete? (yes/no): ')
        if (del_c.lower()) == 'yes':
            ditc.pop(name)
        else:
            pass
    else:
        number_add = input("There no contact in address book, please type its number: ")
        if number_add.isdigit():
            ditc[name] = number_add
        else:
            number_add = input("Please, type correct number with digits only: ")
            ditc[name] = number_add


