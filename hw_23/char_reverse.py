def reverse(world):
    if type(world) == str:
        world = list(world)
    if len(world) == 1:
        return world[0]
    else:
        return world.pop()+reverse(world)


sentence = input('Type your phrase to reverse: ')

print(reverse(sentence))
