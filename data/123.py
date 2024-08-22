from tkinter import *

tk = Tk()

tk.title("Clicker")
tk.geometry("600x400+200+100")
btn = Button(text=" :Боря Пидор)", width=15, height=7)
btn.pack()

n = 0


def nplus(event):
    global n
    n = n + 1
    label["text"] = str(n)


btn.bind('<Button-1>', nplus)
label = Label(tk, text=str(n), font="Helvetica")
label.pack()
tk.mainloop()
