#average
list_1 = [2, 64, 34, 12, 12]
index = 0
sum = 0

while index < len(list_1):
    sum += list_1[index]
    index += 1

avg = sum/len(list_1)
print(f'Average result is: {avg}')

#reverse
firstList = [1,2,3]
secondList=[]

counter = len(firstList)-1

while counter >= 0:
    secondList.append(firstList[counter])
    counter -= 1

print(f'Reversed list: {secondList}')

#copy
counter = 0
secondList=[]
while counter < len(firstList):
    secondList.append(firstList[counter])
    counter += 1
print(f'Copied list: {secondList}')

