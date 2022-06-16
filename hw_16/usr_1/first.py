import tkinter as tk

root = tk.Tk()
root.title('I am rambo')
root.geometry('600x300+100+200')

lb = tk.Label(root, text = 'I am rambo label')
lb.grid()

btn = tk.Button(root, text = 'Rambo btn')
btn.grid()

btn2 = tk.Button(root, text = 'platform killer', command = root.destroy)
btn2.grid()

btn3 = tk.Button(root, text = 'Label killer', command = lb.destroy)
btn3.grid()


root.mainloop()
