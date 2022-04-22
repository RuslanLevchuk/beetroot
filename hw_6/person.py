class Person:
    def __init__(self, firstname, lastname, age):
        self.age = age
        self.firstname = firstname
        self.lastname = lastname

    def talk(self):
        return f"Hello, your name is {self.firstname.title()} {self.lastname.title()} and you are " \
               f"{self.age} years old."
fnm, lnm = input("Input your first and last name: ").split()
ag_e = input("Input your age: ")
pers = Person(fnm, lnm, ag_e)
print(pers.talk())
