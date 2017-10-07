# Créé par zankyo, le 29/09/2017 en Python 3.2

#bibliotheques
from tkinter import *
from random import *
from pygame import *

fen1=Tk()
fen1.title("cookies clicker")

#variables
coup=0
p=1
a=20
b=100
c=1000
d=5000
z=100
y=500
x=5000
w=20000
cpr=0

#commandes
def compt():
    global coup
    global p
    coup=coup+p
    txt2.config(text=coup)
def upgrade1():
    global coup
    global p
    global a
    global z
    if coup>=z:
        up1()
    txt2.config(text=coup)
    txt3.config(text=p)
    txt4.config(text=z)
def upgrade2():
    global coup
    global p
    global b
    global y
    if coup>=y:
        up2()
    txt2.config(text=coup)
    txt3.config(text=p)
    txt5.config(text=y)
def upgrade3():
    global coup
    global p
    global c
    global x
    if coup>=x:
        up3()
    txt2.config(text=coup)
    txt3.config(text=p)
    txt6.config(text=x)

def upgrade4():
    global coup
    global p
    global d
    global w
    if coup>=w:
        up4()
    txt2.config(text=coup)
    txt3.config(text=p)
    txt7.config(text=w)

def up1():
    global coup
    global p
    global a
    global z
    coup=coup-z
    z=z+a
    a=a+2
    p=p+1
def up2():
    global coup
    global p
    global b
    global y
    coup=coup-y
    y=y+b
    b=b+10
    p=p+7
def up3():
    global coup
    global p
    global c
    global x
    coup=coup-x
    x=x+c
    c=c+100
    p=p+100
def up4():
    global coup
    global p
    global d
    global w
    coup=coup-w
    w=w+d
    d=d+500
    p=p+500


#création d'objets
txt2=Label(fen1,text=coup)
txt3=Label(fen1,text=p)
txt4=Label(fen1,text=z)
txt5=Label(fen1,text=y)
txt6=Label(fen1,text=x)
txt7=Label(fen1,text=w)


but=Button(fen1,text="cookies",command=compt)
but1=Button(fen1,text="upgrade1",command=upgrade1)
but2=Button(fen1,text="upgrade2",command=upgrade2)
but3=Button(fen1,text="upgrade3",command=upgrade3)
but4=Button(fen1,text="upgrade4",command=upgrade4)


#placement
txt2.grid(row=2,column=2)
txt3.grid(row=1,column=1)
txt4.grid(row=5,column=4)
txt5.grid(row=5,column=5)
txt6.grid(row=7,column=4)
txt7.grid(row=7,column=5)

but.grid(row=2,column=1)
but1.grid(row=4,column=4)
but2.grid(row=4,column=5)
but3.grid(row=6,column=4)
but4.grid(row=6,column=5)



fen1.mainloop()

