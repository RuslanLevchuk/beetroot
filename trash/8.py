import copy

##Creating a tuple
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = ()
print(tup1)
print(tup2)

##New tuple using range
tup5=tuple(range(0,5),)*2
print(tup5)

tup3 = ('string',)*2
print(tup3)

##Accessing element in tuple
print ("tup1[0]: ", tup1[0])

##Range of element
print(tup1[0:2])

##Last element
print(tup1[-1])

##Check if element is in tuple
if 'physics' in tup1:
    print('Physics in tup1')



##Using for to access all elements
for i in tup1:
    print(i)

##Length
len(tup1)

tup4 = tup1 + tup2
print(tup4)

##Change or add new items
tup4=list(tup4)
tup4[0]='new item'
tup4.append('2005')
tup4=tuple(tup4)
print(tup4)

##Assigning None to tuple
tup3=None

print(type(tup3))


##Deleting tuple
#del(tup5)
#print(tup5)


##Useful methods in tuple
#Index
print(tup1.index(1997))

print(tup5.count(1))

##Inserting list inside tuple
list=[1,2,3]
tup6=(list,4,5)
print(tup6)

tup6[0][1]=7
print(tup6)

##Copy tuple (YOU CAN NOT)
#new_tup=tup6.copy()

##You can copy a tuple (CAN)
new_tup=copy.deepcopy(tup6)
print(new_tup)

new_tup1=tup6
print(new_tup1)

tup6=None
print(new_tup1)



print(id(new_tup1))

print(id(tup6))

print(id(new_tup))

##Why tuples are better than lists?
import sys
a_list=[1,2,3,4,5]
a_tuple=(1,2,3,4,5)

print(sys.getsizeof(a_list))
print(sys.getsizeof(a_tuple))

##Find maximum from tuple of ints
print(f'The max value of tup5 is {max(tup5)}')
print(f'The max value of tup5 is {min(tup5)}')


