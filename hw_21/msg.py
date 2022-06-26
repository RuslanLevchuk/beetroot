import tkinter as tk
import sys

def kill():
    root.destroy()

data = sys.argv
time = 5000
message = 'Это сообщение!'
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
lb = tk.Label(text = message, font = ('Courier', '22'))
lb.pack()
root.mainloop()