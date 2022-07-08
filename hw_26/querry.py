import sqlite3
con = sqlite3.connect('wh.db')

cur = con.cursor()

print("Average salaries: ", end='')
for i in cur.execute("select avg(salary) average from sotr;"):
    print(i)


print("Top 10 salaries: ")
for i in cur.execute("select row_number() over (order by salary desc) num, name, salary, position_title from sotr limit 10;"):
    print(i)


print("Detailee vacantions: ")
for i in cur.execute("select count(*) total_datailee from sotr where status  = 'Detailee';"):
    print(i)


print("Staff assistant positions: ")
for i in cur.execute("select count(*) staff_assistant  from sotr where position_title = 'STAFF ASSISTANT';"):
    print(i)


print("Staff assistant average salary: ")
for i in cur.execute("select floor(avg(salary)) avg_salary_staff_assistant from sotr where position_title = 'STAFF ASSISTANT';"):
    print(i)

#довгі прінти, розкоментуйте, якщо дуже хочеться бачити
print("Total positions: ")
for i in cur.execute("select row_number() over (order by position_title) num, position_title from sotr group by position_title;"):
    #print(i)
    pass


print("Count staff on each position: ")
for i in cur.execute("select count(position_title) count, position_title from sotr group by position_title order by count desc;"):
    #print(i)
    pass

con.close()