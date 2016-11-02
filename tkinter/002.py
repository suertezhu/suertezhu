import Tkinter as tk

window = tk.Tk()
window.tittle = ("my window")
window.geometry = ("200x200")

var1 = tk.StringVar()
l = tk.Label(window,bg = "blue",height = 2,textvariable = var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

bt1 = tk.Button(window,text = "print selection",height = 2,command = print_selection)
bt1.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44,55))
lb = tk.Listbox(window,listvariable = var2)
lb.pack()

items = [5,4,3,2,1]

for item in items:
    lb.insert("end",item)

lb.insert(1,"test")

window.mainloop()









