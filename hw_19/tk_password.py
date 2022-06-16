import tkinter as tk
import random
import time


def show():
    print(password.get())


main = tk.Tk()
main.title("Input password")

main.geometry('1000x500+200+200')
main.resizable(0, 0)

main.rowconfigure(0, weight=2)
main.rowconfigure(1, weight=1)
main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=98)
main.columnconfigure(2, weight=1)

top_frame = tk.Frame(main, background='gray')
top_frame.grid(row=0, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))

submit_btn = tk.Button(main, text='SUBMIT', font=('', 20), command=show)
submit_btn.grid(row=1, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))

password = tk.StringVar()

pass_label = tk.Label(top_frame, text="Input password:", font=('', 20), bg='gray')
pass_label.pack(pady=50)

pass_entry = tk.Entry(top_frame, textvariable=password, show="•")
pass_entry.pack(pady=40)


main.mainloop()
