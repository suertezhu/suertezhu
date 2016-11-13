import Tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("300x300")

l=tk.Label(window,bg="blue",text="empty",width=10).pack()

counter1 = 0
def do_job():
    global counter1
    l.config(text="do"+str(counter1))
    counter1+=1


menubar = tk.Menu(window)
filemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open",command=do_job)
filemenu.add_command(label="Save",command=do_job)
filemenu.add_command(label="New",command=do_job)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=window.quit)
submenu = tk.Menu(filemenu)
filemenu.add_cascade(label="import",menu=submenu,underline=0)
submenu.add_command(label="submennu1",command=do_job)

editmenu = tk.Menu(menubar,tearoff = 0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command=do_job)
editmenu.add_command(label="Copy",command=do_job)
editmenu.add_command(label="Paste",command=do_job)
editmenu.add_separator()
editmenu.add_command(label="Save",command=do_job)


window.config(menu=menubar)
window.mainloop()


