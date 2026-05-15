from tkinter import *
root=Tk()

def click(event):
    global scvalue         #so that we can change the scvalue ...
    text=event.widget.cget("text")           #cget..string me convert krta h aur ye sb screen me print hoga abhi..
    print(text)
    if text =="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        scvalue.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()





root.geometry("600x800")
root.title("calculator made by Ishika")


scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="lucida 40 bold")
screen.pack(padx=36,pady=35 ,fill=X)

f=Frame(root,bg="grey")
b1=Button(f,text="7",fg="black",bg="pink",font="lucida 20 bold",padx=5,pady=5)
b1.pack(side=LEFT,padx=6,pady=6)
b1.bind('<Button-1>',click)
b1=Button(f,text="8",fg="black",bg="pink",font="lucida 20 bold",padx=5,pady=5)
b1.pack(side=LEFT,padx=6,pady=6)
b1.bind('<Button-1>',click)
b1=Button(f,text="9",fg="black",bg="pink",font="lucida 20 bold",padx=5,pady=5)
b1.pack(side=LEFT,padx=6,pady=6)
b1.bind('<Button-1>',click)
b1=Button(f,text="+",fg="black",bg="pink",font="lucida 20 bold",padx=5,pady=5)
b1.pack(side=LEFT,padx=6,pady=6)
b1.bind('<Button-1>',click)
f.pack()                        #akele likhe kyuki button sara neeche show ho rha tha ....


f=Frame(root,bg="grey")
b1=Button(f,text="4",fg="black",bg="pink",font="lucida 20 bold",padx=5,pady=5)
b1.pack(side=LEFT,padx=10,pady=6)
b1.bind('<Button-1>',click)
b1=Button(f,text="5",fg="black",bg="pink",font="lucida 20 bold",padx=5,pady=5)
b1.pack(side=LEFT,padx=6,pady=6)
b1.bind('<Button-1>',click)
b1=Button(f,text="6",fg="black",bg="pink",font="lucida 20 bold",padx=5,pady=5)
b1.pack(side=LEFT,padx=6,pady=6)
b1.bind('<Button-1>',click)
b1=Button(f,text="-",fg="black",bg="pink",font="lucida 20 bold",padx=5,pady=5)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind('<Button-1>',click)
f.pack()                        #akele likhe kyuki button sara neeche show ho rha tha ....

f=Frame(root,bg="grey")
b1=Button(f,text="1",fg="black",bg="pink",font="lucida 20 bold",padx=5,pady=5)
b1.pack(side=LEFT,padx=9,pady=6)
b1.bind('<Button-1>',click)
b1=Button(f,text="2",fg="black",bg="pink",font="lucida 20 bold",padx=5,pady=5)
b1.pack(side=LEFT,padx=6,pady=6)
b1.bind('<Button-1>',click)
b1=Button(f,text="3",fg="black",bg="pink",font="lucida 20 bold",padx=5,pady=5)
b1.pack(side=LEFT,padx=6,pady=6)
b1.bind('<Button-1>',click)
b1=Button(f,text="*",fg="black",bg="pink",font="lucida 20 bold",padx=5,pady=5)
b1.pack(side=LEFT,padx=6,pady=6)
b1.bind('<Button-1>',click)
f.pack()                        #akele likhe kyuki button sara neeche show ho rha tha ....

f=Frame(root,bg="grey")
b1=Button(f,text="C",fg="black",bg="pink",font="lucida 20 bold",padx=5,pady=5)
b1.pack(side=LEFT,padx=6,pady=6)
b1.bind('<Button-1>',click)
b1=Button(f,text="0",fg="black",bg="pink",font="lucida 20 bold",padx=5,pady=5)
b1.pack(side=LEFT,padx=6,pady=6)
b1.bind('<Button-1>',click)
b1=Button(f,text="=",fg="black",bg="pink",font="lucida 20 bold",padx=5,pady=5)
b1.pack(side=LEFT,padx=6,pady=6)
b1.bind('<Button-1>',click)
b1=Button(f,text="/",fg="black",bg="pink",font="lucida 20 bold",padx=5,pady=5)
b1.pack(side=LEFT,padx=7,pady=6)
b1.bind('<Button-1>',click)
f.pack()                        #akele likhe kyuki button sara neeche show ho rha tha ....



root.mainloop()