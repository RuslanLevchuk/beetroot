import tkinter as tk
from tv_controller import *
import time
import types

global power
power = False
global screen
global sound_label

global image_path
global image
global screen_image
global info
global info_input
global is_exist_variable
global is_exist_entry_showed
is_exist_entry_showed = False
sound_label = 0
global TV
print(CHANNELS)

TV = TVController(CHANNELS)


def power_on(btn):
    global screen
    global power
    screen = tk.Toplevel(main)
    screen.title('GNUSMΛS')
    screen.geometry('800x450+800+200')

    screen.rowconfigure(0, weight=1)
    screen.rowconfigure(1, weight=5)
    screen.columnconfigure(0, weight=1)
    screen.columnconfigure(1, weight=9)

    btn.destroy()
    bt_power = tk.Button(main, text=" ⏼ ", font=('', 15), fg='green', command=lambda: power_off(bt_power, screen))
    bt_power.grid(row=0, column=0)
    print_channel(1)
    power = True


def power_off(btn, scr):
    global power
    scr.destroy()
    btn.destroy()
    bt_power = tk.Button(main, text=" ⏼ ", font=('', 15), fg='red', command=lambda: power_on(bt_power))
    bt_power.grid(row=0, column=0)
    power = False


def sound_off():
    global sound_label
    try:
        if sound_label == 0:
            sound_label = tk.Label(screen, text="🔇", font=('',20))
            sound_label.grid(row=0, column=0)
        else:
            sound_label.destroy()
            sound_label = 0
    except NameError:
        pass


def current_channel(n=0):
    global info
    global is_exist_entry_showed
    global is_exist_variable

    try:
        if info.winfo_exists() == 1:
            info.destroy()
    except NameError:
        pass

    try:
        if not n==0:
            info = tk.Label(screen, text=TV.is_exist(n), font=('', 20))
            info.grid(row=0, column=1, sticky=tk.E, padx=10)
            is_exist_entry_showed = False
        else:
            info = tk.Label(screen, text=TV.current_channel(), font=('',20))
            info.grid(row=0, column=1, sticky=tk.E, padx=10)
    except NameError:
        pass



def print_channel(n):

    global is_exist_entry_showed
    global is_exist_variable
    global image_path
    global image
    global screen_image
    global info_input
    global TV

    try:
        if info.winfo_exists() == 1:
            info.destroy()
    except NameError:
        pass

    if is_exist_entry_showed == True and isinstance(n, int):
        n = str(n)
        is_exist_variable.set(n)
        current_channel(n)

    if isinstance(n, int):
        TV.turn_channel(n)

    if callable(n):
        n()
        n=0

    if isinstance(n, int):
        if CHANNELS[TV.actual_channel] == 'BBC':
            image_path = 'images/bbc.png'
        elif CHANNELS[TV.actual_channel] == 'Discovery':
            image_path = 'images/Discovery.png'
        elif CHANNELS[TV.actual_channel] == 'УТ-1':
            image_path = 'images/ut1.png'
        elif CHANNELS[TV.actual_channel] == 'PornHUB':
            image_path = 'images/Pornhub.png'
        elif CHANNELS[TV.actual_channel] == 'ICTV':
            image_path = 'images/ICTV.png'
        try:
            image = tk.PhotoImage(file=image_path)
            screen_image = tk.Label(screen, image=image)
            screen_image.place(x=0, y=0, relwidth=1, relheight=1)
        except NameError:
            pass


def is_exist():
    global info
    global info_input
    global is_exist_variable
    global is_exist_entry_showed
    try:
        if info.winfo_exists() == 1:
            info.destroy()
    except NameError:
        pass
    try:
        is_exist_variable = tk.StringVar()
        info_input = tk.Entry(screen, textvariable=is_exist_variable, width=5)
        info_input.grid(row=0, column=1, sticky=tk.E, padx=10)
        is_exist_entry_showed = True
    except NameError:
        pass



main = tk.Tk()
main.title("GNUSMAS Control")

main.geometry('500x1000+200+200')
main.resizable(0, 0)

main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=1)
main.columnconfigure(2, weight=1)
main.rowconfigure(0, weight=1)
main.rowconfigure(1, weight=1)
main.rowconfigure(2, weight=1)
main.rowconfigure(3, weight=1)
main.rowconfigure(4, weight=1)
main.rowconfigure(5, weight=1)


bt_power = tk.Button(main, text=" ⏼ ", font=('', 15), fg='red', command=lambda: power_on(bt_power))
bt_power.grid(row=0, column=0)
bt_sound = tk.Button(main, text=" 🔇 ", font=('', 15), command=lambda: sound_off())
bt_sound.grid(row=0, column=2)

bt_1 = tk.Button(main, text=" 1 ", font=('', 15), command=lambda: print_channel(1))
bt_1.grid(row=1, column=0)
bt_2 = tk.Button(main, text=" 2 ", font=('', 15), command=lambda: print_channel(2))
bt_2.grid(row=1, column=1)
bt_3 = tk.Button(main, text=" 3 ", font=('', 15), command=lambda: print_channel(3))
bt_3.grid(row=1, column=2)

bt_4 = tk.Button(main, text=" 4", font=('', 15), command=lambda: print_channel(4))
bt_4.grid(row=2, column=0)
bt_5 = tk.Button(main, text=" 5 ", font=('', 15), command=lambda: print_channel(5))
bt_5.grid(row=2, column=1)
bt_6 = tk.Button(main, text=" 6 ", font=('', 15), command=lambda: print_channel(6))
bt_6.grid(row=2, column=2)

bt_7 = tk.Button(main, text=" 7 ", font=('', 15), command=lambda: print_channel(7))
bt_7.grid(row=3, column=0)
bt_8 = tk.Button(main, text=" 8 ", font=('', 15), command=lambda: print_channel(8))
bt_8.grid(row=3, column=1)
bt_9 = tk.Button(main, text=" 9 ", font=('', 15), command=lambda: print_channel(9))
bt_9.grid(row=3, column=2)

bt_first = tk.Button(main, text="first", font=('', 10), command=lambda: print_channel(TV.first_channel))
bt_first.grid(row=4, column=0)
bt_current = tk.Button(main, text="current", font=('', 10), command=current_channel)
bt_current.grid(row=4, column=1)
bt_last = tk.Button(main, text="last", font=('', 10), command=lambda: print_channel(TV.last_channel))
bt_last.grid(row=4, column=2)

bt_previous = tk.Button(main, text="prev", font=('', 10), command=lambda: print_channel(TV.previous_channel))
bt_previous.grid(row=5, column=0)
bt_is_exist = tk.Button(main, text="exsist?", font=('', 10), command=is_exist)
bt_is_exist.grid(row=5, column=1)
bt_next= tk.Button(main, text="next", font=('', 10), command=lambda: print_channel(TV.next_channel))
bt_next.grid(row=5, column=2)


main.mainloop()
