import tkinter as tk

width = 500
height = 250

main = tk.Tk()
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()


main.geometry(f'{width}x{height}+0+0')

w1 = tk.Toplevel(main)
w2 = tk.Toplevel(main)
w3 = tk.Toplevel(main)
w4 = tk.Toplevel(main)

w1.geometry(f'{width}x{height}+{screen_width-width}+0')
w2.geometry(f'{width}x{height}+0+{screen_height-height}')
w3.geometry(f'{width}x{height}+{screen_width-width}+{screen_height-height}')
w4.geometry(f'{width}x{height}+{screen_width//2 - width//2}+{screen_height//2 - height//2}')

main.mainloop()