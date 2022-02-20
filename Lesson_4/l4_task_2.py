while 1:
    name = input("Type your name: ")
    while 1:
        age = input("Type your age (digits only): ")
        if age.isdigit():
            age = int(age)
            if age > 120:
                print("No, you can\'t live so long! Are you vampire?")
            else:
                break
    print(f"Hello {name.capitalize()}, on your next birthday you’ll be {age + 1} years!")
