smallest_salary = 0
smallest_salary_id = 0
largest_salary = 0
largest_salary_id = 0
avg_salary = 0.0
total_count_with_salary = 0
no_salary_count = 0
staff_ass_workers = 0
staff_ass_avg_salary = 0
detailee_workers = 0
detailee_workers_avg_salary = 0
top_10 = []

f = open('white_house_2017_salaries_com.csv', 'r', encoding='utf-8')
headers = f.readline().split(';')
data = f.readlines()
f.close()

for n, val in enumerate(headers):
    headers[n] = val.strip()

for n, v in enumerate(data):
    data[n] = data[n].strip().split(sep=';')

smallest_salary = float(data[0][2].replace('$', '').replace(',',''))
largest_salary = float(data[0][2].replace('$', '').replace(',',''))

for n, employee in enumerate(data):

    employee_temp_salary = float(employee[2].replace('$', '').replace(',',''))
    if employee_temp_salary < smallest_salary and employee_temp_salary != 0:
        smallest_salary = employee_temp_salary
        smallest_salary_id = n
    if employee_temp_salary > largest_salary:
        largest_salary = employee_temp_salary
        largest_salary_id = n
    if employee_temp_salary == 0:
        no_salary_count += 1
    else:
        avg_salary += employee_temp_salary
        total_count_with_salary += 1
    if employee[4] == 'STAFF ASSISTANT':
        staff_ass_workers += 1
        staff_ass_avg_salary += float(employee[2].replace('$', '').replace(',',''))
    if employee[1] == 'Detailee':
        detailee_workers += 1
        detailee_workers_avg_salary += float(employee[2].replace('$', '').replace(',',''))

    top_10.append((employee_temp_salary, n))

top_10.sort(reverse=True)
top_10 = top_10[:10]

print(f"Smallset salary ({round(smallest_salary)} USD) has {data[smallest_salary_id][0]}")
print(f"Largest salary ({round(largest_salary)} USD) has {data[largest_salary_id][0]}")
print(f"Average salary: {round(avg_salary/total_count_with_salary, 2)} USD")
print(f"No salary: {no_salary_count} worker(s)")
print(f"There are {staff_ass_workers} positions STAFF ASSISTANT with average salary "
      f"{round(staff_ass_avg_salary/staff_ass_workers, 2)} USD")
print(f"There are {detailee_workers} detailyee workers with average salary "
      f"{round(detailee_workers_avg_salary/detailee_workers, 2)} USD")
print("Top 10 salaries:")
for i, n in enumerate(top_10):
    print(f"{i+1}: {n[0]} USD ({data[n[1]][0]})")
#print(headers)
#print(data[0])