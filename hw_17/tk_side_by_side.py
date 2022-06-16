import tkinter as tk


main = tk.Tk()
main.title("First one")
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

width = main.winfo_screenwidth()//3

main.geometry(f'{width}x{screen_height}+0+0')

w1 = tk.Toplevel(main)
w1.title('Second one')


w1.geometry(f'{width}x{screen_height}+{width}+0')


main.mainloop()