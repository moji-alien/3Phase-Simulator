import tkinter as tk
import math,time

root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=600, borderwidth=0, highlightthickness=0, bg="gray10")
canvas.grid()
root.wm_title("Circles and Arcs")

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle_arc = _create_circle_arc
canvas.create_line(0,100,1000,100,fill='green')
canvas.create_line(0,200,1000,200,fill='white')
canvas.create_line(0,300,1000,300,fill='green')
canvas.create_line(0,400,1000,400,fill='white')
canvas.create_line(0,500,1000,500,fill='green')

xx=0
yy=0
c=0
txt=tk.Label(root,text='0',fg="white",bg='gray10')
txt.place(x=50,y=50)
txt.pack
txtg=tk.Label(root,text='0',fg="green",bg='gray10')
txtg.place(x=100,y=50)
txtg.pack
txtb=tk.Label(root,text='0',fg="blue",bg='gray10')
txtb.place(x=150,y=50)
txtb.pack
txtr=tk.Label(root,text='0',fg="red",bg='gray10')
txtr.place(x=200,y=50)
txtr.pack
def draw():
    global xx , yy , color , c ,txt,y2,yy2,yy3,w
    txt.config(text=xx)
    
#    if c == 0:
#        color="white"
#    if c == 1:
#        color="red"
#    if c == 2:
#        color='blue'
#    if c == 3:
#        color='yellow'
    xx+=1
    yy=int(300 + (math.sin((((xx*math.pi)*math.pi) / 600)+0) * 200))
    yy2=int(300 + (math.sin((((xx*math.pi)*math.pi) / 600)+2.09) * 200))
    yy3=int(300 + (math.sin((((xx*math.pi)*math.pi) / 600)+4.2) * 200))
    txtr.config(text=yy)
    txtb.config(text=yy3)
    txtg.config(text=yy2)
#    w=(300 + (math.sin((((xx*math.pi)*math.pi) / 120))))
#    print(w)
    canvas.create_circle(xx, yy, 2, fill="red2")
    canvas.create_circle(xx, yy2, 2, fill="green3")
    canvas.create_circle(xx, yy3, 2, fill="NavyBlue")
#    y2=int(300 + (math.sin((((xx-100)*math.pi)*math.pi) / 120) * 100))
#    canvas.create_circle(xx-100, (y2), 2, fill='black')
    if xx == 999:
#        c+=1
        time.sleep(1)
        xx=0
        canvas.create_rectangle(0,90,1000,510,fill='gray10',outline='gray10')
        canvas.create_line(0,100,1000,100,fill='green')
        canvas.create_line(0,200,1000,200,fill='white')
        canvas.create_line(0,300,1000,300,fill='green')
        canvas.create_line(0,400,1000,400,fill='white')
        canvas.create_line(0,500,1000,500,fill='green')
        
        
#        if c == 4:
#            c=0
#            pass
    root.after(10,draw)
draw()
root.mainloop()
