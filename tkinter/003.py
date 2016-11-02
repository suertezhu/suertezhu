import Tkinter as tk

window = tk.Tk()
window.title = ("my window")
window.geometry("200x400")

var = tk.StringVar()
l = tk.Label(window,width = 20, bg = "yellow",textvariable = var)
l.pack()
#label.config
def print_selection():
    l.config(text = "you have selected "+var)

t1 = tk.Radiobutton(window,text = "Option A",
                    variable = var,value = "A",
                    command = print_selection)
t1.pack()

t2 = tk.Radiobutton(window,text = "Option B",
                    variable = var,value = "B",
                    command = print_selection)
t2.pack()

t3 = tk.Radiobutton(window,text = "Option C",
                    variable = var,value = "C",
                    command = print_selection)
t3.pack()

t4 = tk.Radiobutton(window,text = "Option D",
                    variable = var,value = "D",
                    command = print_selection)
t4.pack()

window.mainloop()



