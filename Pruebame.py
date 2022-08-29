'''Brenda soy tu pendejo y fan numero uno
este programa lo hice con mucho cariño
te quiero '''
from cProfile import label
from tkinter import font, messagebox
from tkinter import *
import random
import sys

def obvio():
    messagebox.showinfo(message = "Lo sabia ;D !!", title="")

def button_hover(event):
    x = random.randint(10,400)
    y = random.randint(10, 400)
    my_button_2.place(x=x, y=y)

def exit_(event):
    x = random.randint(10,400)
    y = random.randint(10,400)
    my_button_2.place(x=x, y=y)

'''Aqui hacemos la interfaz grafica mi amor ;D'''
root = Tk()
root.geometry("600x400")
root.iconbitmap('home/cadena/Documentos/DeclaracionAmor/corazon.ico')
root.configure(background='#DA33FF')
root.title("Responde")
label_0 = Label(root, text="Quieres ser mi novia?", bg='#DA33FF', fg='black', width=0, font=("BubbleGum", 30) )
label_0.place(x = 90, y=60)
label_1 = Label(root, text="Brenda<3", bg='#DA33FF', fg='black', width=0, font=("BubbleGum", 30) )
label_1.place(x = 90, y=110)
my_button_1 =  Button(root, text="SI", width=5, height=1, font=("BubbleGum",30), bg='#FF4141', fg='white', command=obvio)
my_button_1.place(x=100, y=220)
my_button_2 =  Button(root, text="NO", width=5, height=1, font=("BubbleGum",30), bg='#FF4141', fg='white')
my_button_2.place(x=350, y=220)

my_button_2.bind("<Enter>", button_hover)
my_button_2.bind("<Leave>", exit_)

root.mainloop()