from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("310x370")
root.title("Calculator By Codingfizz")
root.wm_iconbitmap("1.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="light gray")
b = Button(f, text="9", padx=18, pady=15, font="lucida  10 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=18, pady=15, font="lucida  10 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=18, pady=15, font="lucida  10 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=18, pady=15, font="lucida  10 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="light gray")
b = Button(f, text="6", padx=18, pady=15, font="lucida  10 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=18, pady=15, font="lucida  10 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=18, pady=15, font="lucida  10 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=18, pady=15, font="lucida  10 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="light gray")
b = Button(f, text="3", padx=18, pady=15, font="lucida  10 bold")
b.pack(side=LEFT, padx=11, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=18, pady=15, font="lucida  10 bold")
b.pack(side=LEFT, padx=11, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=18, pady=15, font="lucida  10 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=19, pady=15, font="lucida  10 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="light gray")
b = Button(f, text="0", padx=18, pady=15, font="lucida  10 bold")
b.pack(side=LEFT, padx=11, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=18, pady=15, font="lucida  10 bold")
b.pack(side=LEFT, padx=11, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=18, pady=15, font="lucida  10 bold")
b.pack(side=LEFT, padx=11, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=18, pady=15, font="lucida  10 bold")
b.pack(side=LEFT, padx=11, pady=10)
b.bind("<Button-1>", click)

f.pack()


root.mainloop()
