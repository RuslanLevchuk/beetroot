#1
todo = ['to wake up', 'to taste come coffee', 'to do something', 'coffee brake', 'to do something else',
        'to do something again', 'to go to sleep']
#2
print(f"Tasks for a day: {todo[0]}, {todo[2]}, {todo[3]}, {todo[-1]}")
#3
todo_1, todo_2 = todo[:3], todo[3:]
print(todo_1)
print(todo_2)
#4
todo.append('to see some dreams')
print(todo)
#*
todo[0], todo[-1] = todo[-1], todo[0]
print(todo)
#*
todo.append(input('Type what you wanna else do: '))
for i, v in enumerate(todo):
        print(f"{i+1}: {v}")

#**
todo2 = todo
print(f"assign method ids: {id(todo)}, {id(todo2)}")
todo3 = todo[:]
print(f"slice method ids: {id(todo)}, {id(todo3)}")
todo4 = list(todo)
print(f"listing method ids: {id(todo)}, {id(todo4)}")
todo5 = todo.copy()
print(f"copy method ids: {id(todo)}, {id(todo5)}")