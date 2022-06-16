import tkinter as tk
import random


def check(value, bot_label):
    tools = {'rock': '▨', 'scissors': '✄', 'paper': '▭'}
    computer_choice = random.choice(list(tools.keys()))
    print(computer_choice)
    bot_label['text'] = tools[computer_choice]+' vs '+tools[value]
    if computer_choice == value:
        bot_label['text'] += ': no one won!'
    elif computer_choice=='rock' and value=='scissors' or computer_choice=='scissors' and value=='paper' or computer_choice=='paper' and value=='rock':
        bot_label['text'] += ': You loose...'
    else:
        bot_label['text'] += ': You won!'
    main.update_idletasks()


main = tk.Tk()
main.title("Slot Machine")

main.geometry('1000x500+200+200')
main.resizable(0, 0)

main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=1)
main.columnconfigure(2, weight=1)
main.rowconfigure(0, weight=1)
main.rowconfigure(1, weight=1)
main.rowconfigure(2, weight=1)

top_label = tk.Label(main, text="Select your tool!", font=('', 15))
top_label.grid(row=0, column=0, columnspan=3)
bot_label = tk.Label(main, text="", font=('', 20))
bot_label.grid(row=1, column=0, columnspan=3)


button1 = tk.Button(main, text=" ▨ ", font=('', 50), command=lambda: check('rock', bot_label))
button1.grid(row=2, column=0)

button2 = tk.Button(main, text=" ✄ ", font=('', 50), command=lambda: check('scissors', bot_label))
button2.grid(row=2,column=1)

button3 = tk.Button(main, text=" ▭ ", font=('', 50), command=lambda: check('paper', bot_label))
button3.grid(row=2, column=2)


main.mainloop()
