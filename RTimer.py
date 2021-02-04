from tkinter import *

t=0
timer_on=False

def set_timer():
    global t
    t=t+int(e1.get())
    l1.config(text=disptime(t))
    return t

def start_timer():
    global timer_on
    timer_on = True
    countdown()

def countdown():
    global t
    if t>0 and timer_on == True:
        l1.config(text=disptime(t))
        t-=1
        l1.after(1000,countdown)
    elif t == 0:
        print("end")
        l1.config(text="Time up")

def stop_timer():
    global timer_on
    timer_on = False

def disptime(t):
    m,s = divmod(t, 60)
    h,m = divmod(m, 60)
    td = str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)
    return td

root = Tk()
root.geometry("200x250+900+250")

l1 = Label(root, text = disptime(t), font="times 40")
l1.pack(side=TOP, anchor=W, fill=X, expand=YES)
times = StringVar()
e1 = Entry(root, textvariable=times)
e1.pack(side=TOP, anchor=W, fill=X, expand=YES, padx=10)

b1 = Button(root, text="SET", command=set_timer)
b1.pack(side=TOP, anchor=W, fill=X, expand=YES, padx=10)
b2 = Button(root, text="START", command=start_timer)
b2.pack(side=TOP, anchor=W, fill=X, expand=YES, padx=10)
b3 = Button(root, text="STOP", command=stop_timer)
b3.pack(side=TOP, anchor=W, fill=X, expand=YES, padx=10)

root.mainloop()