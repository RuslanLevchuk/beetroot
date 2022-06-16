import tkinter as tk


main = tk.Tk()
width = main.winfo_screenwidth()
height = main.winfo_screenheight()


main.geometry(f'{width}x{height}+0+0')


main.mainloop()