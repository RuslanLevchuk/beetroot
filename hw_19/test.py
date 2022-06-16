import random

tools = {'rock': '▨', 'scissors': '✄', 'paper': '▭'}
computer_choice = random.choice(list(tools.keys()))
print(computer_choice)