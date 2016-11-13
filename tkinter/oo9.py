import Tkinter as tk

window=tk.Tk()
window.title("my window")
window.geometry("300x300")


def ddd():
    tk.messagebox.showinfo(title="hi",message="hahhah")

b = tk.Button(window,text = 'click me',command=ddd).pack(side="left")








window.mainloop()
