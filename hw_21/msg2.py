import tkinter as tk
from tkinter import messagebox as mb
import sys


def kill():
    root.destroy()


data = sys.argv
time = 5000
message = 'Cообщение!'
if len(data) > 1:
    message = data[1]
    if len(data) > 2:
        try:
            time = int(data[2])
        except ValueError:
            print("Second argument must contain integers only!")
            quit()

root = tk.Tk()
root.after(time, kill)
mb.showinfo(title='Это сообщение', message=message)
root.mainloop()