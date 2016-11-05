import Tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry("300x300")

tk.Label(window,text="main window").pack()

frm = tk.Frame(window).pack()
frm_l = tk.Frame(frm).pack(side="left")
frm_r = tk.Frame(frm).pack(side="right")

tk.Label(frm_l,text="frame on left").pack()

tk.Label(frm_l,text="frame on left2").pack()
tk.Label(frm_r,text="frame on right").pack()


window.mainloop()
