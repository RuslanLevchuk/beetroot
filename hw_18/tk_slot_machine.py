import tkinter as tk
import random
import time

result = ['X', 'X', 'X']


def generate():
    global symbols
    global result
    iter = 20
    while iter > 0:
        result = [str(random.randint(1, 9)), str(random.randint(1, 9)), str(random.randint(1, 9))]

        symbols['text'] = result
        symbols.pack()
        main.update_idletasks()
        iter -= 1
        time.sleep(0.05)


main = tk.Tk()
main.title("Slot Machine")

main.geometry('1000x500+200+200')
main.resizable(0, 0)

main.rowconfigure(0, weight=2)
main.rowconfigure(1, weight=1)
main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=98)
main.columnconfigure(2, weight=1)


top_frame = tk.Frame(main, background='gray')
top_frame.grid(row=0, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))

play_btn = tk.Button(main, text='PLAY!', command=generate)
play_btn.grid(row=1, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))

symbols = tk.Label(top_frame, bg='grey', text=''.join(result), font=('', 100))
symbols.pack()


main.mainloop()
