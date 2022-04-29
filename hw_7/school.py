class Person:
    def __init__(self, f_name, l_name, age, status):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.status = status

    def person_info(self):
        print(f'This is class Person for {self.f_name.title()}')
        print(f"{self.f_name.title()} {self.l_name.title()}, {self.age} years, {self.status.title()}")


class Teacher(Person):
    def __init__(self, f_name, l_name, age, status, discipline, experience, salary):
        Person.__init__(self, f_name, l_name, age, status)
        self.discipline = discipline
        self.experience = experience
        self.salary = salary

    def teacher_info(self):
        print(f'This is class Teacher for {self.f_name.title()}')
        print(f"{self.f_name.title()} {self.l_name.title()}, {self.age} years, {self.status.title()}")
        print(f"Discipline: {self.discipline.title()}")
        print(f"Experience: {self.experience} years")
        print(f"Salary: {self.salary} UAH")


class Student(Person):
    def __init__(self, f_name, l_name, age, status, class_level, stipend, speciality):
        Person.__init__(self, f_name, l_name, age, status)
        self.class_level = class_level
        self.stipend = stipend
        self.speciality = speciality

    def student_info(self):
        print(f'This is class Student for {self.f_name.title()}')
        print(f"{self.f_name.title()} {self.l_name.title()}, {self.age} years, {self.status.title()}")
        print(f"Class level: {self.class_level}")
        print(f"Stipend: {self.stipend} UAH")
        print(f"Speciality: {self.speciality.title()}")


prsn = Person('petka', 'durak', 14, 'student')
tchr = Teacher('natalka', 'levchuk', 28, 'teacher', 'chemistry', 5, '21000')
stdnt = Student('harry', 'potter', 15, 'student', 8, 0, 'magic')


prsn.person_info()
print('===================')
tchr.teacher_info()
print('===================')
tchr.person_info()
print('===================')
stdnt.student_info()
print('===================')
stdnt.person_info()
