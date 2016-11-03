import Tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("200x200")

l = tk.Label(window,bg="blue",width=20,text="empty").pack()

def print_selection():
    if (var1.get()==1) & (var2.get()==0):
        l.config(text="I ONLY LOVE PYTHON!")
    if (var1.get()==0) & (var2.get()==1):
        l.config(text="I ONLY LOVE C++!")
    if (var1.get()==1) & (var2.get()==1):
        l.config(text="I LOVE BOTH!")
    if (var1.get()==0) & (var2.get()==0):
        l.config(text="I don't like them at all!")




var1=tk.IntVar()
var2=tk.IntVar()
cb1 = tk.Checkbutton(window,text="python",variable=var1,onvalue=1,offvalue=0,
                     command=print_selection)
cb1.pack()
cb2 = tk.Checkbutton(window,text="C++",variable=var2,onvalue=1,offvalue=0,
                     command=print_selection)
cb2.pack()

print(var1)

window.mainloop()
