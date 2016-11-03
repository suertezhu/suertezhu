import Tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("500x500")

canvas = tk.Canvas(window,bg="green",width=500,height=400)

image_file = tk.PhotoImage(file='image.gif')
image = canvas.create_image(10,10,anchor="nw",image=image_file)

x0,x1,y0,y1 = 50,100,50,100
line = canvas.create_line(x0,y0,x1,y1)
cval = canvas.create_oval(x0,y0,x1,y1)
arc = canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start=0,extent=150)
rect = canvas.create_rectangle(100,30,150,60)
canvas.pack()

def moveit():
    canvas.move(rect,0,2)

b = tk.Button(window,text="move",command=moveit).pack()

window.mainloop()

