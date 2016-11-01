#!/usr/bin/env pythonmZ# coding=utf-8
import Tkinter as tk


window = tk.Tk()
#window's size
window.title = ("this is my first try of tkinter")
window.geometry("200x100")
#label
var = tk.StringVar()
l = tk.Label(window,bg="green",textvariable=var,width=15,height=2)
l.pack()
#Button
on_click = False
def change():
    global on_click
    if on_click == False:
        on_click = True
        var.set("you click me")
    else:
        on_click = False
        var.set("....")

b = tk.Button(window,text="click",width=15,height=2,command=change)

b.pack()
window.mainloop()


