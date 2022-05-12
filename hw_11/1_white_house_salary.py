import itertools

class Emploee:
    def __init__(self, name, status, salary, pay_basis, position_title):
        self.name = name
        self.status = status
        self.salary = int(salary.replace('$', '').replace('.00', '').replace(',', ''))
        self.pay_basis = pay_basis
        self.position_title = position_title


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
            unit = Emploee(empl[0], empl[1], empl[2], empl[3], empl[4])
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


e = WH('white_house_2017_salaries_com.csv')
print('=========Середня========')
print(e.avg_slary())
print('=========топ-10=========')
t_10 = e.top_ten()
for k, v in t_10.items():
    print(k, v, sep=': ')
print('=======Тимчасові========')
print(e.temporary_vacancy())
print('====STAFF_ASSISTANT=====')
print(e.staff_assis_check())
print('====Кількість та види вакансій====')
print(e.total_vacancies()[0])
#print(*e.total_vacancies()[1], sep='\n')
print('====Кількість людей на кожній вакансії====')
#print(e.each_vacancy())