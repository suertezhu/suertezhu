import Tkinter as tk

window = tk.Tk()
window.title = ("my window")
window.geometry("200x150")


l = tk.Label(window,bg = "yellow",width = 200)
l.pack()

def print_selection(v):
    l.config(text = "the value is "+v)

sc = tk.Scale(window,label = "try me",length = 200,from_ = 0,to = 10,
              resolution = 0.01,showvalue = 0,tickinterval = 2,orient = tk.HORIZONTAL,command = print_selection)
sc.pack()

window.mainloop()
