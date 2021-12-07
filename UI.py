# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 01:15:39 2008

@author: YABRIFA DIEPREYE
"""
from encryption_software import Encryption
from tkinter import *

class MyWindow:
    def __init__(self, win):

        self.lbl1 = Label(win, text = 'M1')
        self.lbl2 = Label(win, text = 'M2')
        self.lbl3 = Label(win, text = 'Cypher')
        self.t1 = Entry(bd=3)
        self.t2 = Entry()
        self.t3 = Entry()
        self.btn = Button (win,text = "Encrypt")
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1 = Button(win, text= "Encrypt", command = self.encrypt)
        self.b1.place(x=100, y= 150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)

        self.lbl4 = Label(win, text = 'cypher')
        self.lbl5 = Label(win, text = 'normal')
        self.t4 = Entry(bd=3)
        self.t5 = Entry()
        self.btn = Button (win,text = "Decrypt")
        self.lbl4.place(x=500, y=50)
        self.t4.place(x=600, y=50)
        self.b2 = Button(win, text= "Decrypt", command = self.decrypt)
        self.b2.place(x=800, y= 60)
        self.lbl5.place(x=500, y=100)
        self.t5.place(x=600, y=100)

    def encrypt(self):
        mc = Encryption()
        self.t3.delete(0, 'end')
        M1 = int(self.t1.get())
        M2 = int(self.t2.get())
        result = mc.encrypt(M1, M2)
        self.t3.insert(END, int(result))

    def decrypt(self):
        mc = Encryption()
        self.t5.delete(0, 'end')
        M1 = int(self.t4.get())
        result = mc.decrypt(M1)
        self.t5.insert(END, int(result))
Window = Tk()
MyWin = MyWindow(Window)
Window.title("damaris cipher")
Window.geometry('1000x900+10+10')
Window.mainloop()
