import itertools

class Employee:
    count = 0
    staff = 0
    staff_salary = 0
    all_salary = 0
    staff_assistants = {}
    def __init__(self, name, status, salary, pay_basis, position_title):
        self.name = name
        self.status = status
        self.salary = int(salary.replace('$', '').replace('.00', '').replace(',', ''))
        self.pay_basis = pay_basis
        self.position_title = position_title

        Employee.count += 1                  #Загадьна кількість співробітників
        if self.status == 'Employee':
            Employee.staff += 1              #Підрахунок постійно працевлаштованих
            Employee.staff_salary += self.salary
        Employee.all_salary += self.salary   #Перерахунок загальної суми зарплат
        if self.position_title == 'STAFF ASSISTANT': #поповнення списку STAFF ASSISTANT
            Employee.staff_assistants[self.name] = self.salary

    def __del__(self):
        Employee.count -= 1
        Employee.all_salary -= self.salary
        if self.status == 'Employee':
            Employee.staff -= 1
        if self.position_title == 'STAFF ASSISTANT':
            Employee.staff_assistants.pop(self.name)

    @classmethod
    def report(self):
        return f"Всього працівників: {Employee.count} з середньою зарплатою {round(Employee.all_salary/Employee.count, 2)}\n" \
               f"З них постійних: {Employee.staff} з середньою зарплатою {round(Employee.staff_salary/Employee.staff, 2)}"

    @classmethod
    def assistants_report(self):
        rep = ''
        for key, val in Employee.staff_assistants.items():
            rep += 'Асистент: ' + key + ' / salary: $' + str(val) + '.00\n'
        return rep




class WH:
    def __init__(self, f_name):
        self.employees = []
        self.set_employees(f_name)


    def set_employees(self, f_name):
        f = open(f_name, 'r', encoding='utf-8')
        data = f.readlines()[1:]
        f.close()
        for n, v in enumerate(data):
            data[n] = data[n].strip().split(sep=';')
        for empl in data:
            unit = Employee(empl[0], empl[1], empl[2], empl[3], empl[4])
            self.employees.append(unit)


    def avg_slary(self):
        sum = 0
        for unit in self.employees:
            sum += unit.salary
        return round(sum/len(self.employees), 2)


    def top_ten(self):
        top_10 = {}
        for unit in self.employees:
            top_10[unit.name] = unit.salary
        top_10 = dict(sorted(top_10.items(), key=lambda item: item[1], reverse=True))
        return dict(itertools.islice(top_10.items(), 10))

    def temporary_vacancy(self):
        temp_vacancy = 0
        for unit in self.employees:
            if unit.status == 'Detailee':
                temp_vacancy += 1
        return f"Всього {temp_vacancy} тимчасових вакансій"

    def staff_assis_check(self):
        staff_assis_employees = 0
        staff_assis_salary_sum = 0
        for unit in self.employees:
            if unit.position_title == 'STAFF ASSISTANT':
                staff_assis_employees += 1
                staff_assis_salary_sum += unit.salary
        return f"Всього нв посаді STAFF ASSISTANT: {staff_assis_employees} працівників, " \
               f"середня зарплата: {round(staff_assis_salary_sum / staff_assis_employees, 2)}"

    def total_vacancies(self):
        vacancies = []
        for unit in self.employees:
            vacancies.append(unit.position_title)
        vacancies = list(set(vacancies))
        return f"Всього {len(vacancies)} видів вакансій", vacancies


    def each_vacancy(self):
        vacancies = dict.fromkeys(self.total_vacancies()[1], 0)
        for unit in self.employees:
            if unit.position_title in vacancies.keys():
                vacancies[unit.position_title] += 1
        return vacancies

    def recount(self):          #Підрахунок суми зарплат як окремий метод
        sum = 0
        for unit in self.employees:
            sum += unit.salary
        Employee.all_salary = sum

    @staticmethod
    def sum_salary(some_class):
        return f"Всього: {some_class.employees[0].__class__.all_salary}"     #тільки через індекс придумав достукатись до класу

    @staticmethod
    def avg_salary(some_class):
        return f"Середня: {round(some_class.employees[0].__class__.all_salary/some_class.employees[0].__class__.count, 2)}"



e = WH('white_house_2017_salaries_com.csv')

print(Employee.report())
print('==================================================')
print(Employee.staff_assistants)
print('==================================================')
print(e.employees[42].name, e.employees[42].position_title, sep=' | ') #Перевірка STAFF ASSISTANT на виделення
del e.employees[42]
print(Employee.staff_assistants) #Необхідний працівник видалено
print('==================================================')
print(Employee.assistants_report())
print(e.sum_salary(e))
print(e.avg_salary(e))