from tkinter import *
from tkinter import messagebox
import random

def Yes():
    messagebox.showinfo(' ', 'Спасибо! Ваш голос учтён!')
    quit()

def motionMouse(event):
    btnNo.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = Tk()
root.geometry('600x600')
root.title('Опрос')
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text='Федюшкин Пидор?', font='Arial 20 bold', bg='white')
label.pack()

btnYes = Button(root, text='Да', font='Arial 20 bold')
btnYes.place(x=170, y=100)

btnNo = Button(root, text='Нет', font='Arial 20 bold', command=NO)
btnNo.place(x=350, y=100)

btnNo.bind('<Enter>', motionMouse)

root.mainloop()