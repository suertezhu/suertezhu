import Tkinter as tk

window = tk.Tk()
window.title = ("my window")
window.geometry = ("200x100")

e = tk.Entry(window,show=None)
e.pack()
def insert_point():
    var=e.get()
    t.insert("insert",var)


def insert_end():
    var=e.get()
    t.insert("end",var)


b1 = tk.Button(window,text="insert point",width=15,height=2,command=insert_point)
b2 = tk.Button(window,text="insert end",width=15,height=2,command=insert_end)
b1.pack()
b2.pack()

t = tk.Text(window,height=2)
t.pack()
window.mainloop()


