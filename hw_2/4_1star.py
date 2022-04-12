
headers = []
f = open('weather_4.txt', 'r')
avg_value = 0

for i in range(10):
    headers.append(f.readline().strip())
data = f.readlines()
f.close()

#print(headers)


for n, v in enumerate(data):
    data[n] = data[n].strip().split(sep='\t')

#print(data[0])
print('Conditions:')
print('/ ', end='')
for i in headers:
    print(i, end=' / ')
print()
while True:
    choice = input('Type what average data you want to see: ').title()
    if choice == 'Time' or choice == 'Wind' or choice == 'Condition' or choice == 'Precip.':
        print(f'Unavailable to show avarage result for {choice}')
        continue
    choice_index = headers.index(choice)
    measurement_unit = []
    temp_data = list(data[0][choice_index])
    for i in range(len(temp_data)):
        #print(data[0][choice_index])
        if temp_data[len(temp_data)-i-1] == ' ':
            del temp_data
            measurement_unit = ''.join(measurement_unit)
            break
        measurement_unit.insert(0, temp_data[len(temp_data)-i-1])

    #print(float(data[0][choice_index].replace(measurement_unit, '').strip()))

    for i in data:
        avg_value += float(i[choice_index].replace(measurement_unit, '').strip())

    print(f"Avarage {choice} is: {round(avg_value/len(data), 1)} {measurement_unit}")

