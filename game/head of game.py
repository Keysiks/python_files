import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
for x in range(0, 600, 20):
    canvas.create_oval((x, x), (x + 20, x + 20), fill='red')
canvas.pack()
master.mainloop()