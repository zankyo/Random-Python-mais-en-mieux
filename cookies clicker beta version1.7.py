﻿# Créé par zankyo, le 29/09/2017 en Python 3.2

#bibliotheques
from tkinter import *
from random import *
from pygame import *
import threading


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
cps=0
e=60
f=300
g=500
h=2500
i=4000
j=20000
k=24000
l=120000



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
def func():
    global coup
    global cps
    coup=coup+cps
    txt2.config(text=coup)
    fen1.mainloop()
def cps1():
    global cps,coup,e,f
    if coup>=f:
        cps=cps+0.1
        coup=coup-f
        f=f+e
        e=e+6
        txt2.config(text=coup)
        txt1.config(text=cps)
        txt8.config(text=f)
def cps2():
    global cps,coup,g,h
    if coup>=h:
        cps=cps+1
        coup=coup-h
        h=h+g
        g=g+50
        txt2.config(text=coup)
        txt1.config(text=cps)
        txt9.config(text=h)
def cps3():
    global cps,coup,i,j
    if coup>=j:
        cps=cps+10
        coup=coup-j
        j=j+i
        i=i+400
        txt2.config(text=coup)
        txt1.config(text=cps)
        txt10.config(text=j)
def cps4():
    global cps,coup,k,l
    if coup>=l:
        cps=cps+50
        coup=coup-l
        l=l+k
        k=k+2400
        txt2.config(text=coup)
        txt1.config(text=cps)
        txt11.config(text=l)


#création d'objets
txt1=Label(fen1,text=cps)
txt2=Label(fen1,text=coup)
txt3=Label(fen1,text=p)
txt4=Label(fen1,text=z)
txt5=Label(fen1,text=y)
txt6=Label(fen1,text=x)
txt7=Label(fen1,text=w)
txt8=Label(fen1,text=f)
txt9=Label(fen1,text=h)
txt10=Label(fen1,text=j)
txt11=Label(fen1,text=l)

but=Button(fen1,text="cookies",command=compt)
but1=Button(fen1,text="upgrade1",command=upgrade1)
but2=Button(fen1,text="upgrade2",command=upgrade2)
but3=Button(fen1,text="upgrade3",command=upgrade3)
but4=Button(fen1,text="upgrade4",command=upgrade4)
but5=Button(fen1,text="cookies par sec 1",command=cps1)
but6=Button(fen1,text="cookies par sec 2",command=cps2)
but7=Button(fen1,text="cookies par sec 3",command=cps3)
but8=Button(fen1,text="cookies par sec 4",command=cps4)



#placement
txt1.grid(row=8,column=1)
txt2.grid(row=2,column=2)
txt3.grid(row=1,column=1)
txt4.grid(row=5,column=4)
txt5.grid(row=5,column=5)
txt6.grid(row=7,column=4)
txt7.grid(row=7,column=5)
txt8.grid(row=9,column=4)
txt9.grid(row=9,column=5)
txt10.grid(row=11,column=4)
txt11.grid(row=11,column=5)


but.grid(row=2,column=1)
but1.grid(row=4,column=4)
but2.grid(row=4,column=5)
but3.grid(row=6,column=4)
but4.grid(row=6,column=5)
but5.grid(row=8,column=4)
but6.grid(row=8,column=5)
but7.grid(row=10,column=4)
but8.grid(row=10,column=5)


def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

setInterval(func, 1)





