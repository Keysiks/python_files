from tkinter import *
from random import *

left = 20


def s1():
    global left
    u = 1
    left = left - int(u)
    if left <= 0:
        sticks.congig(text="Компьютер победил")
        sticks.place(x=75, y=70)
    else:
        sticks.config(text=left * "| ")


def s2():
    global left
    u = 2
    left = left - int(u)
    if left <= 0:
        sticks.config(text="Компьютер победил")
        sticks.place(x=75, y=70)
    else:
        sticks.config(text=left * "| ")


def pc():
    global left
    a = randint(1, 3)
    if left == 4:
        a = 3
    elif left == 3:
        a = 2
    elif left == 2:
        a = 1
    left = left - int(a)
    if left <= 0:
        sticks.config(text="Игрок победил")
        sticks.place(x=140, y=70)
    else:
        sticks.config(text=left * "| ")


root = Tk()
root.geometry("550x200")

text1 = Label(root, text="Сколько палочек будем брать?")
text1.pack()

wbutt1 = Button(root, text="1", command=s1)
wbutt1.place(x=210, y=30)

wbutt2 = Button(root, text="2", command=s2)
wbutt2.place(x=265, y=30)

wbutt3 = Button(root, text="3", command=s1)
wbutt3.place(x=320, y=30)

sticks = Label(root, text=left * "| ")
sticks.config(font=("Arial", 30, 'bold'))
sticks.place(x=50, y=70)

pc_butt = Button(root, text="Ход компьютера", command=pc)
pc_butt.place(x=170, y=150)

root.resizable(0, 0)
root.title("Sticks")
root.mainloop()
