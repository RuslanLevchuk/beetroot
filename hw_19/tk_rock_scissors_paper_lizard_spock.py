import tkinter as tk
import random


def check(value, bot_label):
    tools = {'rock': '▨', 'scissors': '✄', 'paper': '▭', 'lizard': '↝', 'spock': '\V/.'}
    computer_choice = random.choice(list(tools.keys()))
    print(computer_choice)
    bot_label['text'] = tools[computer_choice]+' vs '+tools[value]
    if computer_choice == value:
        bot_label['text'] += ': no one won!'
    elif computer_choice=='rock' and value=='scissors' or computer_choice=='scissors' and value=='paper' or computer_choice=='paper' and value=='rock' or computer_choice=='rock' and value=='lizard' or computer_choice=='spock' and value=='rock' or computer_choice=='lizard' and value=='paper' or computer_choice=='paper' and value=='spock' or computer_choice=='scissors' and value=='lizard' or computer_choice=='spock' and value=='scissors' or computer_choice=='lizard' and value=='spock':
        bot_label['text'] += ': You loose...'
    else:
        bot_label['text'] += ': You won!'
    main.update_idletasks()


main = tk.Tk()
main.title("Slot Machine")

main.geometry('1500x500+200+200')
main.resizable(0, 0)

main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=1)
main.columnconfigure(2, weight=1)
main.columnconfigure(3, weight=1)
main.columnconfigure(4, weight=1)
main.rowconfigure(0, weight=1)
main.rowconfigure(1, weight=1)
main.rowconfigure(2, weight=1)

top_label = tk.Label(main, text="Select your tool!", font=('', 15))
top_label.grid(row=0, column=0, columnspan=5)
bot_label = tk.Label(main, text="", font=('', 20))
bot_label.grid(row=1, column=0, columnspan=5)


button1 = tk.Button(main, text=" ▨ ", font=('', 50), command=lambda: check('rock', bot_label))
button1.grid(row=2, column=0)

button2 = tk.Button(main, text=" ✄ ", font=('', 50), command=lambda: check('scissors', bot_label))
button2.grid(row=2,column=1)

button3 = tk.Button(main, text=" ▭ ", font=('', 50), command=lambda: check('paper', bot_label))
button3.grid(row=2, column=2)

button4 = tk.Button(main, text=" ↝ ", font=('', 50), command=lambda: check('lizard', bot_label))
button4.grid(row=2, column=3)

button5 = tk.Button(main, text="\V/.", font=('', 50), command=lambda: check('spock', bot_label))
button5.grid(row=2, column=4)


main.mainloop()

