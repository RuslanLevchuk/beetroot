class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = {}
        print(f'{name} додано до переліку авторів')

    def __len__(self):
        return len(self.books)

    def __str__(self):
        if len(self.books) == 0:
            return f"{self.name}, народився у {self.birthday} році, країна: {self.country}"
        else:
            some_str = f"{self.name}, народився у {self.birthday} році, країна: {self.country} \n" \
                       f"У біліотеці доступно {len(self.books)} книг цього автора: \n"
            for key, value in self.books.items():
                some_str += key + ', ' + str(value) + ' р \n'
            return some_str




class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f"\t{self.name}, {self.year} рік, {self.author}"


class Library:
    def __init__(self, name, *args):
        self.name = name
        self.authors = []
        self.books = []
        if len(args) > 0:
            self.authors += list(args)

    def add_book(self, name, year, author):
        self.books.append(Book(name, year, author))
        for auth in self.authors:
            if author == auth.name:
               auth.books[name] = year


    def group_by_author(self, author):
        print(f'{author}: ')
        for book in self.books:
            if book.author == author:
                print(book)


    def group_by_year(self, year):
        print(f'{year}: ')
        for book in self.books:
            if book.year == year:
                print(book)

    def __len__(self):
        return len(self.books)

au_1 = Author('Жуль Верн', 'Франція', 1828)
au_2 = Author('Тарас Шевченко', 'Україна', 1814)
au_3 = Author('Стівен Кінг', 'США', 1947)
print()
print(au_1)
print(au_2)
print(au_3)

lib = Library('У Петра', au_1, au_2, au_3)

lib.add_book('Діти капітана Гранта', 1868, 'Жуль Верн')
lib.add_book('20 000 льє під водою', 1869, 'Жуль Верн')
lib.add_book('Замок у Карпатах', 1889, 'Жуль Верн')
lib.add_book('Наймичка', 1853, 'Тарас Шевченко')
lib.add_book('Музикант', 1855, 'Тарас Шевченко')
lib.add_book('Зона покриття', 2006, 'Стівен Кінг')
lib.add_book('Зелена миля', 1996, 'Стівен Кінг')
lib.add_book('Воно', 1986, 'Стівен Кінг')
lib.add_book('Темена вежа', 1982, 'Стівен Кінг')

print()

lib.group_by_author('Стівен Кінг')
lib.group_by_year(2006)
print(f'\nБібліотека містить {len(lib)} книг\n')

print(au_1)
